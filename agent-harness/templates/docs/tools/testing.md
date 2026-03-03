# Testing: Verification Made Explicit

Tests aren't just for humans—they define "done" for agents.

## Test Requirements in Features

Every feature in `features.json` specifies what tests are needed:

```json
{
  "id": "chat-001",
  "description": "User can create new chat",
  "tests": {
    "unit": true,
    "integration": true,
    "e2e": true
  }
}
```

## Test Types

### 1. Unit Tests

**What**: Test individual functions in isolation

**When**: Pure logic, no external dependencies

**Example**:
```typescript
describe('formatDate', () => {
  it('formats dates correctly', () => {
    expect(formatDate(new Date('2024-01-15')))
      .toBe('2024-01-15');
  });
});
```

---

### 2. Integration Tests

**What**: Test multiple components working together

**When**: Services, data access, external APIs

**Example**:
```typescript
describe('UserService', () => {
  it('creates user and saves to database', async () => {
    const user = await userService.create({ email: 'test@test.com' });
    const saved = await db.findUser(user.id);
    expect(saved.email).toBe('test@test.com');
  });
});
```

---

### 3. End-to-End (E2E) Tests

**What**: Test the whole system as a user would

**Tool**: Puppeteer, Playwright, Cypress

**Why**: Many bugs only show up at the UI level

**Example**:
```typescript
describe('New Chat', () => {
  it('creates conversation and shows in sidebar', async () => {
    await page.goto('/');
    await page.click('#new-chat');
    
    // Take screenshot for verification
    await page.screenshot({ path: 'new-chat.png' });
    
    // Verify via DOM
    const sidebar = await page.$('#sidebar');
    expect(sidebar).toContainText('New Conversation');
    
    // Verify input is cleared
    const input = await page.$('#message-input');
    expect(await input.inputValue()).toBe('');
  });
});
```

---

## Testing Workflow for Agents

1. **Read feature's test requirements** from `features.json`
2. **Write tests first** (TDD approach)
3. **Implement feature**
4. **Run tests**
5. **Only mark as passing** when all specified tests pass

---

## What "Passing" Means

A feature isn't `passes: true` until:
- All unit tests specified pass
- All integration tests specified pass
- All E2E tests specified pass
- Manual verification via screenshots (if UI feature)
- No console errors in browser

---

## Flaky Tests

**What**: Tests that sometimes pass, sometimes fail

**Rule**: Don't let flaky tests block progress!

**What to do**:
- Auto-retry 2-3 times
- If still flaky, create separate PR to fix
- Keep the main pipeline moving

**Why**: Waiting is expensive when 100 agents are blocked.

---

*A feature isn't done until the tests say it's done.*
