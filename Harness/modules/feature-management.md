# Module 3: Feature Inventory Management

↩️ [返回概览](../SKILL.md) | [查看工作流](../workflow.md)

## JSON Format

**Mandatory Field**: `verification_plan` (How will you verify this works?)

Example:
```json
{
  "features": [
    {
      "id": "F1",
      "name": "User Login",
      "description": "User login with email/password",
      "verification_plan": "E2E test simulating valid/invalid credentials",
      "status": "pending",
      "pass": false,
      "started_at": "2026-03-13",
      "completed_at": null
    }
  ]
}
```

## Required Fields

| Field | Description |
|-------|-------------|
| `name` | Feature name |
| `description` | What the feature does |
| `verification_plan` | How to verify completion (REQUIRED) |
| `status` | pending / in_progress / completed / blocked |
| `pass` | false (until verified) |

## Status Values

| Status | Description |
|--------|-------------|
| `pending` | Not started |
| `in_progress` | Currently being developed |
| `completed` | Finished and verified |
| `blocked` | Waiting on external dependency |

## Default Failure Principle

- All features default to `pass: false`
- Cannot mark as complete without verification
- Must execute verification plan successfully before flipping to `true`

## One Feature At A Time

- Select one → Implement → Verify → Complete
- Never start new feature before current one is done
