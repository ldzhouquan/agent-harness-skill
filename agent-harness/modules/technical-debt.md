# Module 8: Technical Debt Handling

## Golden Principles List
1. **Prefer shared utility libraries**
   - Prohibit handwritten utility functions in different modules
   - Centralize key logic management, avoid multiple implementation versions repeatedly copied by agents, gradually diverging

2. **Prohibit "happy path" style random probing**
   - When handling external data, must first do explicit structure validation
   - Or use internally encapsulated strongly typed SDK interfaces to uniformly get data
   - Cannot directly assume field must exist without validating structure

## Continuous Small-Step Automatic Repayment Mechanism
- Background regularly runs dedicated agent tasks
- Scans codebase for patterns deviating from golden principles
- Once it detects a problem, automatically generates targeted refactoring PRs
- These PRs often have a very small scope, can be quickly reviewed, or even automatically merged
- More like system-level garbage collection - not waiting for the system to lose control then doing painful large-scale refactoring, but continuous small-step automatic cleanup of structural drift

**Technical debt more like usury:** If let it accumulate, growth rate will exceed your repayment ability. Only sustainable way is to establish a continuous small-step automatic repayment mechanism.

## Core Conclusion
**Discipline is shifting from code itself to engineering scaffolding.**

Here "scaffolding" refers to: tools, execution environment, system abstractions, feedback loops, and entire underlying control system.

**Now most difficult challenges focus on designing environment, feedback loops, and control systems.** In new era, software engineering difficulty no longer lies in squeezing model code generation ability limit, but whether you can build a sufficiently robust control architecture.
