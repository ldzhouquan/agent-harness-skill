# Golden Rules

These are enforceable engineering standards that can be checked by linters.

## Rule 1: No Optimistic Data Access

**What it means**: Never assume a field exists on external data.

**Bad**:
```typescript
const userId = data.user.id; // Crashes if user is missing
```

**Good**:
```typescript
// Option 1: Explicit check
if (!data.user?.id) {
  throw new Error('Missing user.id');
}
const userId = data.user.id;

// Option 2: Schema validation
const validated = UserSchema.parse(data);
const userId = validated.user.id;

// Option 3: Use data access layer
const user = await users.getById(data.userId);
```

**Why**: Prevents crashes from unexpected data shapes.

---

## Rule 2: Prefer Shared Utilities Over Duplication

**What it means**: Use the shared utils directory instead of writing the same function in multiple places.

**Bad**:
```typescript
// In file A
function formatDate(date: Date) { /* ... */ }

// In file B
function formatDate(date: Date) { /* slightly different */ }
```

**Good**:
```typescript
// In utils/dates.ts
export function formatDate(date: Date) { /* ... */ }

// Everywhere else
import { formatDate } from '../utils/dates';
```

**Why**:
- Single source of truth
- Fixes apply everywhere
- No divergent implementations

---

## Rule 3: External Data Must Be Validated at Boundaries

**What it means**: All data entering from outside (API, DB, files) must be validated.

**Where**: In the **Data Access Layer**.

**How**: Use Zod, Joi, or similar schema validators.

**Example**:
```typescript
// data/users.ts
import { z } from 'zod';

const UserSchema = z.object({
  id: z.string().uuid(),
  email: z.string().email(),
  name: z.string(),
});

export async function getUserById(id: string) {
  const row = await db.query('SELECT * FROM users WHERE id = $1', [id]);
  // Validate before returning
  return UserSchema.parse(row);
}
```

---

## Rule 4: No Circular Dependencies

**What it means**: File A imports File B, which imports File A = ❌

**How**: The linter will catch this.

**Fix**: Extract shared code to a third file.

---

## Rule 5: Tests Are Part of the Feature

**What it means**: A feature isn't done without tests.

**How**: `features.json` specifies test requirements.

**What to test**:
- Unit tests for pure functions
- Integration tests for service layer
- E2E tests for critical user journeys

---

## Rule 6: Logs Are for Machines, Comments for Humans

**What it means**:
- Logs = Structured, machine-parseable data
- Comments = Why, not what

**Good log**:
```typescript
logger.info('User login successful', {
  userId: user.id,
  email: user.email,
  timestamp: new Date().toISOString(),
});
```

---

## Enforcement

All these rules are enforced by custom linters. See [linters.md](../tools/linters.md).

*Golden Rules aren't about taste. They're about preventing predictable failures.*
