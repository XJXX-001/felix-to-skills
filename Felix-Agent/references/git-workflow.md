# Git Workflow — Detailed Reference

Complete git workflow patterns for AI agents and engineering teams.

Part of the [Felix-Agent](../SKILL.md) skill — Coding Execution layer.

---

## Commit Message Format

```
<type>: <subject>

<body>  (optional — explains WHY, not WHAT)

<footer> (optional — references issues, breaking changes)
```

**Types:**

| Type | Use When |
|------|----------|
| `feat` | New feature or capability |
| `fix` | Bug fix |
| `refactor` | Code change that neither fixes a bug nor adds a feature |
| `test` | Adding or updating tests |
| `docs` | Documentation only |
| `chore` | Tooling, dependencies, config |

**Examples:**

```bash
# Good — explains intent
feat: add email validation to registration endpoint

Prevents invalid email formats from reaching the database.
Uses Zod schema validation at the route handler level,
consistent with existing validation patterns in auth.ts.

# Bad — obvious from diff
update auth.ts

# Bad — mixed concerns
refactor validation and add phone number field
```

---

## Change Summary Template

After any modification, provide this structured summary:

```
CHANGES MADE:
- src/routes/tasks.ts: Added validation middleware to POST endpoint
- src/lib/validation.ts: Added TaskCreateSchema using Zod

THINGS I DIDN'T TOUCH (intentionally):
- src/routes/auth.ts: Has similar validation gap but out of scope
- src/middleware/error.ts: Error format could be improved (separate task)

POTENTIAL CONCERNS:
- The Zod schema is strict — rejects extra fields. Confirm this is desired.
- Added zod as a dependency (72KB gzipped) — already in package.json
```

---

## Pre-Commit Checklist

```bash
# 1. Review what you're about to commit
git diff --staged

# 2. Scan for secrets
git diff --staged | grep -i "password\|secret\|api_key\|token"

# 3. Run tests
npm test

# 4. Run linting
npm run lint

# 5. Run type checking
npx tsc --noEmit
```

**Automate with husky + lint-staged:**

```json
// package.json
{
  "lint-staged": {
    "*.{ts,tsx}": ["eslint --fix", "prettier --write"],
    "*.{json,md}": ["prettier --write"]
  }
}
```

---

## Worktree Workflow for Parallel Agents

```bash
# 1. Create worktrees for parallel feature work
git worktree add ../project-feature-a feature/task-creation
git worktree add ../project-feature-b feature/user-settings

# 2. Each agent works in its own directory
ls ../
# project/              ← main branch
# project-feature-a/    ← task-creation branch
# project-feature-b/    ← user-settings branch

# 3. Clean up when done
git worktree remove ../project-feature-a
```

---

## Debugging with Git

```bash
# Find which commit introduced a bug
git bisect start
git bisect bad HEAD
git bisect good <commit-hash>
# Git checkouts midpoints; run your test at each step

# View what changed recently
git log --oneline -20
git diff HEAD~5..HEAD -- src/

# Find who last changed a specific line
git blame src/services/task.ts

# Search commit messages
git log --grep="validation" --oneline

# View file history
git log --follow -p -- src/services/task.ts
```

---

## Branch Strategy Quick Reference

```
main (always deployable)
 │
 ├── feature/task-creation      ← One feature per branch
 ├── feature/user-settings      ← Parallel work
 ├── fix/duplicate-tasks        ← Bug fixes
 └── refactor/auth-module       ← Refactoring
```

**Rules:**
- Branch from `main`
- Merge within 1-3 days
- Delete after merge
- Use feature flags for incomplete work, not long-lived branches

---

## File Handling Rules

| File | Action | Reason |
|------|--------|--------|
| `package-lock.json` | Commit | Reproducible installs |
| Prisma migrations | Commit | Database state tracking |
| `dist/`, `.next/` | Ignore | Build output |
| `.env`, `.env.local` | Ignore | Secrets |
| `node_modules/` | Ignore | Dependencies |
| `.vscode/settings.json` | Ignore unless shared | IDE config |

**Minimum `.gitignore`:**

```
node_modules/
dist/
.next/
.env
.env.local
*.pem
.DS_Store
```
