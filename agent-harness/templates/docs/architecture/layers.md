# Layer Definitions

## 1. Types Layer

**Purpose**: Core data structures that everything else depends on.

**What goes here**:
- TypeScript interfaces/types
- Zod schemas
- Enum definitions
- Domain model definitions

**Example**:
```typescript
// types/user.ts
export interface User {
  id: string;
  email: string;
  name: string;
  createdAt: Date;
}
```

**Dependencies**: None (this is the foundation)

---

## 2. Configuration Layer

**Purpose**: Environment-specific configuration.

**What goes here**:
- Environment variable validation
- Feature flags
- Third-party API keys (via env vars)
- App settings

**Example**:
```typescript
// config/app.ts
export const config = {
  databaseUrl: process.env.DATABASE_URL!,
  port: parseInt(process.env.PORT || '3000'),
  enableAnalytics: process.env.ENABLE_ANALYTICS === 'true',
};
```

**Dependencies**: Types Layer only

---

## 3. Data Access Layer

**Purpose**: All external data access goes through here.

**What goes here**:
- Database repositories
- External API clients
- Cache access
- File system operations

**Rules**:
- Always validate incoming data (no optimistic access!)
- Wrap external errors in domain-specific errors
- No business logic here

**Example**:
```typescript
// data/users.ts
export async function getUserById(id: string): Promise<User | null> {
  const result = await db.query('SELECT * FROM users WHERE id = $1', [id]);
  if (!result.rows[0]) return null;
  // Validate before returning
  return UserSchema.parse(result.rows[0]);
}
```

**Dependencies**: Types Layer, Configuration Layer

---

## 4. Service Layer

**Purpose**: Business logic lives here.

**What goes here**:
- Use case implementations
- Domain logic
- Transaction coordination
- Authorization checks

**Example**:
```typescript
// services/auth.ts
export async function login(email: string, password: string): Promise<Session> {
  const user = await getUserByEmail(email);
  if (!user) throw new Error('User not found');
  if (!await verifyPassword(password, user.hashedPassword)) {
    throw new Error('Invalid password');
  }
  return createSession(user.id);
}
```

**Dependencies**: Types Layer, Data Access Layer

---

## 5. Runtime Layer

**Purpose**: Server setup and request handling.

**What goes here**:
- Express/Fastify app setup
- Middleware
- Route definitions
- Error handling middleware

**Dependencies**: Service Layer, Configuration Layer

---

## 6. Interface Layer

**Purpose**: User-facing code.

**What goes here**:
- React/Vue components
- API route handlers
- CLI commands
- GraphQL resolvers

**Dependencies**: Service Layer only (never Data Access directly!)

---

## Layer Enforcement

The custom linter will enforce these rules:
- `no-cross-layer-imports` - Prevents importing from higher layers
- `no-direct-data-access-in-ui` - UI must go through services

*See [linters.md](../tools/linters.md) for linter details.*
