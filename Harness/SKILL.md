---
name: Harness
description: Use when initializing projects, implementing features, fixing bugs, or refactoring code. Enforces strict engineering protocols and verification loops.
---

# Harness

Systematically implements the Harness Engineering methodology, enabling agents to work in a stable, controllable, and verifiable environment.

## Voice Notification

**When executing a workflow, do BOTH:**

1. **Send voice notification**:
   ```bash
   curl -s -X POST http://localhost:8888/notify \
     -H "Content-Type: application/json" \
     -d '{"message": "Running WORKFLOWNAME in Harness"}' \
     > /dev/null 2>&1 &
   ```

2. **Output text**: `Running the **WorkflowName** workflow in the **Harness** skill to ACTION...`

## Workflow Routing

| Workflow | Phase | Trigger | File |
|----------|-------|---------|------|
| **Initialize** | 1 | "start new project", "initialize project" | `modules/initialization.md` |
| **PlanFeature** | 2 | "plan feature", "add feature" | `modules/feature-management.md` |
| **Develop** | 3 | "implement feature", "fix bug", "refactor" | `modules/development-workflow.md` |
| **Verify** | 4 | "merge code", "submit code", "create PR" | `modules/code-merge.md` |
| **Maintain** | 5 | "handle debt", "cleanup", "optimize" | `modules/technical-debt.md` |
| **EnforceArchitecture** | - | "enforce architecture", "check architecture" | `modules/architecture-enforcement.md` |

## Examples

**Example 1: Start a new project**
```
User: "Initialize a new project with TypeScript and testing"
→ Invokes Initialize workflow
→ Sets up Git, CI/CD, Linter, Test Framework
→ Creates AGENTS.md and architecture.md
```

**Example 2: Implement a feature**
```
User: "Add user authentication to the app"
→ Invokes Develop workflow
→ Uses Reflexion Loop (Design → Code → Review → Test → Fix)
→ Maintains Clean State throughout
```

**Example 3: Fix a bug**
```
User: "Fix the login bug"
→ Invokes Develop workflow
→ Writes reproduction test first
→ Proves failure before fixing
```

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