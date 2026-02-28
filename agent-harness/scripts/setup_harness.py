#!/usr/bin/env python3
"""
Setup harness files for a new project.
Creates: features.json, progress.md, init.sh
Based on OpenAI's Harness Engineering methodology
"""

import argparse
import json
import os
from datetime import datetime

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
- Multi-agent roles configured: implementer, tester, observer
- Waiting for first coding session

### Next Session
- Begin implementing features from features.json
- Start with setup-001 (critical priority) as implementer
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

def main():
    parser = argparse.ArgumentParser(description='Setup agent harness files with Harness Engineering')
    parser.add_argument('--project-name', default='My Project', help='Project name')
    parser.add_argument('--project-type', default='web', choices=['web', 'backend', 'data'], help='Project type')
    parser.add_argument('--output-dir', default='.', help='Output directory')
    args = parser.parse_args()

    features = create_features_json(args.project_name)
    features_path = os.path.join(args.output_dir, 'features.json')
    with open(features_path, 'w') as f:
        json.dump(features, f, indent=2)
    print(f"Created: {features_path}")

    progress = create_progress_md(args.project_name)
    progress_path = os.path.join(args.output_dir, 'progress.md')
    with open(progress_path, 'w') as f:
        f.write(progress)
    print(f"Created: {progress_path}")

    init_sh = create_init_sh(args.project_type)
    init_path = os.path.join(args.output_dir, 'init.sh')
    with open(init_path, 'w') as f:
        f.write(init_sh)
    os.chmod(init_path, 0o755)
    print(f"Created: {init_path}")

    print("\nHarness setup complete! (Harness Engineering Edition)")
    print("Next: Initialize git repo if not already done, then start coding.")
    print("Remember: Follow the multi-agent workflow and respect feature dependencies!")

if __name__ == '__main__':
    main()
