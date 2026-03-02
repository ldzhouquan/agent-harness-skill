# Agent Harness Skill

A framework for building AI agents based on OpenAI's Harness Engineering methodology and Anthropic's long-running agent architecture.

## Overview

Agent Harness Skill provides a complete set of tools and best practices for building efficient, maintainable, and observable AI-powered applications.

### Core Principles

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

## Project Structure

```
agent-harness-skill/
├── agent-harness/
│   ├── SKILL.md              # Skill definition file
│   ├── docs/                 # Documentation template
│   │   ├── architecture/     # Architecture docs
│   │   ├── design/           # Design docs
│   │   ├── principles/       # Core principles
│   │   └── tools/            # Tool docs
│   ├── scripts/              # Script tools
│   │   ├── setup_harness.py  # Project initialization script
│   │   └── update_feature.py # Feature status update script
│   ├── references/           # Reference materials
│   └── assets/               # Asset files
└── README.md                  # This file
```

## Initialized Project Structure

When you run the setup script, it creates:

```
your-project/
├── .harness/                 # All harness files organized here
│   ├── project.md           # Knowledge map (navigation entry)
│   ├── docs/                # Documentation
│   ├── features.json        # Feature tracking (ALL START AS FALSE!)
│   ├── progress.md          # Session progress log
│   └── init.sh              # Development server startup
```

## Quick Start

### Install the Skill

Install the `agent-harness.skill` file into your Claude Desktop or skill-supported IDE.

### Initialize a New Project

Run in your new project directory:

```bash
python setup_harness.py --project-name "My Awesome Project" --project-type web
```

This will create:
- `.harness/project.md` - Knowledge map
- `.harness/docs/` - Complete documentation directory
- `.harness/features.json` - Feature tracking manifest
- `.harness/progress.md` - Session progress log
- `.harness/init.sh` - Development server startup script

## Core Documentation

- [Architecture Overview](agent-harness/docs/architecture/overview.md) - Understand the big picture
- [Core Principles](agent-harness/docs/principles/core.md) - What we believe in
- [Getting Started](agent-harness/docs/design/getting-started.md) - First steps for a new project
- [Layered Architecture](agent-harness/docs/architecture/layers.md) - Code structure guidelines
- [Golden Rules](agent-harness/docs/principles/golden-rules.md) - Enforceable engineering standards

## Workflow

1. **Read the Knowledge Map** - Start every session by reading `.harness/project.md`
2. **Follow Session Startup Sequence** - Execute as per `.harness/docs/design/session-startup.md`
3. **One Feature at a Time** - Select the next feature from `.harness/features.json`
4. **Maintain Clean State** - Ensure code is runnable when finishing
5. **Record Progress** - Update `.harness/progress.md`

## Script Tools

### setup_harness.py

Initialize harness files for a new project.

```bash
python setup_harness.py [OPTIONS]

Options:
  --project-name TEXT    Project name
  --project-type TEXT    Project type [web|backend|data]
  --output-dir TEXT      Output directory
  --skip-docs            Skip copying docs directory
```

### update_feature.py

Update feature pass/fail status.

```bash
python update_feature.py [OPTIONS]

Options:
  --feature-index INTEGER  Feature index (0-based)
  --feature-id TEXT        Feature ID (alternative to index)
  --passes BOOLEAN         True or False
  --file TEXT              Features file path
```

## References

- [OpenAI Harness Engineering](https://openai.com/index/harness-engineering)
- [Anthropic Long-Running Agents](https://www.anthropic.com/index/long-running-agents)

## License

This project follows applicable open source licenses.
