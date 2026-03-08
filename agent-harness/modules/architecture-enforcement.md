# Module 5: Architecture Constraint Enforcement

↩️ [返回概览](../SKILL.md) | [查看工作流](../workflow.md) | [模块索引](../modules.md)

## Layered Architecture
- Each business domain divided into fixed layers
- From types layer to config layer, to data access layer, to service layer, to runtime layer, finally to interface layer
- Code can only depend forward, never backward

## Providers Pattern
- All public capabilities must enter through unified Providers entry
- Like building access control system - regardless of delivery or AC repair, must swipe card through main door
- Any other path, prohibited! CI directly red lights

## Implementation Guide: How to Config

**To enforce these rules, you MUST create actual configuration files.**

### For Java (Checkstyle/ArchUnit)
1.  **Create `checkstyle.xml`**: Import standard rules.
2.  **Setup ArchUnit Tests**: Write JUnit tests to enforce layering and naming rules.
    ```java
    @ArchTest
    public static final ArchRule no_access_to_controllers =
        noClasses().that().resideInAPackage("..service..")
            .should().dependOnClassesThat().resideInAPackage("..controller..");
    ```

### For TypeScript/JavaScript (ESLint)
1.  **Create `.eslintrc.js`**:
    ```javascript
    module.exports = {
      rules: {
        "no-restricted-imports": ["error", {
          "paths": ["aws-sdk"], // Enforce Provider pattern
          "message": "Please use StorageProvider instead of direct AWS SDK usage."
        }]
      }
    }
    ```
