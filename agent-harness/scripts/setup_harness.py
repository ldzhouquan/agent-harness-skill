#!/usr/bin/env python3
"""
Setup harness files for a new project.
Creates: .harness/ directory with all harness files
Based on OpenAI's Harness Engineering and Anthropic's long-running agent methodology
"""

import argparse
import json
import os
import shutil
from datetime import datetime

def create_project_md(project_name):
    """Create project.md - the knowledge map for agents."""
    return f"""# Agent Harness - {project_name}

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

- [Architecture Overview](docs/architecture/overview.md) - Document YOUR project architecture
- [Layered Architecture](docs/architecture/layers.md) - Define YOUR project layers
- [Providers Pattern](docs/architecture/providers.md) - Document YOUR cross-cutting concerns
- [Clean State](docs/architecture/clean-state.md) - Define YOUR clean state
- [Core Principles](docs/principles/core.md) - Define YOUR project principles
- [Golden Rules](docs/principles/golden-rules.md) - Define YOUR project rules
- [Build to Delete](docs/principles/build-to-delete.md) - YOUR build-to-delete strategy
- [Cost Inversion](docs/principles/cost-inversion.md) - YOUR cost inversion approach
- [Linters](docs/tools/linters.md) - Document YOUR linting setup
- [Observability](docs/tools/observability.md) - Document YOUR observability setup
- [Testing](docs/tools/testing.md) - Document YOUR testing setup

## Important Notes

- **This file is the map, not the territory** - Don't put everything here
- **Knowledge lives in the repo** - If it's not versioned, it doesn't exist for agents
- **Keep this small (~100 lines)** - It's a navigation aid, not an encyclopedia
- **JSON > Markdown** - For structured data like feature lists

---

*Remember: A good map gets you where you need to go without overwhelming you.*
"""

def create_features_json(project_name):
    """Create initial features.json with enhanced Harness Engineering structure."""
    features = {
        "project": project_name,
        "created": datetime.now().isoformat(),
        "agents": [
            {
                "role": "implementer",
                "description": "Writes production code"
            },
            {
                "role": "tester",
                "description": "Writes and runs tests"
            },
            {
                "role": "observer",
                "description": "Sets up monitoring and observability"
            }
        ],
        "observability": {
            "metrics_enabled": True,
            "logging_enabled": True,
            "tracing_enabled": False
        },
        "features": [
            {
                "id": "setup-001",
                "category": "setup",
                "description": "Project initialization and development environment",
                "priority": "critical",
                "agent_role": "implementer",
                "steps": [
                    "Install dependencies",
                    "Start development server",
                    "Verify app loads in browser"
                ],
                "passes": False
            },
            {
                "id": "observability-001",
                "category": "observability",
                "description": "Structured logging setup",
                "priority": "high",
                "depends_on": ["setup-001"],
                "agent_role": "observer",
                "steps": [
                    "Configure logger",
                    "Verify logs are written",
                    "Check log format includes timestamps and levels"
                ],
                "observability": {
                    "logs": ["application", "error"]
                },
                "passes": False
            },
            {
                "id": "testing-001",
                "category": "testing",
                "description": "Test infrastructure setup",
                "priority": "high",
                "depends_on": ["setup-001"],
                "agent_role": "tester",
                "steps": [
                    "Set up test framework",
                    "Verify test runner works",
                    "Create sample test that passes"
                ],
                "tests": {
                    "unit": True
                },
                "passes": False
            }
        ]
    }
    return features

def create_progress_md(project_name):
    """Create initial progress.md with agent role support."""
    return f"""# Progress: {project_name}

## Session 0 - {datetime.now().strftime('%Y-%m-%d')}

### Project Setup
- Harness initialized with Harness Engineering methodology
- All harness files organized in .harness/ directory
- Knowledge base created: docs/ directory with architecture, principles, and tools
- Single-agent, serial execution approach (per Anthropic recommendations)
- Waiting for first coding session

### Important Reminders
- ALWAYS start by reading .harness/project.md
- Follow the session startup sequence in docs/design/session-startup.md
- ONE FEATURE PER SESSION
- Leave in CLEAN STATE (see docs/architecture/clean-state.md)

### Next Session
- Read .harness/project.md first!
- Begin implementing features from .harness/features.json
- Start with setup-001 (critical priority)
"""

def create_init_sh(project_type):
    """Create init.sh based on project type."""
    if project_type == "web":
        return """#!/bin/bash
# Initialize and start development server

# Install dependencies (uncomment as needed)
# npm install

# Start development server
echo "Starting development server..."
npm run dev
"""
    elif project_type == "backend":
        return """#!/bin/bash
# Initialize and start backend server

# Install dependencies (uncomment as needed)
# pip install -r requirements.txt

# Start server
echo "Starting server..."
python main.py
"""
    else:
        return """#!/bin/bash
# Development server startup script
# Customize this for your project

echo "Starting development server..."
"""

