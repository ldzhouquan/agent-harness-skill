# Module 3: Feature Inventory Management

↩️ [返回概览](../SKILL.md) | [查看工作流](../workflow.md)

## JSON Format (Strong Structure)
- **Mandatory Field**: `verification_plan` (How will you verify this works?)
- Prevents hallucination by requiring upfront planning
- Example:
```json
{
  "features": [
    {
      "id": "feature-001",
      "description": "User login flow",
      "verification_plan": "E2E test simulating valid/invalid credentials",
      "pass": false
    }
  ]
}
```

## Default Failure Principle
- All features default to `false`
- **No Plan without Verification**: You cannot start work without a clear verification strategy
- Must execute verification plan successfully before flipping to `true`

## One Feature At A Time
- Select one feature -> Implement -> Verify -> Commit
- Ensure no cumulative errors between multiple sessions
