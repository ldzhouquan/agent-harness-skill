# GenerateTemplate Workflow

This workflow generates specific section templates for the system analysis document.

## Input

User should specify:
- Which section(s) they need templates for
- Optional: specific focus areas or customizations

## Process

### Step 1: Determine Template Type

Based on user input, identify which template(s) to generate:

| Template | Section | Description |
|----------|---------|-------------|
| Overview | Section 1 | Project background, goals |
| Project Overall | Section 2 | Functional requirements, architecture |
| Database | Section 3 | Table design, data migration |
| Business | Section 4 | Business use cases, system use cases |
| Existing System Impact | Section 5 | Impact analysis |
| Data Analysis Impact | Section 6 | Data warehouse impact |
| Test Strategy | Section 7 | Testing approach |
| Stability | Section 8 | SPOF, fault isolation |
| Financial Risk | Section 9 | Risk analysis, prevention |
| Security | Section 10 | Security analysis |
| Operations | Section 11 | Monitoring, release |
| Non-functional | Section 12 | Performance, concurrency |
| Inter-system | Section 13 | System relationships |
| LDC | Section 14 | LDC deployment |
| Standards | Section 15 | Applicable standards |

### Step 2: Load Templates

Load the Templates.md file to get the relevant section template:

```markdown
SkillSearch('systemanalysis templates')
```

### Step 3: Generate Template

Extract the specific section template requested and customize it if needed.

### Step 4: Provide Guidance

Add guidance on:
- What to include in each section
- Common pitfalls to avoid
- Best practices

## Output Requirements

- **Format:** Markdown template
- **Language:** Chinese
- **Content:** Ready-to-use template with placeholders

## Common Templates

### Database Design Template

```markdown
## 3. 数据库设计

### 3.1 表结构设计

**涉及的数据库:** [数据库名]

**涉及的表:**

| 表名 | 说明 | 预估数据量 | 增长量/天 |
|------|------|------------|-----------|
| | | | |

**表结构详细设计:**

| 字段名 | 类型 | 说明 | 备注 |
|--------|------|------|------|
| | | | |

### 3.2 优化设计

**索引设计:**
| 索引名 | 表名 | 字段 | 类型 |
|--------|------|------|------|
| | | | |

**冗余设计:**
[说明]

**分区策略:**
[说明]

### 3.3 数据迁移设计

[迁移方案说明]

### 3.4 测试分析

[数据兼容性测试用例]
```

### Security Analysis Template

```markdown
## 10. 安全风险分析

### 10.1 安全产品的正确使用

| 安全产品 | 使用场景 | 配置说明 |
|----------|----------|----------|
| | | |

### 10.2 CTU监控的影响

**新增CTU事件:**

| 系统名称 | 事件属性 | CTU规则 | 测试关注点 |
|----------|----------|---------|------------|
| | | | |

### 10.3 业务和数据安全

**敏感数据清单:**

| 数据类型 | 存储方式 | 传输要求 | 备注 |
|----------|----------|----------|------|
| | | | |

**安全分析结果:**

| 序号 | 场景 | 风险描述 | 防控措施 |
|------|------|----------|----------|
| | | | |

### 10.4 内部管理安全

[内部安全管理措施]

### 10.5 安全设计规范

[安全设计checklist自评]
```
