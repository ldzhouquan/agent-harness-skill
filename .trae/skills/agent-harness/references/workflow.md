# Coding Agent Workflow Guide - Harness Engineering Edition

This guide details how a coding agent should work within the harness framework, following OpenAI's Harness Engineering methodology.

## Session Start Checklist

Run these commands in order at the start of EVERY session:

```bash
# 1. Check where you are
pwd

# 2. See what files exist
ls -la

# 3. Check git history
git log --oneline -10

# 4. Read progress file
cat progress.md

# 5. Read feature list
cat features.json
```

## Choosing What to Work On

### Feature Selection Algorithm

1. Parse `features.json` to find all features where `passes: false`
2. For each candidate feature, verify ALL `depends_on` features have `passes: true`
3. Filter by `agent_role` - only work on features assigned to your role
4. Sort remaining features by priority:
   - critical (highest)
   - high
   - medium
   - low
5. Choose the highest-priority feature from the sorted list
6. Read the `steps` array to understand verification criteria
7. Read the `tests` object to understand test requirements
8. Read the `observability` object to understand monitoring requirements
9. Start working on that ONE feature

## Agent Role-Specific Workflows

### Implementer Agent Workflow

1. Focus on writing production code
2. Ensure feature meets functional requirements
3. Consider what the tester will need - make code testable
4. Think about observability - leave hooks for logging/metrics
5. Follow the verification `steps` as you build

### Tester Agent Workflow

1. Write tests as specified in the `tests` field
2. Unit tests: Test individual functions in isolation
3. Integration tests: Test how components work together
4. E2E tests: Test the complete user flow
5. Run all tests before marking feature as passing
6. Leave test coverage reports if possible

### Reviewer Agent Workflow

1. Review code for quality and best practices
2. Check architectural decisions
3. Verify security considerations
4. Ensure code is maintainable
5. Confirm tests are comprehensive

### Observer Agent Workflow

1. Set up logging as specified in `observability.logs`
2. Add metrics collection as specified in `observability.metrics`
3. Configure tracing if `observability.tracing_enabled` is true
4. Ensure logs are structured with timestamps and levels
5. Verify metrics are exported correctly
6. Set up basic dashboards or alerts if needed

## Starting the Development Server

```bash
./init.sh
```

If init.sh doesn't exist, create it based on your project type:

**Node/React:**
```bash
npm install
npm run dev
```

**Python:**
```bash
pip install -r requirements.txt
python main.py
```

## Verification Testing

Before marking a feature as passing, verify it actually works:

1. **Manual testing** - Use the app as a user would
2. **Browser automation** - Use Puppeteer MCP or similar
3. **API testing** - Use curl or HTTP client to test endpoints
4. **Run automated tests** - Execute unit, integration, and E2E tests
5. **Check observability** - Verify logs are being written, metrics are collected

### Anti-Pattern: Don't Trust Code Alone

❌ Bad: "The code looks correct, marking as passing"
✅ Good: "I'll test it in the browser first, run the tests, check the logs, then mark as passing"

Claude tends to mark features complete without proper testing. Use browser automation tools to actually verify features work.

## Session End Checklist

Before ending your session:

1. ✅ Feature is actually tested and works
2. ✅ All specified tests are written and passing
3. ✅ Observability requirements are met (if applicable)
4. ✅ `features.json` updated with `passes: true` and `completed_at` (if applicable)
5. ✅ `progress.md` updated with session summary including your agent role
6. ✅ Git commit with descriptive message
7. ✅ If handing off to another role, leave clear instructions

### Progress File Update Template

```markdown
## Session N - YYYY-MM-DD

### Agent Role: [implementer|tester|reviewer|observer]

### Completed
- What you finished
- Which feature ID(s) you worked on
- Any tests written
- Any observability setup

### In Progress
- What you started but didn't finish

### Next Session
- What the next agent should do
- If switching roles, specify what the next role needs
- Any dependencies that are now unblocked

### Notes
- Any important context for next session
- Known issues or blockers
- Test results summary
```

### Git Commit Message Examples

❌ Bad: "Fixed stuff"
✅ Good: "Add user login flow with session persistence (feature auth-001)"
✅ Good: "Implement dark mode toggle with localStorage persistence (feature ui-001)"
✅ Good: "Fix: resolved token refresh issue in auth module"
✅ Good: "Add Winston logger setup for application logs (feature observability-001)"
✅ Good: "Add unit and integration tests for chat feature (feature functional-001)"

## Multi-Agent Collaboration Patterns

### Hand-off from Implementer to Tester

```
Implementer completes feature → Marks passes: true → Leaves note: 
"Tester, please write unit, integration, and E2E tests as specified in tests field"
```

### Hand-off from Tester to Reviewer

```
Tester completes tests → All tests pass → Leaves note:
"Reviewer, please review code quality and test coverage"
```

### Hand-off from Implementer to Observer

```
Implementer completes feature → Leaves note:
"Observer, please set up logging and metrics as specified in observability field"
```

## Common Pitfalls

### One-Shotting
Don't try to implement everything in one session. Work on ONE feature.

### Premature Victory
Don't mark features as passing without testing. The next agent should be able to trust the feature list.

### Ignoring Dependencies
Always check that all `depends_on` features are passing before starting work.

### Role Confusion
Stick to your `agent_role`. Don't do work assigned to other roles unless explicitly asked.

### Skipping Observability
For production-ready code, observability is not optional. Make sure logging and metrics are in place.

### Leaving Broken State
Always test before ending session. Don't leave the app in a broken state.

### Wasting Time on Setup
Use init.sh. Don't spend time each session figuring out how to run the app.

## Dependency Graph Visualization (Conceptual)

When working on features, visualize the dependency tree:

```
setup-001 (critical, passes: true)
├── observability-001 (high, passes: false) [depends_on: setup-001]
├── functional-001 (high, passes: false) [depends_on: setup-001]
│   └── functional-002 (medium, passes: false) [depends_on: functional-001]
└── ui-001 (medium, passes: false) [depends_on: setup-001]
```

In this example:
- setup-001 is complete
- Next highest priority is observability-001 or functional-001 (both high priority)
- functional-002 cannot start until functional-001 is complete
