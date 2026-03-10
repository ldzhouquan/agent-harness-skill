# 🛡️ Harness Engineering Skill

> The Operating System for Autonomous AI Agents.

A systematic implementation of **Harness Engineering**, enabling agents to work in a stable, controllable, and verifiable environment. It shifts focus from "writing code" to "designing feedback loops".

## 🚀 Why Harness Engineering?

### 1. Eliminate Amnesia
- **Pain**: Agents operate in discrete sessions. When a new session starts, the agent is fresh and completely amnesic, unable to continue previous work.
- **Solution**: Enforce **Context Discovery Protocol**. Agents recover full project context within 5 seconds by reading standardized `progress.txt` and `feature_list.json` upon wake-up.

### 2. Stop Hallucinations
- **Pain**: Agents often write code that "looks right but doesn't run", or hallucinate non-existent APIs.
- **Solution**: **Test-Driven Development (TDD)** + **Reflexion Loop**. Before writing implementation code, a failing test script must be written. No test evidence = code does not exist.

### 3. Prevent Architecture Rot
- **Pain**: As projects grow, agents easily introduce circular dependencies and break layering.
- **Solution**: **Architecture as Law**. Custom Linter rules are not just suggestions, but unbreakable red lines. CI pipelines directly block any violating code.

### 4. Give Agents Senses
- **Pain**: Agents code "blindly", unable to see runtime errors or UI anomalies like humans do.
- **Solution**: **Observability First**. Integrate log analysis and screenshot verification, forcing agents to "observe" system state before modifying code.

## 📦 Getting Started

### 1. Installation
Copy the `agent-harness/` directory to your project root.

```bash
cp -r /path/to/agent-harness-skill/agent-harness ./agent-harness
```

### 2. Initialization
Tell your Agent (or add to System Prompt):

> "I have installed the Harness Engineering Skill in `./agent-harness`. Please read `agent-harness/SKILL.md` to start the initialization process."

### 3. Verification
The Agent should automatically start **Module 1: Project Initialization** and create `AGENTS.md` and `progress.txt`.

## 📂 Project Structure

```
agent-harness/
├── SKILL.md              # 🚦 Traffic Control Tower (Entry Point)
├── workflow.md           # 📋 Detailed Checklists
└── modules/              # 📚 Knowledge Modules
    ├── initialization.md      # Setup & Golden Spike
    ├── knowledge-base.md      # Documentation Strategy
    ├── feature-management.md  # Planning & Specs
    ├── development-workflow.md # The Loop
    ├── architecture-enforcement.md # The Law
    ├── code-merge.md          # Review & Merge
    ├── autonomous-development.md # E2E Autonomy
    └── technical-debt.md      # Cleanup Protocols
```

## ⚡️ Workflow Overview

1.  **Init**: Setup CI/Lint/Test -> Run "Golden Spike" (Hello World).
2.  **Plan**: Deconstruct requirements into `feature_list.json`.
3.  **Dev**: Loop `Locate -> Ground -> Recall -> Verify -> Claim`.
4.  **Reflexion**: `Design -> Code -> Test -> Fix` (The Engine).
5.  **Merge**: Verify clean state -> Merge.

## 🔗 Quick Links

- **[SKILL.md](agent-harness/SKILL.md)**: **START HERE** - The main entry point for all agents.
- **[Workflow](agent-harness/workflow.md)**: Detailed step-by-step execution guide.
