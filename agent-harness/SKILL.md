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

2. **Output text notification**:
   ```
   Running the **WorkflowName** workflow in the **Harness** skill to ACTION...
   ```

**Full documentation:** `~/.claude/skills/PAI/THENOTIFICATIONSYSTEM.md`

## Workflow Routing

**When executing a workflow, also output this text:**

```
Running the **WorkflowName** workflow in the **Harness** skill to ACTION...
```

| Workflow | Trigger | File |
|----------|---------|------|
| **Initialize** | "start new project", "initialize project" | `modules/initialization.md` |
| **Develop** | "implement feature", "fix bug", "refactor" | `modules/development-workflow.md` |
| **PlanFeature** | "plan feature", "add feature" | `modules/feature-management.md` |
| **EnforceArchitecture** | "enforce architecture", "check architecture" | `modules/architecture-enforcement.md` |
| **MergeCode** | "merge code", "submit code", "create PR" | `modules/code-merge.md` |
| **HandleDebt** | "handle debt", "cleanup", "optimize" | `modules/technical-debt.md` |

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

## Quick Reference

**Core Philosophy:**
- **Design Environment**: Build scaffolding (CI, Lint, Directory Structure)
- **Clarify Intent**: Deconstruct requirements into unambiguous specs
- **Build Feedback Loop**: Use Reflexion Loop as Main Execution Engine

**Iron Laws:**
1. Clean State - Code must be runnable at end of each session
2. One Feature At A Time
3. Knowledge Must Be In Repository
4. Architecture Is Law
5. Observability First
6. Test-Driven Development
7. Choose Boring Technology

**Key Files:**
- Project Map: `AGENTS.md`
- Architecture: `architecture.md`
- Feature List: `feature_list.json`

**Full Documentation:**
- Initialization: `SkillSearch('harness initialization')` → modules/initialization.md
- Development: `SkillSearch('harness development')` → modules/development-workflow.md
- Feature Management: `SkillSearch('harness feature')` → modules/feature-management.md
- Architecture: `SkillSearch('harness architecture')` → modules/architecture-enforcement.md
- Code Merge: `SkillSearch('harness merge')` → modules/code-merge.md
- Technical Debt: `SkillSearch('harness debt')` → modules/technical-debt.md
