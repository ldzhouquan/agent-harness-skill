# Experiments & Technical Spikes

## Why Track Experiments?

Technical experiments and spikes help us:
- Evaluate technology choices
- Validate architectural approaches
- Test risky assumptions
- Learn new tools and patterns
- Make informed decisions

## What Qualifies as an Experiment?

Create an experiment log when you:
- Try a new library or framework
- Test different architecture patterns
- Explore performance optimizations
- Validate technical feasibility
- Compare multiple approaches

## Experiment Log Structure

```markdown
# Experiment-001: [Experiment Name]

**Date**: YYYY-MM-DD
**Experimenter**: [Who ran the experiment]
**Status**: [Planned | In Progress | Complete | Cancelled]
**Outcome**: [Adopted | Rejected | Needs More Testing]

## Hypothesis
What are we trying to prove or disprove?

> [Statement of what we believe will happen]

## Background
Why are we running this experiment? What's the context?

## Goals
- Goal 1: What we want to learn
- Goal 2: What we want to validate

## Methodology
How will we run the experiment?

### Setup
- Tools used:
- Environment:
- Test data:

### Test Cases
1. Test case 1
   - Expected result:
   - Actual result:

2. Test case 2
   - Expected result:
   - Actual result:

## Results
What happened? Be objective and data-driven.

### Quantitative Data
- Metric 1: X
- Metric 2: Y

### Qualitative Observations
- Observation 1
- Observation 2

## Analysis
What do the results mean?

### What Worked
- Success 1
- Success 2

### What Didn't Work
- Failure 1
- Failure 2

### Surprises
- Unexpected outcome 1
- Unexpected outcome 2

## Comparison to Alternatives
If comparing multiple approaches:

| Approach | Pros | Cons | Recommend |
|----------|------|------|-----------|
| Option A | ... | ... | ? |
| Option B | ... | ... | ? |

## Conclusion
Final outcome and recommendations.

### Recommendation
[ ] Adopt this approach
[ ] Reject this approach
[ ] Need more testing
[ ] Adopt with modifications (see below)

### Reasoning
Why did we reach this conclusion?

### Next Steps
- [ ] Step 1
- [ ] Step 2

## Artifacts
- Code: [Link to branch/commit]
- Demo: [Link to video/screenshot]
- Data: [Link to raw data]
- Notes: [Any additional files]

## Related
- Discussion log: [Link]
- Decision record: [Link if this led to an ADR]
- Previous experiments: [Links]
- References: [Links to docs/research]

## Timeline
- YYYY-MM-DD: Experiment created
- YYYY-MM-DD: Experiment started
- YYYY-MM-DD: Experiment completed
- YYYY-MM-DD: Results analyzed
```

## File Naming

```
experiment-XXX-short-description.md
```

Examples:
- `experiment-001-redis-vs-memcached.md`
- `experiment-002-react-vs-vue.md`
- `experiment-003-graphql-poc.md`

## Experiments Index

Maintain `index.md` in `.harness/experiments/`:

```markdown
# Experiments Index

## Active
- [Experiment-004: Caching Strategy](experiment-004-caching-strategy.md) - In Progress

## Completed
### Adopted
- [Experiment-002: React vs Vue](experiment-002-react-vs-vue.md) - Adopted React
- [Experiment-001: Redis Caching](experiment-001-redis-caching.md) - Adopted

### Rejected
- [Experiment-003: GraphQL POC](experiment-003-graphql-poc.md) - Rejected (too complex)

### Needs More Testing
- [Experiment-005: Microservices](experiment-005-microservices.md) - Needs scale testing

## Technology Radar
### Adopt
- React
- Redis

### Trial
- None currently

### Assess
- Microservices

### Hold
- GraphQL
```

## Experiment Best Practices

### Before the Experiment
- [ ] Write down your hypothesis first
- [ ] Define success metrics upfront
- [ ] Keep experiments small and focused
- [ ] Timebox the effort

### During the Experiment
- [ ] Take detailed notes
- [ ] Capture both quantitative and qualitative data
- [ ] Document what you learn as you go
- [ ] Don't be afraid to pivot or cancel

### After the Experiment
- [ ] Analyze results objectively
- [ ] Document conclusions clearly
- [ ] Make a decision (adopt/reject/more testing)
- [ ] Share learnings with the team

## Types of Experiments

### 1. Feasibility
Can we build this? Is it technically possible?

### 2. Comparison
Which option is better? A vs B vs C?

### 3. Performance
How fast is it? Does it scale?

### 4. Integration
Will it work with our existing stack?

### 5. Learning
How does this work? What are the patterns?

## Relationship to Other Logs

- **Discussion Logs**: Capture the conversation about what to experiment
- **Experiment Logs**: Capture the structured experiment and results
- **Decision Records**: Capture the final decision if the experiment leads to one
- **Problem Logs**: Reference if the experiment was trying to solve a problem

## Quick Experiment Template (Shorter Version)

For smaller spikes:

```markdown
# Quick Experiment: [Name]

**Date**: YYYY-MM-DD
**Status**: Complete
**Outcome**: Adopted

## What We Tried
[Brief description]

## What We Learned
- Point 1
- Point 2

## Recommendation
[Adopt/Reject] because...

## Code/Links
[References]
```

Use this for experiments that take < 1 day.
