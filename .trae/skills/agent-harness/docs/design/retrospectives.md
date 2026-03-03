# Retrospectives & Lessons Learned

## Why Retrospectives?

Regular retrospectives turn experience into knowledge. They help us:
- Celebrate wins
- Identify areas for improvement
- Share learnings across the team/project
- Refine our processes and practices

## When to Retrospect

- **End of Sprint/Milestone**: After completing a set of features
- **Post-Mortem**: After a major incident or outage
- **End of Session**: After a significant coding session
- **Weekly**: Regular cadence for continuous improvement
- **Ad-hoc**: After learning something important

## Retrospective Structure

### Quick Session Retrospective (15-30 mins)

```markdown
# Retrospective: [Session/Milestone Name]

**Date**: YYYY-MM-DD
**Participants**: [List]
**Duration**: [e.g., 1 week, 2 days]

## What Went Well
- Win 1
- Win 2
- What made these successful?

## What Could Be Better
- Challenge 1
- Challenge 2
- Why were these difficult?

## Action Items
- [ ] Action 1 - [Owner]
- [ ] Action 2 - [Owner]

## Key Metrics
- Features completed: X/Y
- Bugs found: X
- Time spent: X hours
```

### Detailed Project Retrospective

```markdown
# Project Retrospective: [Phase Name]

**Date**: YYYY-MM-DD
**Timeframe**: YYYY-MM-DD to YYYY-MM-DD

## Executive Summary
Brief overview of the period.

## Achievements
What did we accomplish?

### Features Delivered
- Feature 1
- Feature 2

### Technical Wins
- Technical achievement 1
- Technical achievement 2

## Challenges Encountered
What slowed us down?

### Technical Challenges
- Challenge 1
  - Impact:
  - Mitigation:

### Process Challenges
- Challenge 1
  - Impact:
  - Mitigation:

## Lessons Learned

### Technical Lessons
- Lesson 1: [What we learned]
  - How we'll apply it:

- Lesson 2: [What we learned]
  - How we'll apply it:

### Process Lessons
- Lesson 1: [What we learned]
  - How we'll apply it:

## What We'll Keep Doing
- Practice 1
- Practice 2

## What We'll Start Doing
- New practice 1
- New practice 2

## What We'll Stop Doing
- Practice to stop 1
- Practice to stop 2

## Goals for Next Period
- Goal 1
- Goal 2

## Metrics
| Metric | This Period | Previous Period | Change |
|--------|-------------|-----------------|--------|
| Metric 1 | X | Y | ±Z% |
| Metric 2 | X | Y | ±Z% |

## Action Plan
| Action | Owner | Due Date | Status |
|--------|-------|----------|--------|
| Action 1 | Person | YYYY-MM-DD | Not Started |

## Related Links
- Problem logs: [Links]
- Decision records: [Links]
- Discussion logs: [Links]
- Git commits: [Range]
```

## File Naming & Organization

```
.harness/retrospectives/
├── index.md
├── 2024/
│   ├── 03/
│   │   ├── retro-20240303-session-1.md
│   │   ├── retro-20240310-weekly.md
│   │   └── retro-20240331-milestone-1.md
│   └── 04/
└── templates/
    ├── session-retro.md
    └── project-retro.md
```

Naming pattern: `retro-YYYYMMDD-type-description.md`

Examples:
- `retro-20240303-session-auth-feature.md`
- `retro-20240310-weekly.md`
- `retro-20240331-milestone-v1.md`

## Retrospective Index

Maintain `index.md` in `.harness/retrospectives/`:

```markdown
# Retrospectives Index

## 2024
### March
- [2024-03-31 - Milestone 1](2024/03/retro-20240331-milestone-1.md)
- [2024-03-10 - Weekly](2024/03/retro-20240310-weekly.md)
- [2024-03-03 - Session: Auth Feature](2024/03/retro-20240303-session-auth-feature.md)

## Key Learnings Quick Reference

### Technical
- Always add logging before debugging
- Database migrations need rollback plans

### Process
- Test early, test often
- Smaller PRs review faster

## Action Items Tracker
- [ ] Set up automated tests - Due 2024-03-15
- [x] Add monitoring - Completed 2024-03-05
```

## The 4 Key Retrospective Questions

1. **What did we do well?** (Celebrate!)
2. **What did we learn?** (Knowledge!)
3. **What can we improve?** (Growth!)
4. **What still puzzles us?** (Curiosity!)

## Tips for Effective Retrospectives

- **Be honest but constructive** - Focus on improvement, not blame
- **Use data** - Reference metrics, logs, and actual events
- **Include everyone** - Capture all perspectives
- **Follow up** - Action items need owners and deadlines
- **Keep it focused** - Don't try to solve everything at once
- **Make it regular** - Consistency matters more than perfection

## Integration with Other Logs

Retrospectives should reference:
- **Discussion Logs**: What we talked about
- **Decision Records**: What we decided
- **Problem Logs**: What went wrong
- **Git History**: What we built
- **Progress Log**: What we accomplished

## Example: The "Five Whys"

For root cause analysis in retrospectives:

1. Why did the problem happen?
2. Why did that cause the problem?
3. Why was that possible?
4. Why didn't we catch it?
5. Why won't it happen again?

Answer each with data, not guesses!
