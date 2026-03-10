# Module 7: End-to-End Autonomous Development

↩️ [返回概览](../SKILL.md) | [查看工作流](../workflow.md)

## When to Use Autonomous Development
**You can switch to fully autonomous mode ONLY when:**
1. **Spec is Unambiguous**: Requirements are crystal clear (e.g., fix a specific linter error, update a dependency).
2. **Verification is Automated**: CI/CD pipeline is fully functional and trusted.
3. **Scope is Contained**: Changes are limited to a single module or file.

**Trigger Scenarios:**
- **CI Failure Fix**: "Fix the build error in CI run #123."
- **Tech Debt Cleanup**: "Run the Document Gardener to fix broken links."
- **Refactoring**: "Extract this function into a utility class."

## The "Human-in-the-Loop" Boundary
**You MUST stop and ask for human intervention when:**
- **Ambiguity**: Requirements are unclear or contradictory.
- **High Risk**: Changes affect core architecture or security.
- **Verification Gap**: No automated tests exist for the changed code.
- **Loop Detection**: You find yourself in a retry loop (trying the same fix 3+ times).

## Closed-Loop Pipeline
1. Inspects codebase current state
2. Reproduces bugs (records video as evidence)
3. Completes code fix
4. Self-verifies (records successful run)
5. Opens PR
6. Handles review comments
7. Fixes build errors
8. Asks humans only for directional choices
9. Automatically merges code

## Crossing Autonomy Threshold
After testing, review, feedback handling are encoded into architecture, agent can operate end-to-end without human intervention.

## Sober Reminder
This behavior depends on specific codebase structure and toolchain. Higher autonomy requires more rigorous environment design.
