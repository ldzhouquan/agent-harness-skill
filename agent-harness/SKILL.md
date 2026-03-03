---
name: agent-harness
description: "Setup and run AI coding agents across multiple sessions with persistent progress tracking, based on OpenAI's Harness Engineering and Anthropic's long-running agent methodology. Use when: (1) Setting up a new project harness with feature list, progress file, and init script, (2) Continuing work as a coding agent that must resume from where a previous session left off, (3) Managing long-running agent tasks with structured knowledge base and observability."
---

# Agent Harness - Harness Engineering Methodology

## Overview

This skill enables AI coding agents to work effectively across multiple sessions with persistent state, following:
- **OpenAI's Harness Engineering principles** - Methodology to leverage AI agents across the entire SDLC
- **Anthropic's long-running agent architecture** - Single agent, serial execution with external memory

## Critical First Step: Read .harness/project.md

**ALWAYS START BY READING `.harness/project.md`** - it's your map to the knowledge base.

> This is a map, not the territory. Keep it small (~100 lines), use it to navigate to deeper docs.

## Knowledge Base Structure

The project uses **progressive disclosure** - start with `.harness/project.md`, then go deeper. All harness files are organized in the `.harness/` directory:

```
.
├── .harness/              # All harness files live here
│   ├── project.md         # THE MAP - Start here!
│   ├── docs/              # Documentation
│   │   ├── architecture/  # Layered architecture, providers pattern
│   │   ├── design/        # Workflows, getting started
│   │   ├── principles/    # Core beliefs, golden rules
│   │   └── tools/         # Linters, observability, testing
│   ├── discussions/       # Agent interaction logs (requirements, design, plans)
│   ├── decisions/         # Architecture Decision Records (ADRs)
│   ├── problems/          # Problem tracking & debugging logs
│   ├── experiments/       # Technical experiments & spikes
│   ├── retrospectives/    # Retrospectives & lessons learned
│   ├── features.json      # Feature tracking (ALL START AS FALSE!)
│   ├── progress.md        # Session progress log
│   └── init.sh            # Development server startup
```

## Harness Engineering Core Principles

### From OpenAI & Anthropic:

1. **Single Agent, Serial Execution**: One brain at a time to avoid decision conflicts
2. **Memory Lives Outside**: Use files, git, logs - never trust context window alone
3. **Default Failure**: All features start as `passes: false`
4. **One Feature at a Time**: No multitasking
5. **Clean State is Mandatory**: Never leave broken code for next session
6. **Observability First-Class**: Give agents eyes (UI) and stethoscope (logs/metrics)
7. **JSON > Markdown**: For structured data - models break Markdown structure
8. **Build to Delete**: Harness code will be obsolete - keep it lightweight
9. **Cost Inversion**: High-throughput = minimize blocking gates
10. **Knowledge in the Repo**: If it's not versioned, it doesn't exist
11. **Discussions Must Be Logged**: All requirements, design, and execution plans go to `.harness/discussions/`

## Quick Start

### Setting Up a New Project

1. **Read the Getting Started Guide**: `docs/design/getting-started.md`

2. **Run the setup script**:
```bash
python3 scripts/setup_harness.py --project-name "My Project" --project-type web
```

This creates:
- `.harness/` directory containing all harness files
- `.harness/features.json` - Feature list with pass/fail tracking (ALL START AS FALSE!)
- `.harness/progress.md` - Session progress log
- `.harness/init.sh` - Development server startup script
- `.harness/docs/` - Complete documentation directory

### Continuing Work (Coding Agent)

**MANDATORY: FOLLOW THIS EXACT SEQUENCE** (see `.harness/docs/design/session-startup.md`):

1. **Locate**: `pwd && ls -la` - Confirm environment
2. **Recall**: Read `git log --oneline -20` - Rebuild timeline
3. **Recall**: Read `.harness/project.md` - Project knowledge map
4. **Recall**: Read `.harness/progress.md` - Previous session summaries
5. **Recall**: Read `.harness/features.json` - Feature state
6. **Choose**: Filter for `passes: false` with all dependencies met, pick highest priority
7. **Reconstruct**: Run `.harness/init.sh` - Start dev server
8. **Verify**: Test baseline functionality works
9. **Begin**: Work on ONE feature

