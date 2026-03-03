# Feature Workflow: How to Implement One Feature

Remember: **ONE FEATURE PER SESSION**.

## Before You Code

1. ✅ Read the feature description carefully
2. ✅ Understand the verification `steps`
3. ✅ Note the `tests` requirements
4. ✅ Check `depends_on` are all passing

## During Implementation

### Rule: Incremental Testing

Don't write all the code first!

1. Write a little code
2. Test it
3. Repeat

### If You Get Stuck

1. Check git history for similar patterns
2. Look at existing code for inspiration
3. If still stuck: git revert to clean state, document in progress.md, try a different approach

### What to Avoid

- ❌ Don't work on multiple features
- ❌ Don't leave half-implemented code
- ❌ Don't skip tests
- ❌ Don't modify feature description in features.json

## Before You Mark as Passing

Verify **everything** in the feature's `steps`:

Example steps:
```json
"steps": [
  "Navigate to main interface",
  "Click the 'New Chat' button",
  "Verify a new conversation is created",
  "Check that chat area shows welcome state",
  "Verify conversation appears in sidebar"
]
```

Go through **each step** manually (via browser automation if possible).

## Run All Required Tests

```bash
npm test  # or pytest, etc.
```

Ensure all tests specified in `tests` field pass.

## End of Session Checklist

Before you finish, confirm:

- [ ] Feature is fully implemented
- [ ] All verification steps pass
- [ ] All required tests pass
- [ ] `features.json` updated: `passes: true` and `completed_at` set
- [ ] `progress.md` updated with session summary
- [ ] `git status` shows no uncommitted changes
- [ ] All changes committed with meaningful message
- [ ] Development server still starts cleanly
- [ ] App loads with no console errors

**You must hit all these to be in Clean State!**

---

*One feature. One session. Clean state.*
