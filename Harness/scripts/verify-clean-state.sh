#!/bin/bash
# Clean State Verification Script
# Verifies that the project is in a clean, runnable state

ERRORS=0

echo "=== Clean State Verification ==="

# Check 1: No uncommitted changes (if git exists)
if [ -d ".git" ]; then
    echo "[1/6] Checking git status..."
    if [ -n "$(git status --porcelain)" ]; then
        echo "⚠️  WARNING: Uncommitted changes detected:"
        git status --short
    else
        echo "✓ No uncommitted changes"
    fi
fi

# Check 2: Tests pass (auto-detect language)
echo "[2/6] Running tests..."

# TypeScript/JavaScript
if [ -f "package.json" ] && grep -q '"test"' package.json; then
    if npm test --silent 2>/dev/null; then
        echo "✓ Tests pass (npm)"
    else
        echo "❌ TESTS FAILED (npm)"
        ERRORS=$((ERRORS + 1))
    fi
# Python
elif [ -f "pyproject.toml" ] || [ -f "pytest.ini" ]; then
    if command -v pytest &> /dev/null; then
        if pytest --quiet 2>/dev/null; then
            echo "✓ Tests pass (pytest)"
        else
            echo "❌ TESTS FAILED (pytest)"
            ERRORS=$((ERRORS + 1))
        fi
    fi
# Java (Maven)
elif [ -f "pom.xml" ]; then
    if command -v mvn &> /dev/null; then
        if mvn test -q 2>/dev/null; then
            echo "✓ Tests pass (Maven)"
        else
            echo "❌ TESTS FAILED (Maven)"
            ERRORS=$((ERRORS + 1))
        fi
    fi
# Java (Gradle)
elif [ -f "build.gradle" ] || [ -f "build.gradle.kts" ]; then
    if command -v gradle &> /dev/null; then
        if gradle test -q 2>/dev/null; then
            echo "✓ Tests pass (Gradle)"
        else
            echo "❌ TESTS FAILED (Gradle)"
            ERRORS=$((ERRORS + 1))
        fi
    fi
# Rust
elif [ -f "Cargo.toml" ]; then
    if command -v cargo &> /dev/null; then
        if cargo test --quiet 2>/dev/null; then
            echo "✓ Tests pass (cargo)"
        else
            echo "❌ TESTS FAILED (cargo)"
            ERRORS=$((ERRORS + 1))
        fi
    fi
# Go
elif [ -f "go.mod" ]; then
    if command -v go &> /dev/null; then
        if go test ./... 2>/dev/null; then
            echo "✓ Tests pass (go)"
        else
            echo "❌ TESTS FAILED (go)"
            ERRORS=$((ERRORS + 1))
        fi
    fi
fi

# Check 3: No lint errors
echo "[3/6] Checking linter..."

# ESLint (TypeScript/JavaScript)
if [ -f ".eslintrc.json" ] || [ -f ".eslintrc.js" ]; then
    if command -v eslint &> /dev/null; then
        if eslint --quiet . 2>/dev/null; then
            echo "✓ Lint passes (ESLint)"
        else
            echo "❌ LINT ERRORS (ESLint)"
            ERRORS=$((ERRORS + 1))
        fi
    fi
fi

# Ruff (Python)
if [ -f "pyproject.toml" ] || [ -f "ruff.toml" ]; then
    if command -v ruff &> /dev/null; then
        if ruff check . 2>/dev/null; then
            echo "✓ Lint passes (Ruff)"
        else
            echo "❌ LINT ERRORS (Ruff)"
            ERRORS=$((ERRORS + 1))
        fi
    fi
fi

# Checkstyle (Java)
if [ -f "checkstyle.xml" ]; then
    if command -v mvn &> /dev/null; then
        if mvn checkstyle:check -q 2>/dev/null; then
            echo "✓ Lint passes (Checkstyle)"
        else
            echo "❌ LINT ERRORS (Checkstyle)"
            ERRORS=$((ERRORS + 1))
        fi
    fi
fi

