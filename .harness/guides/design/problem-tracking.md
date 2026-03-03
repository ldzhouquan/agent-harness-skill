# Problem Tracking & Debugging Logs

## Why Track Problems?

Every bug, issue, and debugging session contains valuable learning. Capture these to:
- Avoid repeating the same mistakes
- Build a knowledge base of solutions
- Help future agents and team members
- Document system behavior and edge cases

## What to Track

### Bugs & Errors
- Runtime exceptions and stack traces
- Unexpected behavior
- Performance issues
- UI glitches

### Environment Issues
- Build failures
- Dependency conflicts
- Configuration problems
- Network issues

## Problem Log Structure

```markdown
# Problem-001: [Short Description]

**Date**: YYYY-MM-DD HH:MM
**Reported by**: [Who discovered the issue]
**Severity**: [Critical | High | Medium | Low]
**Status**: [Open | Investigating | Resolved | Closed]

## Symptom
What's wrong? What did you see?

- Error message: [Copy the exact error]
- Expected behavior: [What should happen]
- Actual behavior: [What actually happens]

## Environment
- OS: [e.g., macOS 14.3]
- Node/Python version: [e.g., Python 3.11]
- Relevant dependencies: [e.g., FastAPI 0.109.0]
- Git commit: [SHA]

## Reproduction Steps
1. Step 1
2. Step 2
3. Step 3

## Investigation
What did you try? What did you learn?

### Hypothesis 1
- What you thought
- How you tested it
- Result

### Hypothesis 2
- What you thought
- How you tested it
- Result

## Root Cause
What was the actual cause? Be specific!

## Solution
How did you fix it? Include code snippets if relevant.

```python
# Show the fix
```

## Prevention
How can we avoid this in the future?
- Tests to add
- Documentation to update
- Process changes

## Related
- Discussion log: [Link to discussion]
- Code changes: [Git commit SHA]
- Related problems: [Links]

## Lessons Learned
Key takeaways from this debugging session.
```

## File Naming

```
problem-XXX-short-description.md
```

Examples:
- `problem-001-db-connection-timeout.md`
- `problem-002-api-500-error.md`
- `problem-003-build-failure.md`

## Problem Index

Maintain `index.md` in `.harness/problems/`:

```markdown
# Problem Log Index

## Open Problems
- [Problem-004: Memory Leak](problem-004-memory-leak.md) - High - Investigating

## Resolved Problems
- [Problem-003: Build Failure](problem-003-build-failure.md) - Medium - 2024-03-03
- [Problem-002: API 500 Error](problem-002-api-500-error.md) - High - 2024-03-02
- [Problem-001: DB Timeout](problem-001-db-timeout.md) - Critical - 2024-03-01

## Statistics
- Total problems: 4
- Resolved: 3 (75%)
- Open: 1
```

## Quick Debugging Checklist

Before creating a problem log, ensure you have:

- [ ] Captured the exact error message
- [ ] Noted the environment details
- [ ] Written reproduction steps
- [ ] Checked git history for recent changes
- [ ] Looked at related logs
- [ ] Tried the simplest possible reproduction case

## Relationship to Other Logs

- **Discussion Logs**: Capture the conversation about the problem
- **Problem Logs**: Capture the structured debugging details and solution
- **Progress Log**: Reference problem logs when they're resolved

## Best Practices

- **Create early**: Log problems as soon as you start debugging
- **Be detailed**: Include all relevant context
- **Update status**: Keep the log current as you investigate
- **Include code**: Show the before/after of the fix
- **Link everything**: Connect to discussions, commits, and related issues
- **Focus on learning**: The "Lessons Learned" section is crucial!

## Search Tips

When looking for past problems:
- Search by error message text
- Look for similar symptoms
- Check related components
- Review "Lessons Learned" sections
