# Initialization Templates

Detailed templates for project initialization. See [../modules/initialization.md](../modules/initialization.md) for the workflow overview.

---

## AGENTS.md Template

Copy this content to create `AGENTS.md`:

```markdown
# Project Map

> This is a map, not a manual. Follow directions to find needed information.

## Project Overview
[Project name and brief description]

## Quick Navigation
- Architecture Overview: [docs/architecture.md](docs/architecture.md)
- Feature Inventory: [feature_list.json](feature_list.json)
- Progress Log: [progress.txt](progress.txt)
- Design Docs: [docs/designs/](docs/designs/)
- Execution Plans: [docs/plans/](docs/plans/)
- Core Principles: [docs/principles/](docs/principles/)
- Product Specs: [docs/specs/](docs/specs/)
- References: [docs/references/](docs/references/)
- Technical Debt: [docs/tech-debt/](docs/tech-debt/)
- Quality Scores: [docs/quality-scores/](docs/quality-scores/)

## Core Principles
1. Clean State - code must be runnable at end of each session
2. One Feature At A Time - select from feature inventory
3. Knowledge Must Be In Repository - if not in repo, doesn't exist
```

---

## architecture.md Template

Copy this content to create `docs/architecture.md`:

```markdown
# Architecture Bird's Eye View

## Business Domains
[List main business domains]

## Code Layering
- Types layer
- Config layer
- Data access layer
- Service layer
- Runtime layer
- Interface layer

**Rule:** Code can only depend forward, never backward.

## Module Relationships
[Describe relationships between modules]

## Providers Pattern
All public capabilities must enter through unified Providers entry:
- User authentication
- Logging
- Feature flags

**Prohibited:** Any other path is not allowed.
```

---

## Directory Structure

Create this structure in your project:

```
docs/
├── designs/           # Design docs (with validation status)
├── plans/             # Execution plans (in-progress/completed)
├── principles/        # Core beliefs
├── specs/             # Product specs
├── references/        # References
├── tech-debt/        # Technical debt tracking
└── quality-scores/   # Quality score docs
```

---

## feature_list.json Template

Create `feature_list.json`:

```json
{
  "features": []
}
```

---

## progress.txt Template

Create `progress.txt`:

```markdown
# Progress Log

[2026-03-16 10:30] Started working on Calculator feature
[2026-03-16 11:00] Decision: Use TDD approach
[2026-03-17 09:00] Completed Calculator - all tests passing
[2026-03-17 14:20] Blocked: Token refresh bug needs fix
```
