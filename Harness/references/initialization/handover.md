# Handover Protocol (The Golden Spike)

The Handover Protocol proves the environment works before handing over to the Coding Agent. See [../modules/initialization.md](../modules/initialization.md) for the workflow overview.

---

## What is the Golden Spike?

The "Golden Spike" is a proven concept from railroad history - a single ceremonial spike that connected the transcontinental railroad, symbolizing completion.

In our context, it's a **minimal working feature** that proves:
- The test framework works
- The linter works
- The build system works
- Logs are being written

---

## The "Hello World" Test Protocol

### Step 1: Create a Dummy Feature

Add to `feature_list.json`:

```json
{
  "features": [
    {
      "id": 1,
      "name": "System Health Check",
      "description": "Basic health check endpoint",
      "pass": false,
      "started_at": "2026-03-13",
      "completed_at": null
    }
  ]
}
```

### Step 2: Write a Failing Test

Create `src/health.test.ts`:

```typescript
import { healthCheck } from './health';

describe('Health Check', () => {
  test('should return OK status', () => {
    const result = healthCheck();
    expect(result.status).toBe('OK');
  });
});
```

Run the test - it should **FAIL** because `healthCheck` doesn't exist yet.

### Step 3: Implement Minimal Code

Create `src/health.ts`:

```typescript
export function healthCheck() {
  return { status: 'OK' };
}
```

Run the test - it should **PASS**.

### Step 4: Verify Everything Works

1. **Test passes:** `npm test` ✅
2. **Linter passes:** `npm run lint` ✅
3. **Logs work:** Check `logs/` directory has content ✅

### Step 5: Clean Up

1. Remove the health check code
2. Reset `feature_list.json` to empty
3. Ensure no uncommitted changes

---

## Verification Checklist

Before marking initialization as complete, verify:

- [ ] **CI Pipeline**: `.github/workflows/ci.yml` exists and is valid
- [ ] **Test Runner**: `npm test` (or equivalent) runs successfully
- [ ] **Linter**: `npm run lint` (or equivalent) runs without errors
- [ ] **Logs**: `logs/` directory is created and writable

---

## Why This Matters

Without the Golden Spike verification:

1. **Hidden assumptions** - Agent assumes environment works, but it doesn't
2. **Debugging nightmare** - Is it the code or the environment?
3. **Wasted time** - Agent spends hours troubleshooting setup issues

With the Golden Spike:

1. **Proven environment** - Agent can trust the tools work
2. **Clear baseline** - Any failure is in new code, not setup
3. **Confidence** - Agent can proceed with minimal supervision

---

## Alternative: Using the Script

Run the automated verification:

```bash
./Harness/scripts/verify-clean-state.sh
```

This script checks:
- CI configuration exists
- Test framework is configured
- Linter is configured
- Logs directory exists

---

## When to Run

The Handover Protocol should run:

1. **After** setting up all tools (linter, test, CI)
2. **Before** starting any real feature development
3. **After** any significant environment change (new dependencies, config changes)
