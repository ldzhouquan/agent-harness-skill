# Getting Started: New Project Setup

Welcome! Follow this checklist to set up a new agent harness project.

## Prerequisites

- Git repository initialized
- Node.js/Python/etc installed (depending on stack)
- This harness skill installed

## Step 1: Run the Setup Script

```bash
# From your project root
python3 path/to/agent-harness/scripts/setup_harness.py \
  --project-name "Your Project Name" \
  --project-type web  # or backend, data
```

This creates:
- `features.json` - Feature tracking (start with everything failing!)
- `progress.md` - Session progress log
- `init.sh` - Development server startup

## Step 2: Customize features.json

Edit `features.json` to define your actual features:

1. Keep the `setup-001` feature (critical priority)
2. Add your own features with:
   - Clear `description`
   - Correct `priority` (critical > high > medium > low)
   - `depends_on` for dependencies
   - `steps` for verification
   - `tests` requirements
   - `agent_role` assignment

3. **Important**: Leave `passes: false` on everything!

## Step 3: Create Docs Directory (Optional but Recommended)

For larger projects, set up the knowledge base:

```
docs/
├── architecture/
│   ├── overview.md
│   ├── layers.md
│   └── providers.md
├── principles/
│   ├── core.md
│   └── golden-rules.md
└── design/
    └── product-specs.md
```

## Step 4: Initial Git Commit

```bash
git add -A
git commit -m "Initialize agent harness"
```

## Step 5: You're Ready!

First coding session should:
1. Start with `setup-001` feature
2. Follow the session startup sequence
3. Always leave in clean state

---

*Remember: Start small, fail fast, iterate.*
