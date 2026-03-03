# Discussion Logging: Capturing Agent Interactions

## Why Log Discussions?

Every meaningful interaction with the Code Agent - including requirements discussions, design decisions, and execution plans - must be captured in the harness knowledge base. This ensures:

1. **Knowledge Persistence**: Context isn't lost between sessions
2. **Decision Traceability**: Why we made certain choices
3. **Onboarding**: New agents can understand the project history
4. **Retrospective**: Learn from past decisions

## What to Log

### 1. Requirements Discussions
- User requirements and clarifications
- Trade-off analysis
- Priority decisions
- Scope boundaries

### 2. Design Discussions
- Architecture choices
- API design decisions
- Data model trade-offs
- Technology selection rationale

### 3. Execution Plans
- Feature implementation strategies
- Step-by-step action plans
- Risk assessments and mitigations
- Dependency management plans

## Discussion Log Structure

Create individual log files in `.harness/discussions/` directory.

### Naming Convention

```
YYYYMMDD-HHMM-topic-short-description.md
```

Example:
- `20240303-1430-user-authentication-requirements.md`
- `20240303-1645-database-schema-design.md`
- `20240303-1820-api-versioning-strategy.md`

### Log File Template

```markdown
# [Topic Title]

**Date**: YYYY-MM-DD HH:MM
**Participants**: [List of participants/agents involved]
**Type**: requirements | design | execution-plan

## Context
Brief context about what prompted this discussion.

## Discussion Summary
Key points from the conversation. Use bullet points for clarity.

## Decisions Made
- Decision 1: [What was decided]
  - Rationale: [Why this choice]
  - Alternatives considered: [Other options]

## Action Items
- [ ] Action 1 - [Owner] - [Deadline]
- [ ] Action 2 - [Owner] - [Deadline]

## Next Steps
What needs to happen next?

## References
- Related files: [file paths]
- Related discussions: [links to other logs]
- External resources: [links]
```

## Quick Logging Workflow

1. **During Discussion**: Keep notes in a temporary buffer
2. **After Discussion**: Create a log file in `.harness/discussions/`
3. **Commit**: Add and commit the log file with git
4. **Update Progress**: Reference the log in `.harness/progress.md`

## Index File

Maintain a `README.md` in `.harness/discussions/` that indexes all discussions:

```markdown
# Discussions Index

## Recent Discussions
- [2024-03-03 - API Versioning Strategy](20240303-1820-api-versioning-strategy.md)
- [2024-03-03 - Database Schema Design](20240303-1645-database-schema-design.md)

## By Category
### Requirements
- [User Authentication Requirements](20240303-1430-user-authentication-requirements.md)

### Design
- [Database Schema Design](20240303-1645-database-schema-design.md)
- [API Versioning Strategy](20240303-1820-api-versioning-strategy.md)
```

## Integration with Progress.md

When updating `.harness/progress.md`, reference relevant discussion logs:

```markdown
## 2024-03-03 Session

### Completed
- Finalized API versioning strategy [Discussion log](discussions/20240303-1820-api-versioning-strategy.md)
- Started database schema implementation

### Next
- Continue with database schema implementation
```

## Best Practices

1. **Log Early, Log Often**: Capture discussions while they're fresh
2. **Be Specific**: Include alternatives considered and rationale
3. **Link Liberally**: Connect to code, docs, and other discussions
4. **Keep Searchable**: Use consistent keywords in titles and tags
5. **Version Control**: Commit logs alongside code changes

## Tools

For quick logging, you can use:
- Simple text editor (vim, VS Code)
- The `log_discussion.py` helper script (if available)

Remember: **If it's not in the harness, it didn't happen for the next agent.**
