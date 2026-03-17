# Engineering Toolchain Setup

Detailed toolchain recommendations. See [../modules/initialization.md](../modules/initialization.md) for the workflow overview.

---

## Linter & Formatter Toolchain

### JavaScript / TypeScript

| Tool | Purpose | Config File |
|------|---------|-------------|
| ESLint | Linting | `.eslintrc.json` |
| Prettier | Formatting | `.prettierrc` |
| eslint-plugin-import | Import order | Included in ESLint config |

**Recommended configs:**
- Airbnb ESLint Config (comprehensive)
- Standard ESLint Config (minimal)
- TypeScript ESLint Parser

**Command to add:**
```bash
npm init @eslint/config
```

---

### Python

| Tool | Purpose | Config File |
|------|---------|-------------|
| Ruff | Linting + Formatting | `pyproject.toml` |
| Black | Formatting (alternative) | `pyproject.toml` |
| Mypy | Type checking | `mypy.ini` |

**Command to add:**
```bash
pip install ruff black mypy
```

---

### Java

| Tool | Purpose | Config File |
|------|---------|-------------|
| Checkstyle | Linting | `checkstyle.xml` |
| PMD (Alibaba P3C) | Best practices | `rulesets/p3c.xml` |
| ArchUnit | Architecture enforcement | Java code |

**Reference:** [Alibaba P3C PMD](https://github.com/alibaba/p3c/tree/master/p3c-pmd)

---

### Go

| Tool | Purpose | Config File |
|------|---------|-------------|
| golangci-lint | All-in-one linter | `.golangci.yml` |

**Command to add:**
```bash
go install github.com/golangci/golangci-lint/cmd/golangci-lint@latest
```

---

## Test Framework Setup

### JavaScript / TypeScript

| Framework | Command |
|-----------|---------|
| Jest | `npm install --save-dev jest @types/jest ts-jest` |
| Vitest | `npm install --save-dev vitest` |

**Jest config (jest.config.js):**
```javascript
module.exports = {
  preset: 'ts-jest',
  testEnvironment: 'node',
  roots: ['<rootDir>/src'],
  testMatch: ['**/__tests__/**/*.ts'],
};
```

---

### Python

| Framework | Command |
|-----------|---------|
| pytest | `pip install pytest` |

**pytest config (pyproject.toml):**
```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = "test_*.py"
```

---

### Java

| Framework | Notes |
|-----------|-------|
| JUnit 5 | Already included in Maven/Gradle |

**Maven dependency (pom.xml):**
```xml
<dependency>
  <groupId>org.junit.jupiter</groupId>
  <artifactId>junit-jupiter</artifactId>
  <version>5.9.0</version>
  <scope>test</scope>
</dependency>
```

---

## CI Pipeline Templates

### GitHub Actions - TypeScript

Create `.github/workflows/ci.yml`:

```yaml
name: CI

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: npm ci
      - run: npm run lint || true
      - run: npm test
```

---

### GitHub Actions - Python

```yaml
name: CI

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install -e .
      - run: ruff check . || true
      - run: pytest
```

---

## Observability Setup

### Logs Directory

Create `logs/` directory and add to `.gitignore`:

```
# .gitignore
logs/
```

### Test Reporters

**Jest HTML Reporter:**
```bash
npm install --save-dev jest-html-reporter
```

**JUnit XML (for CI):**
```bash
npm install --save-dev jest-junit
```

### Logger Configuration

| Language | Logger |
|----------|--------|
| JS/TS | Winston, Pino |
| Python | Loguru, logging |
| Java | Log4j, SLF4J |
| Go | Zap, Logrus |

---

## Quick Start Commands

### TypeScript Project
```bash
npm init -y
npm install --save-dev typescript @types/node ts-jest jest eslint prettier
npx tsc --init
```

### Python Project
```bash
pip install ruff black mypy pytest
```
