# Module 1: Project Initialization

↩️ [返回概览](../SKILL.md) | [查看工作流](../workflow.md) | [模块索引](../modules.md)

## 1. Create .agent.md Template
```markdown
# Agent Map

&gt; This is a map, not a manual. Follow directions to find needed information.

## Project Overview
[Project name and brief description]

## Quick Navigation
- Architecture Overview: [architecture.md](./architecture.md)
- Feature Inventory: [feature_list.json](./feature_list.json)
- Progress Log: [progress.txt](./progress.txt)
- Design Docs: [docs/designs/](./docs/designs/)
- Execution Plans: [docs/plans/](./docs/plans/)
- Core Principles: [docs/principles/](./docs/principles/)
- Product Specs: [docs/specs/](./docs/specs/)
- References: [docs/references/](./docs/references/)
- Technical Debt: [docs/tech-debt/](./docs/tech-debt/)
- Quality Scores: [docs/quality-scores/](./docs/quality-scores/)

## Core Principles
1. Clean State - code must be runnable at end of each session
2. One Feature At A Time - select from feature inventory
3. Knowledge Must Be In Repository - if not in repo, doesn't exist
```

## 2. Create architecture.md Template
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

## 3. Create docs/ Directory Structure
```
docs/
├── designs/           # Design docs (with validation status)
├── plans/             # Execution plans (in-progress/completed)
├── principles/        # Core beliefs
├── specs/             # Product specs
├── references/        # References
├── tech-debt/         # Technical debt tracking
└── quality-scores/    # Quality score docs
```

## 4. Scaffold Engineering Environment (Crucial)

**You MUST set up the automated machinery before writing code.**

### A. Setup Linter & Formatter
- **Action**: Create config files (`.eslintrc`, `checkstyle.xml`, `.pylintrc`).
- **Rule**: Enforce "Industry Standard" + "Custom Architecture Rules".
- **Goal**: Machine-enforced constraints, not just human review.

### B. Initialize Test Framework
- **Action**: Setup test runner (Jest, JUnit, Pytest).
- **Rule**: Ensure `npm test` or equivalent runs instantly.
- **Goal**: Enable TDD feedback loop from minute one.

### C. Configure CI Pipeline
- **Action**: Create `.github/workflows/ci.yml` (or equivalent).
- **Content**:
  - Checkout code
  - Install dependencies
  - Run Lint
  - Run Tests
- **Goal**: The "Truth" of Clean State is defined by the CI status, not local machine.

### D. Configure Observability (Eyes & Ears)
- **Action**: Setup Logging & Reporting.
  - Create `logs/` directory (gitignored).
  - Configure Test Reporter (e.g., `jest-html-reporter`, `junit-xml`).
  - Configure Logger (e.g., `winston`, `log4j`) to output to both console and file.
- **Goal**: Give the Agent "eyes" to see runtime state and "ears" to hear system health.
