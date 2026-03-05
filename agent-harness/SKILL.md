---
name: harness
description: Use when initializing projects, enforcing architecture constraints, or managing long-running agent workflows. Implements Harness Engineering methodology for stable, verifiable development.
---

# Harness Engineering Skill

## Overview

Systematically implements the Harness Engineering methodology, enabling agents to work in a stable, controllable, and verifiable environment. Integrates Anthropic's long-running agent architecture, OpenAI's Harness Engineering methodology, and the concept of Agent Harness as the operating system for the AI era.

&lt;HARD-GATE&gt;
Before using this Skill, please ensure you have read and understood the docs/Harness Agent.md document.
&lt;/HARD-GATE&gt;

## Common Rationalizations & Reality Checks

| Excuse | Reality |
|--------|---------|
| "It's just a small fix, I'll skip the test" | Small fixes break big systems. Test first. |
| "I'll update the docs later" | Later never comes. Knowledge outside repo doesn't exist. |
| "This architecture is too rigid" | Constraints enable speed. Without guardrails, you crash. |
| "I can handle multiple features at once" | Context windows are finite. Serial execution prevents amnesia. |
| "Waiting for tests is slow" | Fixing bugs later is 10x slower. Cost function inversion applies. |

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

## Detailed Reference

**This skill uses progressive disclosure to save context.**

- **[Workflow & Checklists](workflow.md)**: Detailed execution phases, startup sequences, and checklists for every stage.
- **[Module Details & Templates](modules.md)**: Implementation details, file templates (like `.agent.md`), and specific strategies for each module.

## Key Constraints

### Unbreakable Iron Laws
1. **Clean State Principle Unbreakable** - code must be runnable at end of each session
2. **One Feature At A Time** - never allow handling multiple features simultaneously
3. **Knowledge Must Be In Repository** - important info must be written to files
4. **Architecture Is Law** - layering and Providers pattern must be enforced
5. **Build to Delete** - Harness code must be lightweight for easy refactoring

### When Should Stop and Ask
- Plan has critical gaps cannot start
- Don't understand an instruction
- Verification repeatedly fails
- Encountering situations involving directional choices

## Remember

- **Don't ask what agent can do for you, ask what you can provide for agent**
- **Give agent a map, not a manual**
- **Architecture is law, Linter is prompt, rules are multiplier**
- **Fixing cheap, waiting expensive**
- **Build to Delete - Harness is the data tent**
- **Discipline is shifting from code itself to engineering scaffolding**
- **Now most difficult challenges focus on designing environment, feedback loops, and control systems**
