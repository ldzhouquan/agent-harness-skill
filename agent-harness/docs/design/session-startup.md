# Session Startup: Standard Operating Procedure

Every coding session follows this exact sequence. No shortcuts.

## The 8-Step Startup

### 1. Locate: Check Environment

```bash
pwd
ls -la
```

Confirm you're in the right directory and see the harness files.

---

### 2. Recall: Read Git History

```bash
git log --oneline -20
```

Rebuild the project timeline. What happened recently?

---

### 3. Recall: Read Progress File

```bash
cat progress.md
```

Read session summaries from previous agents.

---

### 4. Recall: Read Feature List

```bash
cat features.json
```

See what's done, what's next.

---

### 5. Choose: Select a Feature

Filter and sort:
1. `passes: false` only
2. All `depends_on` have `passes: true`
3. Sort by priority: critical > high > medium > low
4. Check `agent_role` matches your role

Pick the top one.

---

### 6. Reconstruct: Start Dev Server

```bash
./init.sh
```

Bring up the development environment.

---

### 7. Verify: Check Baseline

Run a quick test to ensure the app still works:
- Open in browser
- Check for console errors
- Verify basic functionality

**Never skip this!** The previous agent might have left something broken (though they shouldn't have).

---

### 8. Begin: Start Working

Now you're ready to implement the feature.

---

## Why This Exact Sequence?

This is ritualized for a reason:
- No forgotten steps
- Consistent across all agents
- No "I didn't know that" excuses
- Every session starts from the same baseline

---

*Locator, Recall, Reconstruct, Verify. Every time.*
