# Module 1: Project Initialization

↩️ [返回概览](../SKILL.md) | [查看工作流](../workflow.md)

## 1. Create AGENTS.md Template
```markdown
# Project Map

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
- **Action**: Create config files (`.eslintrc`, `checkstyle.xml`, `.pylintrc`, `rulesets/pmd.xml`).
- **Rule**: Enforce "Industry Standard" + "Custom Architecture Rules".
- **Goal**: Machine-enforced constraints, not just human review.

**Recommended Toolchain:**
- **JS/TS**: ESLint (Airbnb/Standard) + Prettier + `eslint-plugin-import`
- **Java**: Checkstyle (Google) + PMD (Alibaba P3C) + ArchUnit
  - *Reference*: [Alibaba P3C PMD](https://github.com/alibaba/p3c/tree/master/p3c-pmd)
- **Python**: Ruff + Black + Mypy
- **Go**: GolangCI-Lint

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
  - **(Optional) Setup Visual Testing**: Install `jest-image-snapshot` or Playwright for UI projects.
- **Goal**: Give the Agent "eyes" to see runtime state and "ears" to hear system health.

## E. Handover Protocol (The Golden Spike)

**Verification: Proof of Life**
Before handing over to the Coding Agent, you MUST prove the environment works by implementing a "Tracer Bullet" feature.

**The "Hello World" Test:**
1.  **Create** a dummy feature in `feature_list.json` (e.g., "System Health Check").
2.  **Write** a failing test for it.
3.  **Implement** the minimal code.
4.  **Verify** test passes, linter passes, logs are generated.
5.  **Delete** the dummy feature (Clean State).

**Result:**
- CI Pipeline: Verified Green ✅
- Test Runner: Verified Working ✅
- Linter: Verified Enforcing ✅
- Logs: Verified Writable ✅

**Only then is Initialization Complete.**
