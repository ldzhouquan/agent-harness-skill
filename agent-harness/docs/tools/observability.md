# Observability: Eyes and Ears for Agents

Agents need senses too. Give them eyes (UI visibility) and a stethoscope (internal state).

## The Three Pillars

### 1. Logs

**What**: Structured, machine-readable event records

**Format**: Use JSON logs, not free text

**Example**:
```json
{
  "timestamp": "2024-01-15T10:30:00Z",
  "level": "info",
  "event": "user_login",
  "userId": "user-123",
  "email": "user@example.com",
  "success": true
}
```

**Query Language**: LogQL (for Loki/Grafana)

**Common Queries**:
- `{app="my-app"} |= "error"` - Find all errors
- `{app="my-app"} | json | level="error"` - Structured error search

---

### 2. Metrics

**What**: Numeric measurements over time

**Tool**: Prometheus

**Query Language**: PromQL

**Common Metrics**:
- `http_requests_total` - Request count
- `http_request_duration_seconds` - Latency
- `error_rate` - Error percentage

**Example Prompts Made Possible**:
- "Ensure service starts within 800ms"
- "Keep p95 latency under 2s for all user journeys"

---

### 3. Tracing

**What**: End-to-end request visibility

**Tool**: OpenTelemetry, Jaeger

**Why**: See how a request flows through services

---

## Agent Workspace Setup

Each agent task gets:
- Isolated logs (no cross-talk)
- Dedicated metrics endpoint
- Temporary, disposable observability environment

Like a soundproof booth for each agent.

---

## Giving Agents Senses

### Browser Automation (Eyes)

**Tool**: Puppeteer, Playwright

**Capabilities**:
- Take screenshots
- Inspect DOM
- Simulate user interactions
- Verify UI state

**Example**:
```typescript
// Test "new chat" feature
await page.click('#new-chat-button');
await page.screenshot({ path: 'result.png' });
// Verify sidebar shows new conversation
```

---

## How This Changes Things

**Before**: Agent writes code, human has to verify UI

**After**: Agent can:
1. Open the app
2. Click buttons
3. See what's rendered
4. Check logs for errors
5. Look at metrics
6. Fix issues autonomously

---

## Return on Investment

With good observability:
- Single agent task can run 6+ hours unsupervised
- Often overnight while humans sleep
- Full self-verification loop

---

*If you can't measure it, an agent can't fix it.*
