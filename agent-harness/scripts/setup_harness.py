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

First time here? Start with:
- [Architecture Overview](docs/architecture/overview.md) - Understand the big picture
- [Core Principles](docs/principles/core.md) - What we believe in
- [Getting Started](docs/design/getting-started.md) - First steps

## Project Structure

```
.
├── .harness/              # All harness files live here
│   ├── project.md         # You are here - the map
│   ├── docs/              # Documentation
│   ├── features.json      # Feature tracking (ALL START AS FALSE!)
│   ├── progress.md        # Session progress log
│   └── init.sh            # Development server startup
```

## Key Knowledge Areas

### Architecture
- [Layered Architecture](docs/architecture/layers.md) - How code should be structured
- [Providers Pattern](docs/architecture/providers.md) - Cross-cutting concerns
- [Clean State](docs/architecture/clean-state.md) - What "done" means

### Principles
- [Golden Rules](docs/principles/golden-rules.md) - Enforceable engineering standards
- [Build to Delete](docs/principles/build-to-delete.md) - Harness evolution strategy
- [Cost Inversion](docs/principles/cost-inversion.md) - Throughput-driven engineering

### Workflow
- [Session Startup](docs/design/session-startup.md) - Standard sequence for each session
- [Feature Workflow](docs/design/feature-workflow.md) - How to implement features
- [Git Hygiene](docs/design/git-hygiene.md) - Commit and merge practices

### Tools
- [Custom Linters](docs/tools/linters.md) - Lint rules with auto-fix prompts
- [Observability](docs/tools/observability.md) - Logs, metrics, and tracing
- [Testing](docs/tools/testing.md) - Testing requirements and practices

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

def copy_docs_directory(harness_dir):
    """Copy the docs directory template to the harness directory."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    skill_root = os.path.dirname(script_dir)
    docs_source = os.path.join(skill_root, 'docs')
    
    if os.path.exists(docs_source):
        docs_dest = os.path.join(harness_dir, 'docs')
        shutil.copytree(docs_source, docs_dest, dirs_exist_ok=True)
        print(f"Created: {docs_dest}/")
        return True
    return False

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
        copy_docs_directory(harness_dir)

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