**For complete workflow details, see**:
- `.harness/docs/design/session-startup.md` - Session startup sequence
- `.harness/docs/design/feature-workflow.md` - How to implement one feature
- `.harness/docs/architecture/clean-state.md` - What clean state means

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

Update `.harness/progress.md` at the end of each session:

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
3. **Read project map**: `cat .harness/project.md`
4. **Read progress file**: `cat .harness/progress.md`
5. **Read feature list**: `cat .harness/features.json`
6. **Choose feature**: 
   - Filter for `passes: false`
   - Check that all `depends_on` features have `passes: true`
   - Select by priority: critical > high > medium > low
   - Check `agent_role` matches your current role
7. **Start dev server**: `.harness/init.sh`
8. **Verify baseline**: Run basic test to ensure app works
9. **Check observability**: Ensure logging/metrics are working if applicable

### During Session

1. Work on ONE feature at a time
2. Test incrementally - don't mark features as passing without verification
3. Use browser automation (Puppeteer MCP) for end-to-end testing
4. Write tests as specified in the `tests` field
5. Add observability as specified in the `observability` field
6. If you're the implementer, consider what the tester will need

### End of Session

1. Run tests to verify current feature works
2. Update `.harness/features.json` - set `passes: true` and `completed_at` only after actual testing
3. Update `.harness/progress.md` with session summary, including your agent role
4. Commit changes: `git add -A && git commit -m "Describe what was done"`
5. If handing off to another agent role, leave clear instructions

## Key Concepts Deep Dive

### Clean State

**THE IRON LAW**: You must leave the codebase in clean state before ending a session.

What clean state means:
- ✅ All tests pass
- ✅ No linter errors
- ✅ Dev server starts without errors
- ✅ App loads with no console errors
- ✅ `git status` shows no uncommitted changes
- ✅ `features.json` updated
- ✅ `progress.md` has session summary

**Full details**: `.harness/docs/architecture/clean-state.md`

---

### Golden Rules

Enforceable engineering standards (checked by linters):

1. **No Optimistic Data Access** - Validate external data at boundaries
2. **Prefer Shared Utilities** - No duplicate functions across modules
3. **External Data Validated** - All incoming data gets schema validation
4. **No Circular Dependencies** - Linter catches this
5. **Tests Are Part of Feature** - Feature not done without tests
6. **Structured Logs** - Logs for machines, comments for humans

**Full details**: `.harness/docs/principles/golden-rules.md`

---

### Architecture: Layered & Providers

**Layered Architecture** (unidirectional dependencies only):
1. Types → 2. Configuration → 3. Data Access → 4. Service → 5. Runtime → 6. Interface

**Providers Pattern**: Cross-cutting concerns (auth, logging, tracing) through single entry point.

**Full details**:
- `.harness/docs/architecture/layers.md` - Layer definitions
- `.harness/docs/architecture/providers.md` - Providers pattern

---

### Linters as Prompt Injectors

Linters don't just say "wrong"—they tell agents **how to fix it**:

```
❌ Layer violation: service/auth.ts importing from ui/Button.tsx
💡 Fix: Move shared logic to utils/ or create a service function
📚 Reference: .harness/docs/architecture/layers.md
```

**Full details**: `.harness/docs/tools/linters.md`

---

### Build to Delete

Your harness code will be obsolete in ~6 months. Design for disposal:
- Keep it lightweight
- Loose coupling like Lego bricks
- The real value is crash data, not the harness itself

**Full details**: `.harness/docs/principles/build-to-delete.md`

---

### Cost Inversion

In high-throughput agent environments:
- **Before**: Slow production → heavy review gates
- **After**: Fast production → minimal gates, fast feedback

Three adjustments:
1. Minimize blocking gates
2. Keep PRs short-lived
3. Don't let flaky tests block everything

**Full details**: `.harness/docs/principles/cost-inversion.md`

---

## Common Failure Modes & Harness Engineering Solutions

