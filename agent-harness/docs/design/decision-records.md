# Architecture Decision Records (ADR)

## What are ADRs?

Architecture Decision Records (ADRs) are documents that capture important architectural decisions made along with their context and consequences.

## When to Create an ADR

Create an ADR when you make a decision that:
- Affects the overall architecture
- Changes how components interact
- Introduces or removes dependencies
- Has long-term consequences
- Is not immediately obvious or reversible

## ADR Structure

```markdown
# ADR-001: [Short Title of Decision]

**Status**: [Proposed | Accepted | Deprecated | Superseded]
**Date**: YYYY-MM-DD
**Deciders**: [List of decision makers]

## Context
What is the issue that we're seeing that is motivating this decision or change?

## Decision
What is the change that we're proposing and/or doing?

## Rationale
Why did we choose this option? What were the key factors?

## Alternatives Considered
What other options did we consider? Why were they rejected?

## Consequences
What becomes easier or more difficult to do because of this change?
- Positive outcomes
- Negative outcomes
- Risks and mitigation

## Related Decisions
- ADR-000: [Previous decision this builds on]
- Links to other ADRs

## References
- Links to relevant docs, discussions, or external resources
```

## ADR File Naming

```
adr-XXX-short-title.md
```

Examples:
- `adr-001-database-selection.md`
- `adr-002-api-gateway.md`
- `adr-003-state-management.md`

## ADR Index

Maintain an `index.md` in `.harness/decisions/`:

```markdown
# Architecture Decision Records

## Active Decisions
- [ADR-001: Database Selection](adr-001-database-selection.md) - 2024-03-03
- [ADR-002: API Gateway](adr-002-api-gateway.md) - 2024-03-03

## Deprecated/Deprecated Decisions
- [ADR-000: Old Approach](adr-000-old-approach.md) - Superseded by ADR-001
```

## Workflow

1. **Create**: When making an important decision, create an ADR
2. **Review**: Get feedback from the team (if applicable)
3. **Accept**: Mark as Accepted when finalized
4. **Reference**: Link to ADRs from code comments and docs
5. **Deprecate**: When a decision is changed, mark old ADR as Superseded

## Relationship to Discussion Logs

- **Discussion Logs**: Capture the conversation and exploration
- **ADRs**: Capture the final decision and rationale

A discussion may lead to one or more ADRs. Link them!

## Best Practices

- Keep ADRs concise (1-2 pages max)
- Focus on "why" not just "what"
- Include pros and cons of all options
- Update status as decisions evolve
- ADRs are immutable - create new ones instead of changing old ones
