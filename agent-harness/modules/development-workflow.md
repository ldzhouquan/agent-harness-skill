# Module 4: Incremental Development Workflow

↩️ [返回概览](../SKILL.md) | [查看工作流](../workflow.md) | [模块索引](../modules.md)

## Context Discovery Phase (Startup)
**Must execute at start of EVERY session:**
1. **Locate**: Run `pwd` to confirm working directory
2. **Ground**: Run `ls -R` (limit depth) and read config files (e.g., `package.json`, `pyproject.toml`) to understand environment
3. **Recall**: Read `progress.txt`, `feature_list.json`, and `git log -20`
4. **Claim**: Select highest priority feature with `pass: false`
5. **Verify**: Run basic tests to confirm system health before starting

## Reflexion Protocol (The Feedback Loop)

**Agent MUST execute this loop continuously:**
`Design -> Implement -> Lint -> Test -> Reflexion`

### 1. When Tests Fail (Fail Fast, Look First, Think Slow)
**STOP immediately. Do NOT retry blindly.**
1. **Observe (Eyes & Ears)**: 
   - Read the logs (`tail -n 50 logs/app.log`).
   - Check screenshots/snapshots (if UI test).
   - Don't just look at the exit code!
2. **Hypothesize**: Why did it fail? (Logic error? Environment? Flaky?)
3. **Instrument**: Add more logs if current ones are insufficient.
4. **Plan Fix**: Formulate a new plan based on **evidence**.
   - If code logic is wrong -> **Fix Code**.
   - If design is flawed -> **Fix Design** (Update specs first).
5. **Execute**: Apply fix only after understanding root cause.

### 2. When Tests Pass (Success Check & Self-Review)
**Do NOT celebrate yet. Verify quality:**
1. **Architecture Check**: Did I violate layering? (Run Linter)
2. **Tech Debt Check**: Did I leave hardcoded values or TODOs?
3. **Coverage Check**: Did I cover edge cases?

## Pre-Completion Protocol
**Before marking feature as passed (`pass: true`), you MUST:**
1. **Self-Review**: Read full diff of your changes.
2. **Verification Log**: Output a log comparing:
   - Original Requirement
   - Final Implementation
   - Test Results (Evidence of success)
   - **Observability Evidence**: Link to log snippet or screenshot proving success.
3. **Clean State**: Ensure no uncommitted changes, temporary files, or broken tests.

## One Feature At A Time Rule
- Select one feature -> Test -> Implement -> Verify -> Commit -> Log
- **Never** work on multiple features simultaneously
- **Never** leave broken code for the next session
