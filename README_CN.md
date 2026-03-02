# Agent Harness Skill

基于 OpenAI 的 Harness Engineering 方法论和 Anthropic 长效智能体架构的 AI 智能体开发框架。

## 概述

Agent Harness Skill 提供了一套完整的智能体开发工具和最佳实践，帮助开发者构建高效、可维护、可观测的 AI 驱动应用。

### 核心理念

1. **单智能体，串行执行**：避免决策冲突，保持清晰的执行流程
2. **记忆外部化**：使用文件、git、日志作为持久化记忆，不依赖上下文窗口
3. **默认失败**：所有功能初始状态为 `passes: false`，完成后再标记为成功
4. **一次一个功能**：不进行多任务处理，保持专注
5. **整洁状态是必须的**：永远不要留下破坏的代码
6. **可观测性是一等公民**：给智能体眼睛（UI）和听诊器（日志/指标）
7. **JSON > Markdown**：结构化数据使用 JSON，模型容易破坏 Markdown 结构
8. **构建以删除**：Harness 代码终将过时，保持轻量
9. **成本反转**：高吞吐量 = 最小化阻塞关卡
10. **知识在仓库中**：如果没有版本控制，对于智能体来说就不存在

## 项目结构

```
agent-harness-skill/
├── agent-harness/
│   ├── SKILL.md              # 技能定义文件
│   ├── docs/                 # 文档模板
│   │   ├── architecture/     # 架构文档
│   │   ├── design/           # 设计文档
│   │   ├── principles/       # 核心原则
│   │   └── tools/            # 工具文档
│   ├── scripts/              # 脚本工具
│   │   ├── setup_harness.py  # 项目初始化脚本
│   │   └── update_feature.py # 功能状态更新脚本
│   ├── references/           # 参考资料
│   └── assets/               # 资源文件
└── README.md                  # 英文版本
└── README_CN.md               # 中文版本（本文件）
```

## 初始化后的项目结构

当你运行初始化脚本时，会创建：

```
your-project/
├── .harness/                 # 所有 harness 文件都在这里
│   ├── project.md           # 知识地图（导航入口）
│   ├── docs/                # 文档
│   ├── features.json        # 功能跟踪（全部初始化为 FALSE！）
│   ├── progress.md          # 会话进度日志
│   └── init.sh              # 开发服务器启动脚本
```

## 快速开始

### 安装 Skill

将 `agent-harness.skill` 文件安装到你的 Claude Desktop 或支持技能的 IDE 中。

### 初始化新项目

在新项目目录中运行：

```bash
python setup_harness.py --project-name "My Awesome Project" --project-type web
```

这将创建：
- `.harness/project.md` - 知识地图
- `.harness/docs/` - 完整的文档目录
- `.harness/features.json` - 功能跟踪清单
- `.harness/progress.md` - 会话进度日志
- `.harness/init.sh` - 开发服务器启动脚本

## 核心文档

- [架构概览](agent-harness/docs/architecture/overview.md) - 理解整体架构
- [核心原则](agent-harness/docs/principles/core.md) - 我们的信念
- [入门指南](agent-harness/docs/design/getting-started.md) - 新项目的第一步
- [分层架构](agent-harness/docs/architecture/layers.md) - 代码结构规范
- [黄金规则](agent-harness/docs/principles/golden-rules.md) - 可执行的工程标准

## 工作流程

1. **读取知识地图** - 每次会话开始先读 `.harness/project.md`
2. **遵循会话启动序列** - 按照 `.harness/docs/design/session-startup.md` 执行
3. **一次一个功能** - 从 `.harness/features.json` 中选择下一个功能
4. **保持整洁状态** - 结束时确保代码可运行
5. **记录进度** - 更新 `.harness/progress.md`

## 脚本工具

### setup_harness.py

初始化新项目的 harness 文件。

```bash
python setup_harness.py [OPTIONS]

Options:
  --project-name TEXT    项目名称
  --project-type TEXT    项目类型 [web|backend|data]
  --output-dir TEXT      输出目录
  --skip-docs            跳过 docs 目录复制
```

### update_feature.py

更新功能的通过/失败状态。

```bash
python update_feature.py [OPTIONS]

Options:
  --feature-index INTEGER  功能索引（0 基）
  --feature-id TEXT        功能 ID（索引的替代方案）
  --passes BOOLEAN         True 或 False
  --file TEXT              Features 文件路径
```

## 参考文献

- [OpenAI Harness Engineering](https://openai.com/index/harness-engineering)
- [Anthropic 长效智能体架构](https://www.anthropic.com/index/long-running-agents)

## 许可证

本项目遵循适用的开源许可证。
