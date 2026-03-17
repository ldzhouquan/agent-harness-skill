# Bug Fix TDD Workflow - Detailed Guide

This document provides detailed instructions for each step of the RED → GREEN → REFACTOR workflow.

## Step 1: RED - Write Failing Test FIRST

### This is the MOST IMPORTANT step. Do NOT skip it.

**You must do this BEFORE writing any fix code.**

### How to do it:

1. **Check if test files already exist**
   - Run `ls` or `find . -name "*test*"` to locate test directory
   - If no tests exist, create a test file NOW

2. **Create/modify a test file**
   - For JS/TS: `*.test.ts` or `*.spec.ts` in `__tests__/` or `tests/`
   - For Python: `test_*.py` in `tests/`
   - The test should specifically reproduce the bug scenario

3. **Write the test that demonstrates the bug**
   - Be specific about the expected vs actual behavior
   - Use clear variable names
   - The test description should say exactly what's wrong

4. **RUN THE TEST AND VERIFY IT FAILS**
   - This is crucial. If the test passes, you haven't found the bug.
   - **SAVE THE FAILURE OUTPUT** - copy it exactly

5. **Create a temporary file with the failure evidence**
   - Name it `BUG_EVIDENCE.md` or `test_failure.txt`
   - Paste the exact failure output there
   - Include the command you ran

### Example - Copy this pattern:

TypeScript example:
```typescript
// __tests__/discount.test.ts
import { calculateDiscount } from '../src/calculator';

describe('calculateDiscount', () => {
  test('should return 10% discount for amounts over 1000', () => {
    // ARRANGE
    const amount = 1500;

    // ACT
    const result = calculateDiscount(amount);

    // ASSERT - This should FAIL before the fix
    expect(result).toBe(0.1);
  });
});
```

Run it:
```bash
npm test
```

**Copy the EXACT output** like this:
```
 FAIL  __tests__/discount.test.ts
  calculateDiscount
    ✕ should return 10% discount for amounts over 1000 (5ms)

  ● calculateDiscount › should return 10% discount for amounts over 1000

    expect(received).toBe(expected)

    Expected: 0.1
    Received: 0.05

      5 |   // ACT
      6 |   const result = calculateDiscount(amount);
    > 7 |
      8 |   // ASSERT - This should FAIL before the fix
      9 |   expect(result).toBe(0.1);
```

**SAVE THIS OUTPUT.** You will need it for the verification log.

---

## Step 2: GREEN - Fix the Bug

### ONLY AFTER YOU HAVE A FAILING TEST.

1. **Look at the failing test output** - understand exactly what's wrong
2. **Fix the code** - make the minimal necessary change
3. **RUN THE TEST AGAIN**
4. **Verify it PASSES**
5. **SAVE THE PASSING OUTPUT** too

### Example fix:

```typescript
// src/calculator.ts
export function calculateDiscount(amount: number): number {
  // BUG WAS HERE: had amount > 2000 instead of amount > 1000
  if (amount > 1000) {
    return 0.1;
  }
  return amount > 500 ? 0.05 : 0;
}
```

Run and verify it passes:
```bash
npm test
```

Output should show:
```
 PASS  __tests__/discount.test.ts
  calculateDiscount
    ✓ should return 10% discount for amounts over 1000 (3ms)
```

---

## Step 3: REFACTOR - Clean Up

### AFTER the test passes:

1. **Review your changes** - is the code clean?
2. **Check for technical debt** - any TODOs, hardcoded values?
3. **Run ALL tests** - not just the one you wrote
4. **Run linter** - make sure code style is correct
5. **Verify everything still passes**

---

## Why This Matters

The goal isn't just to fix the bug. The goal is to:

1. **Prove the bug existed** - with a failing test
2. **Fix it** - with minimal changes
3. **Prove it's fixed** - with a passing test
4. **Prevent regression** - with a test that will catch this bug in the future

If you skip any step, you haven't completed the bug fix.
