---
name: harness
description: Use when initializing projects, implementing features, fixing bugs, or refactoring code. Enforces strict engineering protocols and verification loops.
---

# Harness Engineering Skill

## Overview

Systematically implements the Harness Engineering methodology, enabling agents to work in a stable, controllable, and verifiable environment.

**Core Philosophy:**
- **Design Environment**: Build scaffolding (CI, Lint, Directory Structure) for agents to thrive.
- **Clarify Intent**: Deconstruct requirements into unambiguous specs.
- **Build Feedback Loop**: Use Reflexion Loop as the **Main Execution Engine**.

> **🗺️ PROJECT MAP**: The file **`AGENTS.md`** in the project root is your primary navigation map. It indexes all documentation, plans, and feature lists. **Always read it first.**

## 🚦 Role-Based Dispatcher (Start Here)

**Identify your current mission and follow the link:**

| Mission Type | Your Role | ⚡️ Action Protocol |
| :--- | :--- | :--- |
| **Start New Project** | Initializer Agent | 👉 **[Module 1: Project Initialization](modules/initialization.md)** |
| **Implement Feature** | Coding Agent | 👉 **[Module 4: Development Workflow](modules/development-workflow.md)** |
| **Fix Bug / Refactor** | Coding Agent | 👉 **[Module 4: Development Workflow](modules/development-workflow.md)** |
| **Plan / Design** | Architect Agent | 👉 **[Module 3: Feature Management](modules/feature-management.md)** |
| **Submit Code** | Reviewer Agent | 👉 **[Module 6: Code Merge Strategy](modules/code-merge.md)** |

> **⚠️ Critical Warning:**
> The Reflexion Loop (Design -> Code -> Review -> Test -> Fix) is NOT an optional step. It IS the workflow.
> - **Violation of the "STOP" protocol** (retrying without observation) is a critical failure.
> - **Violation of the "Clean State" protocol** (leaving broken code) is a critical failure.

## Unbreakable Iron Laws

1. **Clean State** - Code must be runnable at end of each session.
2. **One Feature At A Time** - Never allow handling multiple features simultaneously.
3. **Knowledge Must Be In Repository** - If it's not in the repo (file/doc), it doesn't exist.
4. **Architecture Is Law** - Layering and Providers pattern must be enforced.
5. **Observability First** - Agent must "see" system state (logs, metrics, screenshots) to verify itself.
6. **Test-Driven Development** - Write the test/reproduction script FIRST. Prove failure before fixing.
7. **Choose Boring Technology** - Prefer mature, stable tech stacks that agents understand best.

## Architecture & Linter Enforcement Protocol

**Treat Linters as Context Injection, NOT just error reporting.**

1. **Linter Error = Fix Instruction**: Do not ask permission. Fix immediately.
2. **Zero Tolerance**: Task is NOT complete until all linter checks pass.
3. **Autonomous Refactoring**: Resolve architecture violations autonomously.

👉 **Detailed Rules:** **[Module 5: Architecture Constraint Enforcement](modules/architecture-enforcement.md)**

## Common Rationalizations & Reality Checks

| Excuse | Reality |
|--------|---------|
| "It's just a small fix, I'll skip the test" | Small fixes break big systems. Test first. |
| "I'll update the docs later" | Later never comes. Knowledge outside repo doesn't exist. |
| "This architecture is too rigid" | Constraints enable speed. Without guardrails, you crash. |
| "I can handle multiple features at once" | Context windows are finite. Serial execution prevents amnesia. |
| "Waiting for tests is slow" | Debugging is the most expensive activity. TDD is the only shortcut. |
| "This new tech is cool" | Boring tech is predictable. Agents need predictability, not hype. |

## When Should Stop and Ask

- Plan has critical gaps cannot start
- Don't understand an instruction
- Verification repeatedly fails
- Encountering situations involving directional choices
