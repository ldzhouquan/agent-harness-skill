# 🛡️ Harness Engineering Skill

> The Operating System for Autonomous AI Agents. (自主 AI 智能体的操作系统)

[English Documentation](README.md)

系统化实施 **Harness Engineering** 方法论，使智能体能够在稳定、可控和可验证的环境中工作。它将关注点从"直接写代码"转移到"设计反馈循环"和"控制系统"上。

## 🚀 为什么选择 Harness Engineering？

### 1. 彻底消除"失忆" (Eliminate Amnesia)
- **痛点**: 智能体工作是离散的会话（Session）。新会话启动时，Agent 是全新的、完全失忆的，无法接续上一轮的工作。
- **解法**: 强制执行 **Context Discovery Protocol**。Agent 每次唤醒时，通过读取标准化的 `progress.txt` 和 `feature_list.json`，在 5 秒内恢复完整的项目上下文。

### 2. 终结代码幻觉 (Stop Hallucinations)
- **痛点**: 智能体经常写出"看起来对但跑不通"的代码，或者幻想不存在的 API。
- **解法**: **Test-Driven Development (TDD)** + **Reflexion Loop**。在编写实现代码前，必须先写出失败的测试。没有测试证据，代码就不存在。

### 3. 防止架构腐化 (Prevent Architecture Rot)
- **痛点**: 随着项目变大，智能体容易引入循环依赖，破坏分层结构。
- **解法**: **Architecture as Law**。自定义 Linter 规则不仅仅是建议，而是不可逾越的红线。CI 管道会直接拦截任何违规代码。

### 4. 赋予系统"感官" (Give Agents Senses)
- **痛点**: 智能体在"盲写"代码，无法像人类一样看到运行时错误或界面异常。
- **解法**: **Observability First**。集成日志分析和截图验证，强制 Agent 在修改代码前先"观察"系统状态。

## 📦 快速开始 (Getting Started)

### 1. 安装

**方式一：** 直接告诉 Claude：
> 使用 `https://github.com/ldzhouquan/agent-harness-skill` 的 Harness skill

**方式二：** 克隆并链接：
```bash
git clone https://github.com/ldzhouquan/agent-harness-skill.git
ln -s agent-harness-skill/Harness ~/.claude/skills/Harness
```

### 2. 初始化 (Initialization)
告诉你的 Agent（或在 System Prompt 中添加）：

> "/Harness Please set up a new project for me."

### 3. 验证 (Verification)
Agent 应该会自动开始执行 **Module 1: Project Initialization**，并创建 `AGENTS.md` 和 `progress.txt`。

## 📂 项目结构

```
Harness/
├── SKILL.md              # 🚦 塔台（所有 Agent 的统一入口）
├── workflow.md           # 📋 详细执行清单
├── Tools/                # 🛠️ 工具脚本
├── scripts/              # 📜 自动化脚本
├── references/           # 📚 参考资料
│   ├── initialization/
│   ├── bugfix/
│   └── development/
└── modules/              # 📚 核心知识模块
    ├── initialization.md           # 初始化 & 金钉子验证
    ├── feature-management.md       # 规划与规格说明
    ├── development-workflow.md    # 反思循环 (The Loop)
    ├── bug-fix-protocol.md        # Bug 修复协议 (TDD)
    ├── architecture-enforcement.md # 架构铁律
    ├── code-merge.md             # 审查与合并策略
    ├── autonomous-development.md   # 端到端自治
    ├── technical-debt.md          # 技术债务清理协议
    └── progress-tracking.md       # 进度追踪
```

## ⚡️ 工作流概览

1.  **Init**: 设置 CI/Lint/Test -> 跑通 "Golden Spike" (Hello World)。
2.  **Plan**: 将需求解构为 `feature_list.json`。
3.  **Dev**: 循环 `Locate -> Ground -> Recall -> Verify -> Claim`。
4.  **Reflexion**: `Design -> Code -> Test -> Fix` (核心引擎)。
5.  **Merge**: 验证整洁状态 -> 合并。

## 🔗 快速链接

- **[SKILL.md](Harness/SKILL.md)**: **从此开始 (START HERE)** - 所有智能体的唯一入口。
- **[工作流](Harness/workflow.md)**: 详细的分步执行指南。
