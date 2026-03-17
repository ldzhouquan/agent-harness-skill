---
name: Harness
description: Use when initializing projects, implementing features, fixing bugs, or refactoring code. Enforces strict engineering protocols and verification loops.
---

# Harness

Systematically implements the Harness Engineering methodology, enabling agents to work in a stable, controllable, and verifiable environment.

## Workflow Modules

> ⚠️ **Agent MUST read the appropriate module based on task context**

- **Initialize** → `modules/initialization.md` — new projects, setup
- **Develop** → `modules/development-workflow.md` — implement features
- **FixBug** → `modules/bug-fix-protocol.md` — fix bugs, test failures
- **Verify** → `modules/code-merge.md` — merge, submit, PR
- **Maintain** → `modules/technical-debt.md` — cleanup, optimize
- **TrackProgress** → `modules/progress-tracking.md` — update progress
- **EnforceArchitecture** → `modules/architecture-enforcement.md` — architecture checks
- **Autonomous** → `modules/autonomous-development.md` — full control mode


## Core Philosophy

- **Design Environment**: Build scaffolding (CI, Lint, Directory Structure) for agents to thrive.
- **Clarify Intent**: Deconstruct requirements into unambiguous specs.
- **Build Feedback Loop**: Use Reflexion Loop as the **Main Execution Engine**.

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

1. **Linter Error = Fix Instruction**: Do not ask permission. Fix immediately.
2. **Zero Tolerance**: Task is NOT complete until all linter checks pass.
3. **Autonomous Refactoring**: Resolve architecture violations autonomously.

👉 **Detailed Rules:** **[Module 5: Architecture Constraint Enforcement](modules/architecture-enforcement.md)**

## When Should Stop and Ask

- **Requirements unclear** - e.g., "build an API" without specifying language/framework → ask first
- **Missing verification plan** - cannot start without knowing how to verify → ask first
- **Don't understand an instruction** - ask before proceeding
- **Verification repeatedly fails** - stop and analyze root cause
- **Technology/direction choices required** - which language, which framework → ask first