# Clippy (Rust)
if [ -f "Cargo.toml" ]; then
    if command -v cargo &> /dev/null; then
        if cargo clippy -- -D warnings 2>/dev/null; then
            echo "✓ Lint passes (clippy)"
        else
            echo "❌ LINT ERRORS (clippy)"
            ERRORS=$((ERRORS + 1))
        fi
    fi
fi

# golangci-lint (Go)
if [ -f ".golangci.yml" ] || [ -f ".golangci.yaml" ]; then
    if command -v golangci-lint &> /dev/null; then
        if golangci-lint run 2>/dev/null; then
            echo "✓ Lint passes (golangci-lint)"
        else
            echo "❌ LINT ERRORS (golangci-lint)"
            ERRORS=$((ERRORS + 1))
        fi
    fi
fi

# Check 4: Build succeeds
echo "[4/6] Checking build..."

# TypeScript/JavaScript
if [ -f "package.json" ] && grep -q '"build"' package.json; then
    if npm run build --silent 2>/dev/null; then
        echo "✓ Build succeeds (npm)"
    else
        echo "❌ BUILD FAILED (npm)"
        ERRORS=$((ERRORS + 1))
    fi
# Python
elif [ -f "pyproject.toml" ]; then
    if command -v python &> /dev/null; then
        if python -m py_compile . 2>/dev/null; then
            echo "✓ Build succeeds (python)"
        else
            echo "❌ BUILD FAILED (python)"
            ERRORS=$((ERRORS + 1))
        fi
    fi
# Java (Maven)
elif [ -f "pom.xml" ]; then
    if command -v mvn &> /dev/null; then
        if mvn package -DskipTests -q 2>/dev/null; then
            echo "✓ Build succeeds (Maven)"
        else
            echo "❌ BUILD FAILED (Maven)"
            ERRORS=$((ERRORS + 1))
        fi
    fi
# Java (Gradle)
elif [ -f "build.gradle" ] || [ -f "build.gradle.kts" ]; then
    if command -v gradle &> /dev/null; then
        if gradle build -x test -q 2>/dev/null; then
            echo "✓ Build succeeds (Gradle)"
        else
            echo "❌ BUILD FAILED (Gradle)"
            ERRORS=$((ERRORS + 1))
        fi
    fi
# Rust
elif [ -f "Cargo.toml" ]; then
    if command -v cargo &> /dev/null; then
        if cargo build --quiet 2>/dev/null; then
            echo "✓ Build succeeds (cargo)"
        else
            echo "❌ BUILD FAILED (cargo)"
            ERRORS=$((ERRORS + 1))
        fi
    fi
# Go
elif [ -f "go.mod" ]; then
    if command -v go &> /dev/null; then
        if go build ./... 2>/dev/null; then
            echo "✓ Build succeeds (go)"
        else
            echo "❌ BUILD FAILED (go)"
            ERRORS=$((ERRORS + 1))
        fi
    fi
fi

# Check 5: No temporary files
echo "[5/6] Checking for temp files..."
TEMP_FILES=$(find . -maxdepth 2 -name "*.tmp" -o -name "*.bak" -o -name "*~" 2>/dev/null | grep -v node_modules | grep -v .git || true)
if [ -n "$TEMP_FILES" ]; then
    echo "⚠️  Temporary files found:"
    echo "$TEMP_FILES"
else
    echo "✓ No temp files"
fi

# Check 6: No broken symlinks
echo "[6/6] Checking for broken symlinks..."
BROKEN_LINKS=$(find . -maxdepth 2 -type l ! -exec test -e {} \; -print 2>/dev/null | grep -v node_modules | grep -v .git || true)
if [ -n "$BROKEN_LINKS" ]; then
    echo "⚠️  Broken symlinks found:"
    echo "$BROKEN_LINKS"
else
    echo "✓ No broken symlinks"
fi

echo ""
if [ $ERRORS -gt 0 ]; then
    echo "❌ FAILED: $ERRORS issue(s) detected"
    exit 1
else
    echo "✓ PASSED: Clean state verified"
fi

echo "=== Verification Complete ==="
