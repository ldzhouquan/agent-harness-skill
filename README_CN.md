# Harness Engineering Skill

Harness Engineering 方法论的系统化实现，使 AI 智能体能够在稳定、可控和可验证的环境中工作。集成了 Anthropic 的长效智能体架构、OpenAI 的 Harness Engineering 方法论，以及 Agent Harness 作为 AI 时代操作系统的概念。

## 概述

Harness Engineering Skill 提供了一个完整的框架，用于构建具有纪律性、稳定性和可验证性的 AI 驱动应用。它将重点从直接编写代码转移到设计环境、反馈循环和控制系统，使智能体能够有效地工作。

## 核心理念

### 1. 单智能体串行架构
- 避免多智能体决策冲突
- 同一大脑在不同模式下工作：初始化器智能体 vs 编码智能体
- 只有串行才能保证整洁状态的交接

### 2. 外部记忆系统
- 依赖文件系统、日志和 Git 历史，而不是内部记忆
- 通过结构化文件传递工作，消除遗忘风险
- 持久化日志和 Git 历史使新会话独立

### 3. 整洁状态
- 每个会话结束时，代码必须可运行，文档必须更新
- 满足主分支合并标准
- 永远不要为下一班留下破坏的代码
- Git 回滚机制确保稳定性

### 4. 结构化知识库
- 使用 `AGENTS.md` 作为地图（目录），而不是手册
- 使用 `docs/` 目录存储详细知识
- 渐进式信息披露
- 知识必须在仓库中 - 如果不在，就不存在

### 5. 架构即法律
- 强制执行不变量，不微观管理实现
- 分层架构：代码只能向前依赖，永远不能向后
- Providers 模式：所有公共能力通过统一入口
- Linter 作为提示：自定义 linter 提供修复说明

### 6. 可观测性优先 (Observability First)
- 智能体必须"看见"系统状态以进行自我验证
- 给智能体装上"眼睛"（截图/DOM快照）和"耳朵"（日志/指标）
- 测试失败 = 停止 -> 观察 -> 假设 -> 修复

### 7. 测试驱动开发 (Test-Driven Development)
- 先写测试/复现脚本
- 在修复前证明失败
- 快速且廉价地失败（脚本）vs 缓慢且昂贵地失败（生产环境）
- 没有验证的代码是不完整的

## 项目结构

```
agent-harness/
├── SKILL.md              # 技能定义文件
├── workflow.md           # 完整工作流和检查清单
├── modules.md            # 核心模块索引
└── modules/              # 详细模块文档
    ├── initialization.md      # 项目初始化模板
    ├── knowledge-base.md      # 知识库管理
    ├── feature-management.md  # 功能清单管理
    ├── development-workflow.md # 增量开发
    ├── architecture-enforcement.md # 架构约束
    ├── code-merge.md          # 代码合并策略
    ├── autonomous-development.md # 端到端自治
    └── technical-debt.md      # 技术债务处理
```

## 5 阶段工作流

### 阶段 1：项目初始化（初始化器智能体）
设置环境，创建知识库结构，建立基本约束。

**创建的关键文件：**
- `AGENTS.md` - 项目地图（导航入口）
- `architecture.md` - 架构鸟瞰图
- `feature_list.json` - 功能清单（全部 pass: false）
- `progress.txt` - 进度日志
- `docs/` 目录结构

### 阶段 2：功能规划
创建结构化功能清单，明确所有需求。

### 阶段 3：增量开发（编码智能体）
一次一个功能，保持整洁状态。

**启动序列（每个会话必须执行）：**
1. **Locate** - 运行 `pwd` 确认工作目录
2. **Ground** - 运行 `ls -R` 并读取配置文件以了解环境
3. **Recall** - 读取 `progress.txt`、`feature_list.json` 和 `git log -20`
4. **Verify** - 在开始前运行基础测试以确认系统健康
5. **Claim** - 选择优先级最高且 `pass: false` 的功能

### 阶段 4：验证与合并
测试、审查、合并，保持高吞吐量。

### 阶段 5：持续维护
持续清理技术债务，保持架构一致性。

## 不可打破的铁律

1. **整洁状态原则不可打破** - 每个会话结束时代码必须可运行
2. **一次一个功能** - 永远不允许同时处理多个功能
3. **知识必须在仓库中** - 重要信息必须写入文件
4. **架构即法律** - 必须强制执行分层和 Providers 模式
5. **构建以删除** - Harness 代码必须轻量级以便于重构

## 常见借口与现实检查

| 借口 | 现实 |
|------|------|
| "这只是一个小修复，我会跳过测试" | 小修复会破坏大系统。先测试。 |
| "我稍后会更新文档" | 稍后永远不会来。仓库外的知识不存在。 |
| "这个架构太僵化了" | 约束带来速度。没有护栏，你会撞车。 |
| "我可以同时处理多个功能" | 上下文窗口是有限的。串行执行防止遗忘。 |
| "等待测试太慢了" | 稍后修复 bug 慢 10 倍。成本函数反转适用。 |

## 快速开始

### 安装 Skill

将技能安装到你的 Trae IDE 或支持技能的环境中：

1. 将 `agent-harness/` 目录复制到你的技能目录
2. 或使用提供的安装脚本

### 初始化新项目

按照 [workflow.md](agent-harness/workflow.md) 中的初始化检查清单：

1. 初始化 Git 仓库
2. 使用模板创建 `AGENTS.md`
3. 创建 `architecture.md`
4. 设置 `docs/` 目录结构
5. 创建 `feature_list.json`
6. 创建 `progress.txt`

## 关键文档

- **[SKILL.md](agent-harness/SKILL.md)** - 技能定义和核心理念
- **[workflow.md](agent-harness/workflow.md)** - 完整工作流和检查清单
- **[modules.md](agent-harness/modules.md)** - 核心模块索引
- **[modules/initialization.md](agent-harness/modules/initialization.md)** - 项目初始化模板

## 记住

- **不要问智能体能为你做什么，问你能为智能体提供什么**
- **给智能体一张地图，而不是一本手册**
- **架构即法律，Linter 即提示，规则即乘数**
- **修复便宜，等待昂贵**
- **构建以删除 - Harness 是数据帐篷**
- **纪律正从代码本身转向工程脚手架**
- **现在最困难的挑战集中在设计环境、反馈循环和控制系统上**

## 参考文献

- [OpenAI Harness Engineering](https://openai.com/index/harness-engineering)
- [Anthropic 长效智能体](https://www.anthropic.com/index/long-running-agents)

## 许可证

本项目遵循适用的开源许可证。
