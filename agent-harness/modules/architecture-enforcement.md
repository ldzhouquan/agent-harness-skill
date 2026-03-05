# Module 5: Architecture Constraint Enforcement

## Layered Architecture
- Each business domain divided into fixed layers
- From types layer to config layer, to data access layer, to service layer, to runtime layer, finally to interface layer
- Code can only depend forward, never backward

**Why?**
- Reverse dependencies make changing one place affect many
- When 100 agents change code simultaneously, hidden connections quickly spiral out of control
- Essence of one-way dependency is controlling blast radius: changes only propagate forward, upstream never dragged down by downstream

## Providers Pattern
- All public capabilities must enter through unified Providers entry
- Like building access control system - regardless of delivery or AC repair, must swipe card through main door
- Any other path, prohibited! CI directly red lights

## Custom Linters
- Linters not just error reporting tools, they're context injection tools
- When Linter errors, error message directly includes remediation instructions
- Example: "Service layer cannot reference UI module, please move shared logic to utils directory"
- Agent reading this error equals reading a prompt, then refactors code themselves, re-runs Linter until all green
- No human intervention needed

**Not humans following rules, but rules guarding system.**
