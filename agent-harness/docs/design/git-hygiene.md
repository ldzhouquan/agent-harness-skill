# Git Hygiene: Commit Practices

Git is your memory. Use it well.

## Commit Frequency

**Commit early, commit often.**

Every meaningful change gets a commit:
- Feature implementation ✓
- Test addition ✓
- Bug fix ✓
- Documentation update ✓

## Commit Message Format

```
<type>: <description>

[Optional body]
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `test`: Adding/updating tests
- `docs`: Documentation
- `refactor`: Code restructuring
- `chore`: Build, tools, etc.

Examples:
```
feat: implement user login flow
fix: handle missing user.id in API response
test: add e2e test for new chat feature
docs: update progress.md for session 3
```

## Branch Strategy

### Simple Projects (Most Cases)

- Just use `main` branch
- Commit directly (clean state only!)
- Git revert if needed

### Larger Teams/Projects

- Short-lived feature branches
- Merge quickly (keep PRs small!)
- Delete branches after merge

## Git as Undo Button

If you mess up:

```bash
# Go back to last clean state
git reset --hard HEAD

# Or if you already committed
git revert HEAD
```

**Never** leave broken code uncommitted!

## What to Commit

- ✅ All source code
- ✅ Tests
- ✅ `features.json` updates
- ✅ `progress.md` updates
- ✅ Documentation

## What NOT to Commit

- ❌ `node_modules` / dependencies
- ❌ `.env` files with secrets
- ❌ Build artifacts
- ❌ IDE configs (VS Code, etc.)
- ❌ Temporary files

(Your `.gitignore` should handle these.)

## Git Log as Project Timeline

The git log should tell the story of the project.

Good log:
```
feat: setup project structure
feat: add user authentication
fix: handle expired tokens
test: add login tests
feat: implement chat feature
```

Bad log:
```
wip
more stuff
fix things
oops
```

---

*Git isn't just version control—it's the project's memory.*
