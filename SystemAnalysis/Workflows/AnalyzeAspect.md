# AnalyzeAspect Workflow

This workflow performs in-depth analysis on a specific aspect of the system.

## Input

User should specify:
- The aspect to analyze (database, security, stability, risk, performance, etc.)
- The system or project context
- Any specific concerns or focus areas

## Process

### Step 1: Determine Analysis Aspect

Based on user input, identify which aspect to analyze:

| Aspect | Chinese | Section |
|--------|---------|---------|
| Database | 数据库设计 | Section 3 |
| Business | 业务分析 | Section 4 |
| Stability | 稳定性分析 | Section 8 |
| Financial Risk | 资损风险分析 | Section 9 |
| Security | 安全风险分析 | Section 10 |
| Operations | 运维分析 | Section 11 |
| Non-functional | 非功能性分析 | Section 12 |
| Inter-system | 系统间关系 | Section 13 |
| LDC | LDC分析 | Section 14 |

### Step 2: Load Relevant Template Section

Load Templates.md to get the specific template for the chosen aspect.

### Step 3: Perform Analysis

**Database Analysis (数据库设计):**
- Table structure review
- Naming convention compliance check
- Third normal form verification
- Index design analysis
- Data migration plan review
- Query optimization suggestions

**Security Analysis (安全风险分析):**
- Security product usage review
- CTU monitoring configuration
- Sensitive data protection
- Internal management security
- Security design checklist

**Stability Analysis (稳定性分析):**
- Single point of failure identification
- Data hot spot analysis
- Fault isolation capability
- Service degradation design
- Compatibility analysis

**Financial Risk Analysis (资损风险分析):**
- Risk identification
- Prevention measure review
- Concurrent control analysis
- Data consistency verification

**Performance Analysis (性能分析):**
- Performance requirements review
- Bottleneck identification
- Caching strategy
- Database optimization
- Concurrency control

### Step 4: Output

Generate a detailed analysis report including:
- Current state assessment
- Issues and risks identified
- Recommendations
- Action items

## Output Requirements

- **Format:** Markdown document
- **Language:** Chinese
- **Content:** Detailed analysis with specific findings and recommendations
