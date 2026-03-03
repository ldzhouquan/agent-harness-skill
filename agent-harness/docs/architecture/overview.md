# Architecture Overview

## Bird's Eye View

This project follows a strictly layered architecture with unidirectional dependencies.

## Business Domains

Identify your core business domains first. Examples:
- Authentication
- User Management
- Chat
- Billing

## Code Layers

From innermost to outermost:

1. **Types Layer** - Core data structures, interfaces, enums
2. **Configuration Layer** - App config, environment variables
3. **Data Access Layer** - Database queries, external API clients
4. **Service Layer** - Business logic, use cases
5. **Runtime Layer** - Server setup, middleware, routing
6. **Interface Layer** - UI components, API handlers

## Dependency Rule

Code may only depend on layers **below** it, never above.

- Service Layer → Data Access Layer ✅
- Interface Layer → Service Layer ✅
- Service Layer → Interface Layer ❌ (Never!)

## Why This Matters

When 100 agents are modifying code simultaneously:
- No hidden dependencies = No unexpected breakages
- Changes propagate forward only
- Refactoring is predictable
- Merge conflicts are minimized

---

*See [layers.md](layers.md) for detailed layer definitions.*
