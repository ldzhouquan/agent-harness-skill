# Build to Delete

## The Premise

**Your harness code will be obsolete within 6 months.**

- New models will make complex pipelines unnecessary
- What required 100 lines of control code might be a single prompt
- Over-engineered harnesses become liabilities

## The Strategy: Build for Disposal

### 1. Keep It Lightweight

- Avoid deep abstractions
- Prefer simple, composable functions
- No "clever" control flows

### 2. Loose Coupling

- Harness components like Lego bricks
- Easy to remove individual pieces
- No deep dependency chains

### 3. Document, Don't Over-Engineer

- Prefer clear patterns over complex frameworks
- Document "why" so future you knows what to keep

## What to Keep, What to Delete

| Keep | Delete Eventually |
|------|------------------|
| Git workflows | Complex prompt chaining |
| Linter rules | Workarounds for model limitations |
| Test infrastructure | Custom memory management |
| Feature tracking (JSON) | Clever state machines |

## The Real Value Isn't the Code

The most valuable output of your harness isn't the harness itself—it's the **crash data**.

- Every time an agent fails mid-task
- Every model drift captured
- Every breakpoint in long workflows

This data trains the next generation of models.

## Example: Evolution Timeline

- **2024**: Need complex pipeline for multi-step tasks
- **2025**: Single prompt can do same task
- **2026**: Model natively handles it

Your 2024 harness code is gone, but the crash data lives on.

---

*Build harnesses like you're going to throw them away—because you are.*
