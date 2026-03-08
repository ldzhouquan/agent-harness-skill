# Module 8: Technical Debt Handling

↩️ [返回概览](../SKILL.md) | [查看工作流](../workflow.md) | [模块索引](../modules.md)

## Golden Principles
1. **Prefer shared utility libraries** - prohibit handwritten utility functions in different modules
2. **Prohibit "happy path" style random probing** - must first do explicit structure validation for external data

## Continuous Small-Step Automatic Repayment
- Background regularly runs dedicated agent tasks
- Scans codebase for patterns deviating from golden principles
- Automatically generates targeted refactoring PRs (small scope, quick review)
- Like system-level garbage collection - continuous small-step automatic cleanup

**Technical debt more like usury:** If let it accumulate, growth rate will exceed your repayment ability.
