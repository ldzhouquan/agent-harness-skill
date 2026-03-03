# Discussion Capture Workflow: Record Every Brainstorm

## The Problem

When using other skills or tools for brainstorming, design sessions, or planning, the discussions and conclusions can get lost. This workflow ensures **nothing gets lost**.

## The Capture Workflow

### Phase 1: Before the Brainstorm (5 mins)

1. **Check if harness exists**
   ```bash
   ls -la .harness/
   ```
   If not, run: `python ~/.claude/skills/agent-harness/scripts/setup_harness.py`

2. **Prepare to capture**
   - Open the `.harness/discussions/` directory
   - Have `log_discussion.py` ready

### Phase 2: During the Brainstorm (Live Capture)

Use this **checklist** while brainstorming:

- [ ] Jot down key points in a temporary note
- [ ] Capture decisions as they're made
- [ ] Note alternatives that were considered
- [ ] Record rationale for choices
- [ ] Capture open questions and action items

**Quick capture template** (copy-paste into chat):
```
## Quick Notes
- [Key point 1]
- [Key point 2]

## Decisions So Far
- [Decision 1]

## Open Questions
- [Question 1]
```

### Phase 3: Immediately After (CRITICAL - 10 mins)

**DO THIS BEFORE DOING ANYTHING ELSE!**

#### Step 1: Create the discussion log
```bash
python ~/.claude/skills/agent-harness/scripts/log_discussion.py \
  --type [requirements|design|execution-plan] \
  --title "Short descriptive title" \
  --participants "Who was involved"
```

#### Step 2: Fill in the log
Open the created file and populate:
1. **Context**: What was this discussion about?
2. **Discussion Summary**: Key points from the conversation
3. **Decisions Made**: What was decided, why, alternatives
4. **Action Items**: What needs to happen next
5. **References**: Links to related files/discussions

#### Step 3: Commit it
```bash
git add .harness/discussions/YYYYMMDD-HHMM-*.md
git commit -m "Log discussion: [Title]"
```

#### Step 4: Update progress.md (optional but recommended)
Add a line in `.harness/progress.md` referencing the discussion log.

## The "5-Minute Rule"

**If a discussion is longer than 5 minutes, it MUST be logged.**

Exceptions:
- Trivial questions with 1-2 line answers
- Quick clarifications that don't change direction

## The Capture Trigger Questions

Ask yourself **these 3 questions** after any conversation:

1. **Would a new agent understand this decision without context?**
   - If NO → Log it!

2. **Are there alternatives we considered?**
   - If YES → Log them!

3. **Would we want to remember this in 3 months?**
   - If YES → Log it!

If you answered YES to any of the above → LOG IT!

## Integration with Other Skills

### When switching from another skill to Agent Harness

```
1. [Other Skill] Brainstorm complete
2. [Capture Workflow] Pause - time to log!
3. [Agent Harness] Run log_discussion.py
4. [Agent Harness] Fill in the log template
5. [Agent Harness] Commit to git
6. [Continue] Now proceed with implementation
```

### Prompt Template for Brainstorm Conclusion

Add this **prompt snippet** at the end of any brainstorm session:

```
---
## TIME TO CAPTURE THIS DISCUSSION!

Before we continue, let's record what we just discussed.

Please help me create a discussion log:

1. Summarize the key points from our conversation
2. List any decisions that were made (include rationale and alternatives)
3. Identify action items and next steps
4. Note any open questions

I will then use this to create a proper discussion log in the harness.
---
```

## Common Capture Scenarios

### Scenario 1: Requirements Discussion
**When**: Talking about what to build
**Log type**: `requirements`
**Key to capture**: User needs, constraints, priorities, scope boundaries

### Scenario 2: Design Brainstorm
**When**: Talking about how to build it
**Log type**: `design`
**Key to capture**: Architecture choices, trade-offs, API design, data models

### Scenario 3: Planning Session
**When**: Talking about the plan
**Log type**: `execution-plan`
**Key to capture**: Implementation steps, dependencies, risks, timeline

### Scenario 4: Technical Decision
**When**: Making an important technical choice
**Also create**: An ADR in `.harness/decisions/`
**Link**: Reference the ADR from the discussion log

## Capture Quality Checklist

A good discussion log has:

- [ ] **Context**: Why we had this discussion
- [ ] **Summary**: What was discussed
- [ ] **Decisions**: What was decided + rationale
- [ ] **Alternatives**: What else we considered
- [ ] **Actions**: What needs to happen next
- [ ] **Links**: Connections to related logs/files

## Anti-Patterns to Avoid

❌ **Too Late**: Waiting hours/days to log
❌ **Too Vague**: "We talked about stuff"
❌ **No Rationale**: Just stating decisions without why
❌ **No Alternatives**: Not mentioning what was rejected

✅ **Good**: Timely, detailed, complete, linked

## Tools & Shortcuts

### Quick Log Command (alias suggestion)
Add to your shell config:
```bash
alias log-discussion='python ~/.claude/skills/agent-harness/scripts/log_discussion.py'
```

### IDE Integration
- Create a keyboard shortcut to run `log_discussion.py`
- Keep the `.harness/discussions/` directory in your IDE sidebar

## Reminder

> **The Golden Rule of Capture**:
> 
> If you're wondering "should I log this?" → **YES, LOG IT**.
> 
> It's easier to delete an unnecessary log than to recreate a lost one.

**Remember: If it's not in the harness, it didn't happen for the next agent.**
