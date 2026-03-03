# Feature List JSON Schema

## Top-Level Structure

```json
{
  "project": "Project Name",
  "created": "2024-01-15T10:30:00",
  "agents": [...],
  "observability": {...},
  "features": [...]
}
```

## Feature Object

Each feature has these fields:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | Yes | Unique identifier for the feature |
| `category` | string | Yes | Category: "setup", "functional", "ui", "performance", "security", "observability", "testing" |
| `description` | string | Yes | Human-readable feature description |
| `priority` | string | Yes | Priority: "critical", "high", "medium", "low" |
| `depends_on` | array | No | Array of feature IDs that this feature depends on |
| `agent_role` | string | No | Agent role responsible: "implementer", "tester", "reviewer", "observer" |
| `steps` | array | Yes | Verification steps to confirm feature works |
| `tests` | object | No | Test requirements: unit, integration, e2e |
| `observability` | object | No | Observability requirements: metrics, logs, traces |
| `passes` | boolean | Yes | Whether feature has been tested and passes |
| `completed_at` | string | No | ISO timestamp when feature was completed |

## Categories

### setup
Project initialization and environment setup.

### functional
Core business logic and features.

### ui
User interface and visual elements.

### performance
Speed, loading times, optimization.

### security
Authentication, authorization, data protection.

### observability
Logging, metrics, tracing, and monitoring.

### testing
Test infrastructure, coverage, and quality gates.

## Agent Roles

### implementer
Responsible for writing production code.

### tester
Responsible for writing tests and verifying functionality.

### reviewer
Responsible for code review and quality assurance.

### observer
Responsible for observability, monitoring, and performance.

## Example Feature List

```json
{
  "project": "My Web App",
  "created": "2024-01-15T10:30:00",
  "agents": [
    {
      "role": "implementer",
      "description": "Writes production code"
    },
    {
      "role": "tester",
      "description": "Writes and runs tests"
    },
    {
      "role": "observer",
      "description": "Sets up monitoring and observability"
    }
  ],
  "observability": {
    "metrics_enabled": true,
    "logging_enabled": true,
    "tracing_enabled": false
  },
  "features": [
    {
      "id": "setup-001",
      "category": "setup",
      "description": "Development server runs without errors",
      "priority": "critical",
      "agent_role": "implementer",
      "steps": [
        "Run npm install",
        "Run npm run dev",
        "Open http://localhost:3000",
        "Page loads without console errors"
      ],
      "passes": true,
      "completed_at": "2024-01-15T11:00:00"
    },
    {
      "id": "observability-001",
      "category": "observability",
      "description": "Structured logging setup",
      "priority": "high",
      "depends_on": ["setup-001"],
      "agent_role": "observer",
      "steps": [
        "Configure Winston logger",
        "Verify logs are written to files",
        "Check log format includes timestamps and levels"
      ],
      "observability": {
        "logs": ["application", "error", "access"]
      },
      "passes": false
    },
    {
      "id": "functional-001",
      "category": "functional",
      "description": "User can create a new chat conversation",
      "priority": "high",
      "depends_on": ["setup-001"],
      "agent_role": "implementer",
      "steps": [
        "Navigate to main interface",
        "Click the 'New Chat' button",
        "Verify a new conversation is created",
        "Check that chat area shows welcome state",
        "Verify conversation appears in sidebar"
      ],
      "tests": {
        "unit": true,
        "integration": true,
        "e2e": true
      },
      "passes": false
    },
    {
      "id": "ui-001",
      "category": "ui",
      "description": "Dark mode toggle works correctly",
      "priority": "medium",
      "depends_on": ["setup-001"],
      "agent_role": "implementer",
      "steps": [
        "Click dark mode toggle",
        "Background changes to dark color",
        "Text remains readable",
        "Toggle persists after page reload"
      ],
      "tests": {
        "e2e": true
      },
      "passes": false
    }
  ]
}
```

## Best Practices

1. **Start with failing features** - Set all `passes` to `false` initially
2. **Only edit passes and completed_at fields** - Coding agents should only modify these fields
3. **Detailed steps** - Include specific verification steps for each feature
4. **Use dependencies** - Set `depends_on` to ensure features are built in the right order
5. **Prioritize rigorously** - Use "critical" for must-have features, "high" for important, etc.
6. **Assign agent roles** - Use `agent_role` to clarify which agent should work on what
7. **Include observability** - Add logging, metrics, and tracing requirements for production readiness
8. **Specify test coverage** - Define which types of tests are required for each feature
9. **JSON over Markdown** - JSON is less likely to be accidentally modified by AI
10. **Track completion time** - Set `completed_at` when a feature is marked as passing