| Problem | Solution | Reference |
|---------|----------|-----------|
| Agent one-shots the app | One feature at a time | `.harness/docs/design/feature-workflow.md` |
| Agent declares victory too early | Default failure, require testing | `.harness/docs/principles/core.md` |
| Agent leaves environment broken | Clean state mandatory | `.harness/docs/architecture/clean-state.md` |
| Agent wastes time on setup | `.harness/init.sh` + session startup sequence | `.harness/docs/design/session-startup.md` |
| No observability | Give agents eyes & stethoscope | `.harness/docs/tools/observability.md` |
| Missing tests | Tests defined in feature schema | `.harness/docs/tools/testing.md` |
| Features built out of order | Use `depends_on` | `references/feature_schema.md` |
| Architecture drift | Layered architecture + linters | `.harness/docs/architecture/layers.md`, `.harness/docs/tools/linters.md` |
| Code duplication | Golden rules + shared utils | `.harness/docs/principles/golden-rules.md` |

## Scripts

- `scripts/setup_harness.py` - Initialize harness files for a new project
- `scripts/update_feature.py` - Update feature pass/fail status
- `scripts/log_discussion.py` - Create structured discussion log files

## Knowledge Capture System (MANDATORY!)

**ALL meaningful project knowledge MUST be logged in the harness!** This is a complete system for capturing every aspect of the project journey.

### The 5 Knowledge Capture Categories

| Category | Directory | Purpose | Guide |
|----------|-----------|---------|-------|
| **Discussions** | `.harness/discussions/` | Requirements, design talks, execution plans | [Guide](docs/design/discussion-logging.md) |
| **Decisions** | `.harness/decisions/` | Architecture Decision Records (ADRs) | [Guide](docs/design/decision-records.md) |
| **Problems** | `.harness/problems/` | Bugs, debugging, issue resolution | [Guide](docs/design/problem-tracking.md) |
| **Experiments** | `.harness/experiments/` | Technical spikes, feasibility tests | [Guide](docs/design/experiments.md) |
| **Retrospectives** | `.harness/retrospectives/` | Lessons learned, process improvement | [Guide](docs/design/retrospectives.md) |

### 1. Discussion Logs

Use for: Requirements, design conversations, execution plans

```bash
python scripts/log_discussion.py \
  --type design \
  --title "Database Schema Design" \
  --participants "Code Agent, User"
```

**When to use**: During conversations with the Code Agent

### 2. Architecture Decision Records (ADRs)

Use for: Important technical and architectural decisions

Create in `.harness/decisions/`:
- Naming: `adr-XXX-short-title.md`
- Use template in `.harness/docs/design/decision-records.md`

**When to use**: When making a decision that affects architecture, dependencies, or has long-term consequences

### 3. Problem Tracking

Use for: Bugs, errors, debugging sessions, environment issues

Create in `.harness/problems/`:
- Naming: `problem-XXX-short-description.md`
- Use template in `.harness/docs/design/problem-tracking.md`

**When to use**: When encountering and debugging any issue

### 4. Experiments & Spikes

Use for: Technology evaluation, feasibility testing, prototype validation

Create in `.harness/experiments/`:
- Naming: `experiment-XXX-short-description.md`
- Use template in `.harness/docs/design/experiments.md`

**When to use**: When trying new technologies, validating approaches, or testing assumptions

### 5. Retrospectives

Use for: Periodic review, lessons learned, process improvement

Create in `.harness/retrospectives/`:
- Naming: `retro-YYYYMMDD-type-description.md`
- Use templates in `.harness/docs/design/retrospectives.md`

**When to use**: End of sprint, after major milestones, weekly, or after significant learning

### How They Work Together

```
Discussion → (may lead to) → Experiment
                                    ↓
                            Decision (ADR)
                                    ↓
                            Implementation
                                    ↓
                            (may encounter) → Problem
                                    ↓
                            Retrospective (learn from all)
```

### General Workflow for All Log Types

1. **Create early**: Start the log when you begin the activity
2. **Be detailed**: Include context, alternatives, rationale
3. **Link everything**: Connect related logs together
4. **Commit with git**: Always version control your knowledge
5. **Update indexes**: Keep the README/index.md files current

### Why This Matters

- **Knowledge persistence**: Nothing gets lost between sessions
- **Full traceability**: Understand the complete story of every decision
- **Fast onboarding**: New agents can quickly get up to speed
- **Continuous improvement**: Learn from both successes and failures
- **Organizational memory**: Build a knowledge base that outlives any single session

**Remember: If it's not in the harness, it didn't happen for the next agent.**

**The Golden Rule: Log it ALL.**

## References

- `references/feature_schema.md` - Detailed feature list JSON schema
- `references/workflow.md` - Complete coding agent workflow guide
