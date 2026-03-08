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

**The Reflexion Loop (Design -> Code -> Review -> Test -> Fix) is NOT an optional step. It IS the workflow.**

**MANDATORY EXECUTION PATH:**
When implementing features or fixing bugs, you **MUST** follow the steps in **[Module 4: Incremental Development Workflow](modules/development-workflow.md)**.
- **Violation of the "STOP" protocol** (retrying without observation) is a critical failure.
- **Violation of the "Clean State" protocol** (leaving broken code) is a critical failure.

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

1. **Linter Error = Fix Instruction**
   - When a linter reports an error, it is providing a **specific prompt** for remediation.
   - You MUST read the error message as a directive and refactor the code immediately.
   - **DO NOT** ignore, suppress, or bypass linter errors.

2. **Zero Tolerance Policy**
   - A task is **NOT complete** until all linter checks pass.
   - Linter violations are treated with the same severity as compilation errors or failing tests.

3. **Autonomous Refactoring**
   - You are expected to resolve architecture violations (e.g., layering issues, forbidden patterns) **autonomously**.
   - Do not ask the user for permission to fix a linter error; just fix it.

**Detailed Rules & Examples:**
👉 **[Module 5: Architecture Constraint Enforcement](modules/architecture-enforcement.md)**

## Next Steps (Progressive Disclosure)

**Start here first, then go deeper as needed:**

1. **[Complete Workflow](workflow.md)** - 5 阶段执行流程
2. **[Core Module Details](modules.md)** - 实现细节、文件模板和具体策略

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