def copy_skill_templates(harness_dir):
    """Copy guides, project docs templates, references, and scripts to the harness directory."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    skill_root = os.path.dirname(script_dir)
    
    copied = []
    
    guides_source = os.path.join(skill_root, 'docs')
    if os.path.exists(guides_source):
        guides_dest = os.path.join(harness_dir, 'guides')
        shutil.copytree(guides_source, guides_dest, dirs_exist_ok=True)
        
        project_templates_dir = os.path.join(guides_dest, 'project-templates')
        if os.path.exists(project_templates_dir):
            shutil.rmtree(project_templates_dir)
        
        print(f"Created: {guides_dest}/")
        copied.append('harness guides')
    
    project_templates_source = os.path.join(skill_root, 'docs', 'project-templates')
    if os.path.exists(project_templates_source):
        docs_dest = os.path.join(harness_dir, 'docs')
        shutil.copytree(project_templates_source, docs_dest, dirs_exist_ok=True)
        print(f"Created: {docs_dest}/")
        copied.append('project docs templates')
    
    refs_source = os.path.join(skill_root, 'references')
    if os.path.exists(refs_source):
        refs_dest = os.path.join(harness_dir, 'references')
        shutil.copytree(refs_source, refs_dest, dirs_exist_ok=True)
        print(f"Created: {refs_dest}/")
        copied.append('references')
    
    scripts_source = os.path.join(skill_root, 'scripts')
    if os.path.exists(scripts_source):
        scripts_dest = os.path.join(harness_dir, 'scripts')
        shutil.copytree(scripts_source, scripts_dest, dirs_exist_ok=True)
        
        setup_script = os.path.join(scripts_dest, 'setup_harness.py')
        if os.path.exists(setup_script):
            os.remove(setup_script)
        
        print(f"Created: {scripts_dest}/")
        copied.append('scripts')
    
    return copied

def main():
    parser = argparse.ArgumentParser(description='Setup agent harness files with Harness Engineering')
    parser.add_argument('--project-name', default='My Project', help='Project name')
    parser.add_argument('--project-type', default='web', choices=['web', 'backend', 'data'], help='Project type')
    parser.add_argument('--output-dir', default='.', help='Output directory')
    parser.add_argument('--skip-docs', action='store_true', help='Skip copying docs directory')
    args = parser.parse_args()

    harness_dir = os.path.join(args.output_dir, '.harness')
    os.makedirs(harness_dir, exist_ok=True)

    project_md = create_project_md(args.project_name)
    project_md_path = os.path.join(harness_dir, 'project.md')
    with open(project_md_path, 'w') as f:
        f.write(project_md)
    print(f"Created: {project_md_path}")

    features = create_features_json(args.project_name)
    features_path = os.path.join(harness_dir, 'features.json')
    with open(features_path, 'w') as f:
        json.dump(features, f, indent=2)
    print(f"Created: {features_path}")

    progress = create_progress_md(args.project_name)
    progress_path = os.path.join(harness_dir, 'progress.md')
    with open(progress_path, 'w') as f:
        f.write(progress)
    print(f"Created: {progress_path}")

    init_sh = create_init_sh(args.project_type)
    init_path = os.path.join(harness_dir, 'init.sh')
    with open(init_path, 'w') as f:
        f.write(init_sh)
    os.chmod(init_path, 0o755)
    print(f"Created: {init_path}")

    if not args.skip_docs:
        copy_skill_templates(harness_dir)
    
    discussions_dir = os.path.join(harness_dir, 'discussions')
    os.makedirs(discussions_dir, exist_ok=True)
    
    discussions_index = os.path.join(discussions_dir, 'README.md')
    with open(discussions_index, 'w') as f:
        f.write("""# Discussions Index

## Recent Discussions

## By Category
### Requirements

### Design

### Execution Plans
""")
    print(f"Created: {discussions_index}")
    
    decisions_dir = os.path.join(harness_dir, 'decisions')
    os.makedirs(decisions_dir, exist_ok=True)
    
    decisions_index = os.path.join(decisions_dir, 'index.md')
    with open(decisions_index, 'w') as f:
        f.write("""# Architecture Decision Records

## Active Decisions

## Deprecated/Superseded Decisions
""")
    print(f"Created: {decisions_index}")
    
    problems_dir = os.path.join(harness_dir, 'problems')
    os.makedirs(problems_dir, exist_ok=True)
    
    problems_index = os.path.join(problems_dir, 'index.md')
    with open(problems_index, 'w') as f:
        f.write("""# Problem Log Index

## Open Problems

## Resolved Problems

## Statistics
- Total problems: 0
- Resolved: 0
- Open: 0
""")
    print(f"Created: {problems_index}")
    
    experiments_dir = os.path.join(harness_dir, 'experiments')
    os.makedirs(experiments_dir, exist_ok=True)
    
    experiments_index = os.path.join(experiments_dir, 'index.md')
    with open(experiments_index, 'w') as f:
        f.write("""# Experiments Index

## Active

## Completed
### Adopted

### Rejected

### Needs More Testing

## Technology Radar
### Adopt

### Trial

### Assess

### Hold
""")
    print(f"Created: {experiments_index}")
    
    retrospectives_dir = os.path.join(harness_dir, 'retrospectives')
    os.makedirs(retrospectives_dir, exist_ok=True)
    
    retrospectives_index = os.path.join(retrospectives_dir, 'index.md')
    with open(retrospectives_index, 'w') as f:
        f.write("""# Retrospectives Index

## Key Learnings Quick Reference

### Technical

### Process

## Action Items Tracker
""")
    print(f"Created: {retrospectives_index}")

    print("\n" + "="*60)
    print("Harness setup complete! (Enhanced Edition)")
    print("="*60)
    print("\nNEXT STEPS:")
    print("1. Read .harness/project.md (CRITICAL FIRST STEP!)")
    print("2. Initialize git repo if not already done")
    print("3. Follow the session startup sequence in .harness/docs/design/session-startup.md")
    print("\nKEY REMINDERS:")
    print("- Single agent, serial execution (no parallel agents!)")
    print("- ONE FEATURE PER SESSION")
    print("- ALWAYS leave in CLEAN STATE")
    print("- Memory lives in files/git, not context window")
    print("\nFor complete documentation, see the .harness/docs/ directory!")

if __name__ == '__main__':
    main()
