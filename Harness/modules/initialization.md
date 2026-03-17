# Module 1: Project Initialization

↩️ [返回概览](../SKILL.md) | [查看工作流](../workflow.md)

## Quick Overview

Initialize a new project in this order:

1. **Create documentation structure** → [templates.md](../references/initialization/templates.md)
2. **Set up engineering tools** → [toolchain.md](../references/initialization/toolchain.md)
3. **Verify environment works** → [handover.md](../references/initialization/handover.md)

---

## Step 1: Create Documentation Structure

**File:** [references/initialization/templates.md](../references/initialization/templates.md)

Create these files in your project:

| File | Purpose |
|------|---------|
| `AGENTS.md` | Project map for agents |
| `docs/architecture.md` | Architecture overview |
| `feature_list.json` | Feature tracking |
| `progress.txt` | Progress log |

**Directory structure:**
```
docs/
├── designs/           # Design docs
├── plans/             # Execution plans
├── principles/        # Core beliefs
├── specs/             # Product specs
├── references/        # References
├── tech-debt/        # Technical debt
└── quality-scores/   # Quality docs
```

---

## Knowledge Base Principles

### Progressive Disclosure
- Start with 100-line `AGENTS.md`
- Then tell agents where to find next information
- Don't overwhelm at start

### Knowledge Must Be In Repository
- Anything inaccessible in runtime context effectively doesn't exist
- Slack channels, Google Docs, knowledge in brains - all inaccessible to system
- Move important knowledge into repo, but organized like onboarding new teammates

### Document Quality Assurance
- Linter and CI tasks validate knowledge base links
- "Document Gardener" agent runs regularly, scans for outdated docs

---

## Step 2: Set Up Engineering Tools

**File:** [references/initialization/toolchain.md](../references/initialization/toolchain.md)

| Component | Required | Action |
|-----------|----------|--------|
| **Linter** | Yes | Configure ESLint/Ruff/Checkstyle |
| **Formatter** | Yes | Configure Prettier/Black |
| **Test Framework** | Yes | Configure Jest/Pytest/JUnit |
| **CI Pipeline** | Yes | Create `.github/workflows/ci.yml` |
| **Logs** | Yes | Create `logs/` directory |

**CI Pipeline Template (TypeScript):**
```yaml
name: CI
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: '20' }
      - run: npm ci
      - run: npm run lint || true
      - run: npm test
```

---

## Step 3: Verify Environment Works

**File:** [references/initialization/handover.md](../references/initialization/handover.md)

Run the **Hello World Test** to prove everything works:

1. Create a dummy feature in `feature_list.json`
2. Write a failing test
3. Implement minimal code
4. Verify test passes, linter passes, logs work
5. Clean up

**Or run the verification script:**
```bash
./Harness/scripts/verify-clean-state.sh
```

---

## Verification Checklist

Before initialization is complete, verify:

- [ ] AGENTS.md created
- [ ] docs/architecture.md created
- [ ] feature_list.json created
- [ ] progress.txt created
- [ ] Test framework works (`npm test`)
- [ ] Linter works (`npm run lint`)
- [ ] CI pipeline configured
- [ ] logs/ directory created

**Only then is Initialization Complete.**
