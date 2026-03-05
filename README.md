# Harness Engineering Skill

A systematic implementation of the Harness Engineering methodology, enabling AI agents to work in a stable, controllable, and verifiable environment. Integrates Anthropic's long-running agent architecture, OpenAI's Harness Engineering methodology, and the concept of Agent Harness as the operating system for the AI era.

## Overview

The Harness Engineering Skill provides a complete framework for building AI-powered applications with discipline, stability, and verifiability. It shifts the focus from writing code directly to designing the environment, feedback loops, and control systems that enable agents to work effectively.

## Core Principles

### 1. Single Agent Serial Architecture
- Avoid multi-agent decision conflicts
- Same brain in different modes: initializer agent vs coding agent
- Only serial guarantees clean state handoffs

### 2. External Memory System
- Rely on filesystem, logs, and Git history instead of internal memory
- Transfer work via structured files, eliminate amnesia risk
- Persistent logs and Git history make new sessions independent

### 3. Clean State
- Code must be runnable, docs updated at end of each session
- Meet main branch merge standards
- Never leave broken code for next shift
- Git rollback mechanism for stability

### 4. Structured Knowledge Base
- Use `.agent.md` as map (table of contents), not manual
- Use `docs/` directory for detailed knowledge
- Progressive information disclosure
- Knowledge must be in repository - if not, it doesn't exist

### 5. Architecture is Law
- Enforce invariants, don't micromanage implementation
- Layered architecture: code can only depend forward, never backward
- Providers pattern: all public capabilities through unified entry
- Linter as prompts: custom linters provide fix instructions

### 6. Cost Function Inversion
- In agent world: fixing is cheap, waiting is expensive
- Fast release, fast exposure, fast fix
- Minimize blocking gates, short PR lifecycle
- Never let flaky tests block progress indefinitely

### 7. Build to Delete
- Harness must be lightweight, like Lego bricks
- New models bring new agent construction approaches
- Harness is the data tent - capture crash trajectories as training data
- Don't resist refactoring and deletion, learn to cast monitoring net

## Project Structure

```
agent-harness/
├── SKILL.md              # Skill definition file
├── workflow.md           # Complete workflow & checklists
├── modules.md            # Core module index
└── modules/              # Detailed module documentation
    ├── initialization.md      # Project initialization templates
    ├── knowledge-base.md      # Knowledge base management
    ├── feature-management.md  # Feature inventory management
    ├── development-workflow.md # Incremental development
    ├── architecture-enforcement.md # Architecture constraints
    ├── code-merge.md          # Code merge strategy
    ├── autonomous-development.md # End-to-end autonomy
    └── technical-debt.md      # Technical debt handling
```

## 5-Phase Workflow

### Phase 1: Project Initialization (Initializer Agent)
Set up environment, create knowledge base structure, establish basic constraints.

**Key Files Created:**
- `.agent.md` - Project map (navigation entry)
- `architecture.md` - Architecture bird's eye view
- `feature_list.json` - Feature inventory (all pass: false)
- `progress.txt` - Progress log
- `docs/` directory structure

### Phase 2: Feature Planning
Create structured feature inventory, clarify all requirements.

### Phase 3: Incremental Development (Coding Agent)
One feature at a time, maintain Clean State.

**Startup Sequence (MUST execute EVERY session):**
1. **Locate** - Run `pwd` to confirm working directory
2. **Recall** - Read `progress.txt` and Git commit history
3. **Claim Task** - Read `feature_list.json`, find highest priority not yet passed
4. **Restore** - Run tests to verify basic functionality works
5. **Validate** - Confirm system health before starting new development work

### Phase 4: Verification & Merge
Test, review, merge, maintain high throughput.

### Phase 5: Continuous Maintenance
Continuously clean technical debt, maintain architectural coherence.

## Unbreakable Iron Laws

1. **Clean State Principle Unbreakable** - code must be runnable at end of each session
2. **One Feature At A Time** - never allow handling multiple features simultaneously
3. **Knowledge Must Be In Repository** - important info must be written to files
4. **Architecture Is Law** - layering and Providers pattern must be enforced
5. **Build to Delete** - Harness code must be lightweight for easy refactoring

## Common Rationalizations & Reality Checks

| Excuse | Reality |
|--------|---------|
| "It's just a small fix, I'll skip the test" | Small fixes break big systems. Test first. |
| "I'll update the docs later" | Later never comes. Knowledge outside repo doesn't exist. |
| "This architecture is too rigid" | Constraints enable speed. Without guardrails, you crash. |
| "I can handle multiple features at once" | Context windows are finite. Serial execution prevents amnesia. |
| "Waiting for tests is slow" | Fixing bugs later is 10x slower. Cost function inversion applies. |

## Quick Start

### Install the Skill

Install the skill into your Trae IDE or skill-supported environment:

1. Copy the `agent-harness/` directory to your skills directory
2. Or use the provided installation script

### Initialize a New Project

Follow the initialization checklist in [workflow.md](agent-harness/workflow.md):

1. Initialize Git repository
2. Create `.agent.md` using the template
3. Create `architecture.md`
4. Set up `docs/` directory structure
5. Create `feature_list.json`
6. Create `progress.txt`

## Key Documentation

- **[SKILL.md](agent-harness/SKILL.md)** - Skill definition and core principles
- **[workflow.md](agent-harness/workflow.md)** - Complete workflow and checklists
- **[modules.md](agent-harness/modules.md)** - Core module index
- **[modules/initialization.md](agent-harness/modules/initialization.md)** - Project initialization templates

## Remember

- **Don't ask what agent can do for you, ask what you can provide for agent**
- **Give agent a map, not a manual**
- **Architecture is law, Linter is prompt, rules are multiplier**
- **Fixing cheap, waiting expensive**
- **Build to Delete - Harness is the data tent**
- **Discipline is shifting from code itself to engineering scaffolding**
- **Now most difficult challenges focus on designing environment, feedback loops, and control systems**

## References

- [OpenAI Harness Engineering](https://openai.com/index/harness-engineering)
- [Anthropic Long-Running Agents](https://www.anthropic.com/index/long-running-agents)

## License

This project follows applicable open source licenses.
