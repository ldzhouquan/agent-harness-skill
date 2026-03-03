# Clean State Definition

## What is Clean State?

A codebase is in **Clean State** when:

1. ✅ All tests pass (`npm test`)
2. ✅ No linter errors (`npm run lint`)
3. ✅ Development server starts without errors
4. ✅ App loads in browser with no console errors
5. ✅ `git status` shows no uncommitted changes
6. ✅ `features.json` is updated with any completed work
7. ✅ `progress.md` has session summary

## The Iron Law

**YOU MUST LEAVE THE CODEBASE IN CLEAN STATE BEFORE ENDING A SESSION.**

No exceptions. No "I'll fix it tomorrow." No half-implemented features.

## What If You Can't Reach Clean State?

If you're stuck and can't get to clean state:

1. **Git revert** to the last known clean state
2. **Document** what you tried in `progress.md`
3. **Mark** any work-in-progress clearly
4. **Never** leave broken code for the next agent

## Why This Is Non-Negotiable

1. **The next agent is失忆** - They don't know what you were doing
2. **No hidden state** - Everything must be in files/git
3. **Fast recovery** - New sessions can start immediately
4. **Trust** - Agents can rely on the codebase being usable

---

*Clean state isn't about perfection. It's about respect for the next agent.*
