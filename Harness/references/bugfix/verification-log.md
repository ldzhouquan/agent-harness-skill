# Bug Fix Verification Log - Template

## MANDATORY: You MUST create this file. NO EXCEPTIONS.

Create `BUGFIX_VERIFICATION.md` in the project root:

```markdown
# Bug Fix Verification

## Bug Description
[What was wrong? Be specific. Example: "calculateDiscount was returning 0.05 for amounts over 1000 instead of 0.1"]

## Step 1: RED - Reproduce Bug
- [ ] Test created at: __tests__/discount.test.ts
- [ ] Test FAILS as expected
- **Evidence of Failure:**
  ```
  [PASTE EXACT TEST FAILURE OUTPUT HERE]
  ```

## Step 2: GREEN - Fix Applied
- [ ] Code fixed at: src/calculator.ts
- [ ] Test NOW PASSES
- **Evidence of Success:**
  ```
  [PASTE EXACT TEST PASSING OUTPUT HERE]
  ```

## Step 3: REFACTOR - Clean Up
- [ ] Code reviewed for quality
- [ ] All existing tests still pass
- [ ] Lint passes

## Final Verification
- [ ] Clean state maintained
- [ ] No uncommitted changes
- [ ] All tests pass

**Fixed by:** Harness Agent
**Date:** YYYY-MM-DD
```

---

## How to Record Evidence

### For Test Failure (RED step):

Run your test and copy the EXACT output:

```bash
npm test -- --testPathPattern=discount
```

Copy everything from the output, especially:
- The test name that failed
- Expected vs Received values
- The stack trace (if any)

### For Test Success (GREEN step):

After fixing the code, run the test again:

```bash
npm test -- --testPathPattern=discount
```

Copy the PASS output:

```
 PASS  __tests__/discount.test.ts
  calculateDiscount
    ✓ should return 10% discount for amounts over 1000 (3ms)
```

---

## What If You Can't Write an Automated Test?

This should be extremely rare. If you truly can't write a test:

1. **Document why** in the verification log
2. **Create a manual reproduction script** (shell script, curl commands, etc.)
3. **Follow RED → GREEN** with manual verification
4. **Take screenshots or save terminal output as evidence**

Example for manual verification:
```markdown
## Manual Verification
- [ ] Created reproduction script: scripts/repro_bug.sh
- [ ] Ran script before fix - FAILED (see output below)
- [ ] Applied fix
- [ ] Ran script after fix - PASSED (see output below)

### Before Fix Output:
$ bash scripts/repro_bug.sh
Error: NullPointerException at line 42

### After Fix Output:
$ bash scripts/repro_bug.sh
Success: User data returned correctly
```

**Prefer automated tests whenever possible.**
