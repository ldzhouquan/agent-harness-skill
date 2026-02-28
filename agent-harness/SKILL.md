---
name: agent-harness
description: "Setup and run AI coding agents across multiple sessions with persistent progress tracking, based on OpenAI's Harness Engineering methodology. Use when: (1) Setting up a new project harness with feature list, progress file, and init script, (2) Continuing work as a coding agent that must resume from where a previous session left off, (3) Managing long-running agent tasks that span hours or days with multi-agent collaboration."
---

# Agent Harness - Harness Engineering Methodology

## Overview

This skill enables AI coding agents to work effectively across multiple sessions with persistent state, following OpenAI's Harness Engineering principles - a methodology that leverages AI agents to drive the entire software development lifecycle. It provides two modes:

1. **Initializer Mode**: Sets up harness files for a new project
2. **Coding Agent Mode**: Resumes work following the harness workflow with specialized agent roles

## Harness Engineering Core Principles

Based on OpenAI's internal methodology:

1. **Multi-Agent Collaboration**: Specialized agents (implementer, tester, reviewer, observer) work together
2. **End-to-End Coverage**: From application logic to tests, CI, docs, observability, and internal tools
3. **Structured Observability**: Built-in logging, metrics, and tracing requirements
4. **Dependency-Aware Development**: Features are built in the right order with explicit dependencies
5. **Rigorous Testing**: Unit, integration, and E2E tests defined upfront
6. **Progress Persistence**: Clear state tracking across sessions

## Quick Start

### Setting Up a New Project

Run the setup script to create harness files:

```bash
python3 scripts/setup_harness.py --project-name "My Project" --project-type web
```

This creates:
- `features.json` - Feature list with pass/fail tracking, priorities, dependencies
- `progress.md` - Session progress log
- `init.sh` - Development server startup script

### Continuing Work (Coding Agent)

At the start of each session, the coding agent should:

1. Run `pwd` to see current directory
2. Read `git log --oneline -10` for recent history
3. Read `progress.md` for session summaries
4. Read `features.json` and choose the highest-priority incomplete feature whose dependencies are all met
5. Check the `agent_role` field to see if this feature is assigned to your role
6. Run `./init.sh` to start development server
7. Run basic end-to-end test to verify app works
8. Begin work on chosen feature

## Feature List Structure

The `features.json` file uses this enhanced JSON schema:

```json
{
  "project": "Project Name",
  "created": "2024-01-15T10:30:00",
  "agents": [...],
  "observability": {...},
  "features": [
    {
      "id": "feature-id",
      "category": "functional",
      "description": "Feature description",
      "priority": "high",
      "depends_on": ["other-feature-id"],
      "agent_role": "implementer",
      "steps": [
        "Step 1 to verify",
        "Step 2 to verify"
      ],
      "tests": {
        "unit": true,
        "integration": true,
        "e2e": false
      },
      "observability": {
        "logs": ["application"],
        "metrics": ["response_time"]
      },
      "passes": false
    }
  ]
}
```

Rules:
- Features start with `"passes": false`
- Only edit the `passes` and `completed_at` fields
- Use JSON (not Markdown) - models are less likely to accidentally modify it
- Always check `depends_on` to ensure prerequisites are met
- Respect the `agent_role` assignment

## Agent Roles

### Implementer
- Writes production code
- Focuses on functional requirements
- Follows dependency order

### Tester
- Writes comprehensive tests
- Verifies functionality works
- Ensures test coverage requirements are met

### Reviewer
- Reviews code quality
- Ensures best practices are followed
- Validates architectural decisions

### Observer
- Sets up logging, metrics, and tracing
- Monitors performance
- Ensures production readiness

## Progress File Format

Update `progress.md` at the end of each session:

```markdown
## Session 3 - 2024-01-15

### Agent Role: implementer

### Completed
- Implemented user login feature
- Added session persistence
- Marked feature `auth-001` as passing

### In Progress
- User profile page (80% done)

### Next Session
- Complete user profile page
- Add password reset flow
- Observer agent should set up logging for auth module

### Notes
- Found issue with token refresh, needs investigation
- All critical dependencies for `profile-001` are now met
```

## Coding Agent Session Workflow

### Start of Session

1. **Check environment**: `pwd && ls -la`
2. **Read git history**: `git log --oneline -10`
3. **Read progress file**: `cat progress.md`
4. **Read feature list**: `cat features.json`
5. **Choose feature**: 
   - Filter for `passes: false`
   - Check that all `depends_on` features have `passes: true`
   - Select by priority: critical > high > medium > low
   - Check `agent_role` matches your current role
6. **Start dev server**: `./init.sh`
7. **Verify baseline**: Run basic test to ensure app works
8. **Check observability**: Ensure logging/metrics are working if applicable

### During Session

1. Work on ONE feature at a time
2. Test incrementally - don't mark features as passing without verification
3. Use browser automation (Puppeteer MCP) for end-to-end testing
4. Write tests as specified in the `tests` field
5. Add observability as specified in the `observability` field
6. If you're the implementer, consider what the tester will need

### End of Session

1. Run tests to verify current feature works
2. Update `features.json` - set `passes: true` and `completed_at` only after actual testing
3. Update `progress.md` with session summary, including your agent role
4. Commit changes: `git add -A && git commit -m "Describe what was done"`
5. If handing off to another agent role, leave clear instructions

## Common Failure Modes & Harness Engineering Solutions

| Problem | Solution |
|---------|----------|
| Agent one-shots the app | Work on only one feature at a time, respect dependencies |
| Agent declares victory too early | Use feature list with all features initially failing, require testing |
| Agent leaves environment broken | Require git commits and progress file updates |
| Agent wastes time on setup | Use init.sh script for one-command startup |
| No observability in production | Use observer agent role and built-in observability requirements |
| Missing tests | Define test requirements upfront in feature schema |
| Features built out of order | Use `depends_on` to enforce correct build order |
| No role clarity | Use `agent_role` to specialize agents |

## Scripts

- `scripts/setup_harness.py` - Initialize harness files for a new project
- `scripts/update_feature.py` - Update feature pass/fail status

## References

- `references/feature_schema.md` - Detailed feature list JSON schema
- `references/workflow.md` - Complete coding agent workflow guide
