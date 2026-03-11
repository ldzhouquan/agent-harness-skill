# CreateAnalysis Workflow

This workflow creates a comprehensive system analysis document.

## Input

User should provide:
- Project name
- Business background
- Technical background (new development vs. upgrade)
- Core business requirements
- Target system properties (performance, availability, etc.)

## Process

### Step 1: Collect Project Information

Ask the user to provide:
1. **Project name** - 项目名称
2. **Business background** - 业务背景描述
3. **Development type** - 全新产品 / 升级改造
4. **Core functions** - 核心功能列表
5. **System goals** - 系统目标 (性能、可用性等)

### Step 2: Load Templates

Load the Templates.md file to get the full template structure:

```markdown
SkillSearch('systemanalysis templates')
```

### Step 3: Generate Document

Create a comprehensive system analysis document with the following sections:

1. **概述 (Overview)**
   - Terminology definitions
   - Project background
   - Business and system goals

2. **项目整体分析 (Project Overall Analysis)**
   - Functional requirements list
   - System architecture
   - Interface design
   - Technology stack
   - Dependency analysis
   - Domain model

3. **数据库设计 (Database Design)**
   - Table structure design
   - Naming conventions
   - Optimization design
   - Data migration plan
   - Data compatibility tests

4. **业务分析 (Business Analysis)**
   - Business use cases
   - System use cases
   - Test case designs

5. **现有系统影响分析 (Existing System Impact Analysis)**
   - Impact on existing systems
   - Test focus areas

6. **数据分析影响 (Data Analysis Impact)**
   - Data warehouse boundary analysis
   - Impact on existing data analysis

7. **测试策略分析 (Test Strategy Analysis)**
   - Testability analysis
   - Overall test strategy

8. **稳定性分析 (Stability Analysis)**
   - Single point of failure analysis
   - Data hot spot analysis
   - Fault isolation analysis
   - Service degradation analysis

9. **资损风险分析 (Financial Loss Risk Analysis)**
   - Risk list
   - Prevention and control measures

10. **安全风险分析 (Security Risk Analysis)**
    - Security product usage
    - CTU monitoring
    - Business and data security
    - Internal management security

11. **运维分析 (Operations Analysis)**
    - Network/hardware impact
    - Release impact analysis
    - System monitoring
    - Business monitoring
    - Logging
    - Disaster recovery

12. **非功能性分析 (Non-functional Analysis)**
    - Error data correction
    - Performance analysis
    - Concurrency control
    - Fault tolerance

13. **系统间关系和影响 (Inter-system Relationships)**
    - External interface changes
    - Service changes
    - Dependency changes

14. **LDC分析 (LDC Analysis)**
    - RZone deployment analysis
    - Service call changes
    - Test focus areas

15. **适用的标准 (Applicable Standards)**

### Step 4: Output

Save the generated document to the user's project directory or output as markdown.

## Output Requirements

- **Format:** Markdown document
- **Language:** Chinese (based on the template)
- **Completeness:** All 15 sections should be present
- **Detail Level:** Appropriate for the project scope (P1 functions should have detailed analysis)
