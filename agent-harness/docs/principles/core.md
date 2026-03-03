# Core Principles

These are the non-negotiable beliefs that guide everything we do.

## 1. Single Agent, Serial Execution

- **Why**: Programming is high-density write operations
- **Result**: No decision conflicts, no catastrophic merges
- **Exception**: Read-only/verification agents can work in parallel

## 2. Memory Lives Outside the Model

- **Why**: Context windows are finite; compression is lossy
- **How**: Use files, git, logs for memory
- **Rule**: If it's not in the repo, it doesn't exist

## 3. Default Failure

- **Why**: Agents get overconfident
- **How**: All features start as `passes: false`
- **Rule**: Must pass tests to mark as complete

## 4. One Feature at a Time

- **Why**: Prevents "biting off too much"
- **How**: `features.json` enforces this
- **Rule**: Never work on more than one feature per session

## 5. Clean State is Mandatory

- **Why**: Next agent is "amnesiac"
- **How**: Git commits + progress file
- **Rule**: Never leave broken code for next session

## 6. Observability is First-Class

- **Why**: Agents need eyes and ears too
- **How**: Logs, metrics, tracing built-in
- **Rule**: Features include observability requirements

## 7. JSON > Markdown for Structure

- **Why**: Models accidentally modify Markdown structure
- **How**: `features.json` uses strict JSON
- **Rule**: Only edit `passes` and `completed_at` fields

---

*These principles are not suggestions. They are the operating system.*
