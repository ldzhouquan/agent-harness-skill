# Custom Linters & Rules

Linters aren't just for catching errors—they're for injecting context and prompts.

## Linter as Prompt Injector

When a linter errors, it doesn't just say "wrong"—it tells the agent **how to fix it**.

### Example: Layer Import Violation

**Error Message**:
```
❌ Layer violation: service/auth.ts importing from ui/Button.tsx
Service layer cannot reference UI layer.

💡 Fix: Move shared logic to utils/ or types/,
    or create a service function that the UI can call.
    See docs/architecture/layers.md for details.
```

The agent reads this like a prompt and knows exactly what to do.

---

## Custom Linter Rules

### 1. `no-cross-layer-imports`

**What it does**: Prevents importing from higher layers.

**Severity**: Error

**Auto-fix prompt included**: Yes

**Example violations**:
- Service → UI ❌
- UI → Data Access directly ❌
- Service → Data Access ✅

---

### 2. `must-use-providers`

**What it does**: Forces use of providers module for cross-cutting concerns.

**Severity**: Error

**Example violations**:
```typescript
// ❌ Direct JWT import
import jwt from 'jsonwebtoken';

// ✅ Use providers
import { auth } from '../providers';
```

---

### 3. `no-optimistic-data-access`

**What it does**: Flags unvalidated external data access.

**Severity**: Error

**Example violations**:
```typescript
// ❌ Optimistic access
const userId = data.user.id;

// ✅ Validated
const userId = UserSchema.parse(data).user.id;
```

---

### 4. `feature-json-only-edit-passes`

**What it does**: Ensures only `passes` and `completed_at` are edited in features.json.

**Severity**: Error

**Why**: Prevents accidental modification of feature descriptions.

---

### 5. `enforce-clean-state`

**What it does**: Checks for clean state before allowing commits.

**Severity**: Warning (pre-commit hook)

**Checks**:
- No uncommitted changes
- All tests pass
- No linter errors

---

## How to Add a New Linter Rule

1. Define the error message with clear fix instructions
2. Link to relevant documentation
3. Make it actionable—agent should know what to do next

---

## Linter Output Format

Always structure linter errors like this:

```
❌ [Rule-Name] Brief error description

💡 What to do: Clear, step-by-step fix instructions
📚 Reference: docs/path/to/explanation.md
```

---

*Linters don't just enforce rules—they teach.*
