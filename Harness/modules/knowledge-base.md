# Module 2: Knowledge Base Management

↩️ [返回概览](../SKILL.md) | [查看工作流](../workflow.md)

## Structured Document Organization
- Design docs cataloged and indexed, each with validation status
- Execution plans split into in-progress, completed
- All embedded in code repo, versioned, centralized

## Progressive Information Disclosure
- Start with 100-line `AGENTS.md`
- Then told where to find next information
- Not overwhelmed at start

## Automated Document Quality Assurance
- Dedicated Linter and CI tasks validate knowledge base links
- "Document Gardener" agent runs regularly, scans for outdated docs
- Automatically opens PR to fix

## Knowledge Must Be In Repository
- Anything inaccessible in runtime context effectively doesn't exist
- Slack channels, Google Docs, knowledge in brains - all inaccessible to system
- Must move important knowledge into repo, but not chaotically - like onboarding new teammates
