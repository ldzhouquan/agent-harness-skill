---
name: SystemAnalysis
description: System analysis for financial/enterprise software projects. USE WHEN system analysis, system design document, system analysis document, PRD analysis, technical specification, project analysis, risk analysis, security analysis, stability analysis.
---

# SystemAnalysis

系统分析 Skill - 结构化分析业务需求，实现企业级系统设计，形成系统分析文档。

## Voice Notification

**When executing a workflow, do BOTH:**

1. **Send voice notification**:
   ```bash
   curl -s -X POST http://localhost:8888/notify \
     -H "Content-Type: application/json" \
     -d '{"message": "Running the WORKFLOWNAME workflow in the SystemAnalysis skill to ACTION"}' \
     > /dev/null 2>&1 &
   ```

2. **Output text notification**:
   ```
   Running the **WorkflowName** workflow in the **SystemAnalysis** skill to ACTION...
   ```

## Workflow Routing

| Workflow | Trigger | File |
|----------|---------|------|
| **CreateAnalysis** | "create system analysis", "write system analysis", "new system analysis document" | `Workflows/CreateAnalysis.md` |
| **AnalyzeAspect** | "analyze database", "analyze security", "analyze stability", "analyze risk", "analyze performance" | `Workflows/AnalyzeAspect.md` |
| **ReviewAnalysis** | "review system analysis", "check system analysis", "validate system analysis" | `Workflows/ReviewAnalysis.md` |
| **GenerateTemplate** | "generate template", "template for", "section template" | `Workflows/GenerateTemplate.md` |

## Quick Reference

**分析领域 (Analysis Domains):**
- 项目整体分析 (Project Overall)
- 数据库设计 (Database Design)
- 业务分析 (Business Analysis)
- 稳定性分析 (Stability Analysis)
- 资损风险分析 (Financial Loss Risk)
- 安全风险分析 (Security Risk)
- 运维分析 (Operations Analysis)
- 系统间关系 (Inter-system Relationships)

**Full Documentation:**
- Templates: `SkillSearch('systemanalysis templates')` → loads Templates.md
- Examples: `SkillSearch('systemanalysis examples')` → loads Examples.md

## Examples

**Example 1: Create a new system analysis document**
```
User: "Create a system analysis document for a new payment system"
→ Invokes CreateAnalysis workflow
→ Collects project background and goals
→ Generates comprehensive system analysis document based on 15 sections
→ Outputs structured markdown document
```

**Example 2: Analyze specific aspect**
```
User: "Analyze the database design for our order system"
→ Invokes AnalyzeAspect workflow
→ Focuses on database design section
→ Analyzes table structure, relationships, naming conventions
→ Provides optimization recommendations
```

**Example 3: Review existing analysis**
```
User: "Review my system analysis document for completeness"
→ Invokes ReviewAnalysis workflow
→ Checks all 15 required sections
→ Validates each section meets analysis standards
→ Provides completeness report with gaps
```
