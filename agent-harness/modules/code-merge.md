# Module 6: Code Merge Strategy

↩️ [返回概览](../SKILL.md) | [查看工作流](../workflow.md) | [模块索引](../modules.md)

## Cost Function Inversion
**Traditional World:** Fixing expensive, waiting cheap  
**Agent World:** Fixing cheap, waiting expensive → Fast release, fast exposure, fast fix

## Three Key Actions

1. **Minimize Blocking Gates** - Keep only minimal blocking gates
2. **Keep PR Lifecycle Short** - High-frequency small-step fast merges, collision probability extremely low
3. **Never Let Flaky Tests Block Progress Indefinitely** - Use re-run mechanism instead of blocking

**Applicability:** Only holds when agent code output far exceeds human attention.
