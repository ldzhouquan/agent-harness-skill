# ReviewAnalysis Workflow

This workflow reviews an existing system analysis document for completeness and quality.

## Input

User should provide:
- Path to the system analysis document, OR
- The document content directly

## Process

### Step 1: Read Document

Read the system analysis document provided by the user.

### Step 2: Check Completeness

Verify all 15 sections are present:

| Section | Chinese | Required |
|---------|---------|----------|
| 1 | 概述 | Yes |
| 2 | 项目整体分析 | Yes |
| 3 | 数据库设计 | Yes |
| 4 | 业务分析 | Yes |
| 5 | 现有系统影响分析 | Yes |
| 6 | 数据分析影响 | Yes |
| 7 | 测试策略分析 | Yes |
| 8 | 稳定性分析 | Yes |
| 9 | 资损风险分析 | For financial systems |
| 10 | 安全风险分析 | Yes |
| 11 | 运维分析 | Yes |
| 12 | 非功能性分析 | Yes |
| 13 | 系统间关系和影响 | Yes |
| 14 | LDC分析 | For LDC systems |
| 15 | 适用的标准 | Optional |

### Step 3: Check Quality

For each section, verify:

**Section 2 (项目整体分析):**
- [ ] Functional requirements list with priorities
- [ ] System architecture description
- [ ] Interface list with parameters
- [ ] Technology stack identified
- [ ] Dependency analysis complete

**Section 3 (数据库设计):**
- [ ] Table structure defined
- [ ] Naming conventions followed
- [ ] Index design included
- [ ] Data migration plan (if applicable)
- [ ] Data compatibility tests (if applicable)

**Section 4 (业务分析):**
- [ ] Business use cases documented
- [ ] System use cases with input/output
- [ ] Test case designs included

**Section 8 (稳定性分析):**
- [ ] Single point of failure analysis
- [ ] Fault isolation design
- [ ] Service degradation design

**Section 9 (资损风险分析):**
- [ ] Risk list complete
- [ ] Prevention measures defined
- [ ] Test cases for risk scenarios

**Section 10 (安全风险分析):**
- [ ] Security product usage reviewed
- [ ] Sensitive data identified
- [ ] Security design checklist completed

### Step 4: Generate Report

Create a review report with:
- Completeness score
- Quality issues by section
- Missing sections
- Recommendations for improvement

## Output Requirements

- **Format:** Markdown document
- **Language:** Chinese
- **Content:** Detailed review with actionable recommendations

## Review Report Template

```markdown
# 系统分析文档审查报告

## 文档信息
- 项目名称: [名称]
- 审查日期: [日期]
- 完整性评分: [X/15]

## 完整性检查

### 已完成 sections
| Section | Status |
|---------|--------|
| 1. 概述 | ✅/❌ |
| 2. 项目整体分析 | ✅/❌ |
| ... | ... |

### 缺失 sections
- [ ] Section X: 名称

## 质量问题

### Section X
- 问题1描述
- 问题2描述

## 建议

### 高优先级
1. 建议1
2. 建议2

### 中优先级
...

### 低优先级
...
```
