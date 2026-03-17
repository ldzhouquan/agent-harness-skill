# Module: Bug Fix Protocol (TDD First)

↩️ [返回概览](../SKILL.md) | [查看开发工作流](development-workflow.md)

> ⚠️ **CRITICAL: READ THIS BEFORE DOING ANYTHING ELSE**
>
> IF YOU SKIP STEP 1 (WRITE FAILING TEST FIRST), YOU HAVE FAILED.

## The TDD Rule: RED → GREEN → REFACTOR

**YOU CANNOT SKIP ANY STEP. NOT ONE. NOT EVER.**

### The Four Steps

1. **RED** - Prove the bug exists with a failing test
2. **GREEN** - Fix the code
3. **REFACTOR** - Clean up, run all tests, run linter
4. **VERIFY** - Create verification log with evidence

**NO BUG FIX IS COMPLETE WITHOUT ALL FOUR STEPS.**

---

## Quick Workflow

### Step 1: RED - Write Failing Test FIRST

**This is the most important step. Do not skip it.**

1. Find or create test file (`*.test.ts`, `test_*.py`, etc.)
2. Write test that reproduces the bug
3. **Run test and verify it FAILS**
4. Save failure output as evidence

👉 **Detailed guide:** [references/bugfix/tdd-workflow.md](references/bugfix/tdd-workflow.md)

### Step 2: GREEN - Fix the Bug

1. Analyze the failing test output
2. Fix the minimal code needed
3. Run test and verify it PASSES
4. Save passing output as evidence

### Step 3: REFACTOR - Clean Up

1. Review changes for quality
2. Run ALL tests (not just the new one)
3. Run linter
4. Check for technical debt

### Step 4: Create Verification Log

Create `BUGFIX_VERIFICATION.md` with:
- Bug description
- Failure evidence (test output)
- Success evidence (test output)
- Clean state confirmation

👉 **Template:** [references/bugfix/verification-log.md](references/bugfix/verification-log.md)

---

## Quick Checklist

Before you claim a bug is fixed, verify ALL of these:

- [ ] Step 1: Wrote failing test BEFORE fixing code
- [ ] Step 1: Ran test and confirmed it fails
- [ ] Step 1: Saved failure output
- [ ] Step 2: Fixed only the bug (no scope creep)
- [ ] Step 2: Ran test and confirmed it passes
- [ ] Step 2: Saved passing output
- [ ] Step 3: Ran ALL tests
- [ ] Step 3: Ran linter
- [ ] Step 4: Created verification log
- [ ] Clean State maintained

**IF ANY BOX IS NOT CHECKED, THE BUG FIX IS NOT COMPLETE.**

---

## What If You Can't Write an Automated Test?

This should be extremely rare. If you truly can't write a test:

1. Document why in verification log
2. Create manual reproduction script
3. Follow RED → GREEN with manual verification
4. Save evidence (screenshots, terminal output)

**Prefer automated tests whenever possible.**
