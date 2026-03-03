# Agent Harness - Agent Harness Skill

Welcome! This file is your map to the knowledge base.

## Quick Start

First time here? Start by exploring the harness structure below.

## Project Structure

```
.
├── .harness/              # All harness files live here
│   ├── project.md         # You are here - the map
│   ├── docs/              # YOUR PROJECT DOCUMENTATION (edit these!)
│   │   ├── architecture/  # Project architecture docs
│   │   ├── principles/    # Project principles and standards
│   │   └── tools/         # Project tools and setup
│   ├── guides/            # HOW TO USE THE HARNESS (read these!)
│   │   ├── architecture/  # Harness architecture principles
│   │   ├── design/        # Workflows, capture guides
│   │   ├── principles/    # Harness core principles
│   │   └── tools/         # Harness tool guides
│   ├── references/        # Harness reference materials
│   ├── scripts/           # Helper scripts (run these!)
│   ├── discussions/       # Agent interaction logs (requirements, design, plans)
│   ├── decisions/         # Architecture Decision Records (ADRs)
│   ├── problems/          # Problem tracking & debugging logs
│   ├── experiments/       # Technical experiments & spikes
│   ├── retrospectives/    # Retrospectives & lessons learned
│   ├── features.json      # Feature tracking (ALL START AS FALSE!)
│   ├── progress.md        # Session progress log
│   └── init.sh            # Development server startup
```

## Harness Usage Guides (Read These!)

Learn how to use the harness effectively:

- [Getting Started](guides/design/getting-started.md) - First steps with the harness
- [Session Startup](guides/design/session-startup.md) - Standard session startup sequence
- [Feature Workflow](guides/design/feature-workflow.md) - How to implement features
- [Quick Capture Workflow](guides/design/capture-workflow.md) - Capture brainstorming from ANY skill ⭐
- [Git Hygiene](guides/design/git-hygiene.md) - Commit and merge practices
- [Architecture Overview](guides/architecture/overview.md) - Harness architecture principles
- [Core Principles](guides/principles/core.md) - Harness engineering principles
- [Golden Rules](guides/principles/golden-rules.md) - Enforceable engineering standards
- [Clean State](guides/architecture/clean-state.md) - What "done" means
- [Layers](guides/architecture/layers.md) - Layered architecture guide
- [Providers](guides/architecture/providers.md) - Cross-cutting concerns pattern
- [Build to Delete](guides/principles/build-to-delete.md) - Harness evolution strategy
- [Cost Inversion](guides/principles/cost-inversion.md) - Throughput-driven engineering
- [Linters](guides/tools/linters.md) - Lint rules with auto-fix prompts
- [Observability](guides/tools/observability.md) - Logs, metrics, and tracing
- [Testing](guides/tools/testing.md) - Testing requirements and practices

## Reference Materials

- [Feature Schema](references/feature_schema.md) - JSON schema for features.json
- [Workflow Guide](references/workflow.md) - Complete coding agent workflow
- [Superpowers Skills](references/superpowers/) - Proven TDD, debugging, and planning workflows

## Helper Scripts

- [update_feature.py](scripts/update_feature.py) - Update feature pass/fail status
- [log_discussion.py](scripts/log_discussion.py) - Create structured discussion logs
- [capture_discussion.py](scripts/capture_discussion.py) - Quick capture for brainstorm sessions ⭐

## Knowledge Capture & Logging

Use these directories to capture project knowledge:

- [Discussions Index](discussions/README.md) - Browse all recorded discussions
- [Discussion Logging Guide](guides/design/discussion-logging.md) - How to log agent interactions
- [Decisions Index](decisions/README.md) - Architecture Decision Records (ADRs)
- [Decision Records Guide](guides/design/decision-records.md) - How to document technical decisions
- [Problems Index](problems/README.md) - Bug tracking and debugging logs
- [Problem Tracking Guide](guides/design/problem-tracking.md) - How to track issues and solutions
- [Experiments Index](experiments/README.md) - Technical experiments and spikes
- [Experiments Guide](guides/design/experiments.md) - How to run and document experiments
- [Retrospectives Index](retrospectives/README.md) - Lessons learned and retrospectives
- [Retrospectives Guide](guides/design/retrospectives.md) - How to run retrospectives

**IMPORTANT**: All requirements, design, decisions, problems, and experiments MUST be logged!

## Project Documentation (Edit These!)

The `docs/` directory contains templates for YOUR project documentation. Edit these to describe YOUR project!

- [Project Architecture](docs/architecture/overview.md) - Document YOUR project architecture
- [Project Principles](docs/principles/core.md) - Define YOUR project principles
- [Tools & Setup](docs/tools/setup.md) - Document YOUR tools and setup

## Important Notes

- **This file is the map, not the territory** - Don't put everything here
- **Knowledge lives in the repo** - If it's not versioned, it doesn't exist for agents
- **Keep this small (~100 lines)** - It's a navigation aid, not an encyclopedia
- **JSON > Markdown** - For structured data like feature lists

---

*Remember: A good map gets you where you need to go without overwhelming you.*
