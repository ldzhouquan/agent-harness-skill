# Providers Pattern

## What are Cross-Cutting Concerns?

These are things every module needs but shouldn't implement themselves:
- Authentication
- Logging
- Feature flags
- Tracing
- Metrics

## The Problem

If each module implements auth independently:
- Inconsistent behavior
- Hard to update
- Security gaps
- Code duplication

## The Solution: Single Entry Point

All cross-cutting concerns must be accessed through a **single `providers` module**.

### Directory Structure

```
src/
├── providers/
│   ├── index.ts          # Public API
│   ├── auth.ts           # Auth implementation
│   ├── logging.ts        # Logging implementation
│   └── tracing.ts        # Tracing implementation
```

### Usage

**Correct**:
```typescript
import { auth, logger } from '../providers';

async function handler(req: Request) {
  const user = await auth.getCurrentUser(req);
  logger.info('Request handled', { userId: user.id });
}
```

**Incorrect**:
```typescript
// ❌ Don't do this - each module rolling its own
import jwt from 'jsonwebtoken';
const user = jwt.verify(req.headers.authorization, SECRET);
```

## Why This Works

1. **Single source of truth** - Update auth in one place
2. **Consistent behavior** - All modules use the same logic
3. **Testable** - Easy to mock providers in tests
4. **Enforceable** - Linter can block alternative paths

## Linter Rule

The `must-use-providers` linter will:
- Flag direct imports of auth/logging/etc libraries
- Suggest importing from `providers` instead
- Provide auto-fix instructions

---

*No backdoors. All access through the front door.*
