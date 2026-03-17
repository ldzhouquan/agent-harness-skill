# Module 4: Incremental Development Workflow

↩️ [返回概览](../SKILL.md) | [查看工作流](../workflow.md)

## Context Discovery Phase (Startup)
**Must execute at start of EVERY session:**
1. **Locate**: Run `pwd` to confirm working directory
2. **Ground**: Run `ls -R` (limit depth) and read config files (e.g., `package.json`, `pyproject.toml`) to understand environment
3. **Recall**: Read `progress.txt`, `feature_list.json`, and `git log -20`
   - **IF progress.txt DOES NOT EXIST: CREATE IT NOW**
   - **IF feature_list.json DOES NOT EXIST: CREATE IT NOW**
4. **Verify**: Run basic tests to confirm system health before starting
5. **Claim**: Select highest priority feature with `pass: false`

## One Feature At A Time Rule
- Select one feature -> Test -> Implement -> Verify -> Commit -> Log
- **Never** work on multiple features simultaneously
- **Never** leave broken code for the next session

## Reflexion Protocol (The Feedback Loop)

**Agent MUST execute this loop continuously:**
`Design -> Implement -> Lint -> Test -> Reflexion`

### 1. When Tests Fail → CHECKLIST

> ⚠️ **YOU MUST COMPLETE ALL STEPS BEFORE FIXING CODE**

- [ ] **Step 1: Run the failing test** - Execute test command, capture output
- [ ] **Step 2: Analyze failure** - Read error message, identify root cause
- [ ] **Step 3: Document hypothesis** - Write down why you think it fails
- [ ] **Step 4: Fix ONE thing** - Make minimal change based on hypothesis
- [ ] **Step 5: Re-run test** - Verify fix works before continuing

**NEVER fix code without running test first.**

### 2. When Tests Pass (Success Check & Self-Review)
**Do NOT celebrate yet. Verify quality:**
1. **Architecture Check**: Did I violate layering? (Run Linter)
2. **Tech Debt Check**: Did I leave hardcoded values or TODOs?
3. **Coverage Check**: Did I cover edge cases?

## Pre-Completion Protocol
**Before marking feature as passed (`pass: true`), you MUST:**

1. **RUN THE TESTS - NO EXCEPTIONS**
   - Execute the test command (`npm test`, `pytest`, `cargo test`, etc.)
   - **SAVE THE OUTPUT TO A FILE** - create `test_results.txt` and paste output there
   - Confirm **ALL TESTS PASS** (not just the ones you wrote)
   - If tests fail, go back to Reflexion Loop - DO NOT PROCEED

2. **Self-Review**: Read full diff of your changes.

3. **Verification Log**: Output a log comparing:
   - Original Requirement
   - Final Implementation
   - **Test Results (Evidence of success)** - PASTE THE ACTUAL TEST OUTPUT HERE
   - **Observability Evidence**: Link to log snippet or screenshot proving success.

4. **Update progress.txt**: See [modules/progress-tracking.md](modules/progress-tracking.md)

5. **Mark feature complete**: See [modules/feature-management.md](modules/feature-management.md)

6. **Clean State**: Ensure no uncommitted changes, temporary files, or broken tests.
