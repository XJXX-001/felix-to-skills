---
name: Felix-Agent
description: |
  Behavioral guidelines to reduce common LLM coding and execution mistakes, derived from Andrej Karpathy's observations,
  combined with disciplined git workflow and agent execution practices. Use when writing, reviewing, refactoring, or debugging code,
  or when designing multi-step agent workflows, CLI integrations, and stateful task execution —
  to avoid overcomplication, make surgical changes, surface assumptions before implementing,
  define verifiable success criteria, prefer deterministic tooling over manual steps, and keep every change manageable.
  Triggers: coding best practices, code review, simplify code, surgical edit, think before coding,
  goal-driven development, avoid overengineering, Karpathy guidelines, LLM coding pitfalls,
  git workflow, commit discipline, branching strategy, atomic commits, agent workflow, CLI tool,
  state management, resume task, deterministic execution, batch operation, tool discovery.
category: engineering
---

# Engineering Discipline

Behavioral guidelines to reduce common LLM coding mistakes, derived from [Andrej Karpathy's observations](https://x.com/karpathy/status/2015883857489522876) on LLM coding pitfalls, combined with disciplined version control practices.

**Tradeoff:** These guidelines bias toward caution over speed. For trivial tasks, use judgment.

Engineering discipline has three layers:
- **Mindset** (how to think) — the four Karpathy principles
- **Coding Execution** (how to code) — git workflow that makes every change reviewable, reversible, and verifiable
- **Agent Execution** (how to run) — deterministic tooling, workflow design, and state management that make multi-step tasks reliable and resumable

---

## 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them — don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

### Git Mapping: Plan the Change Before the Code

Before writing any code, know how it will flow through version control:

- **Scope the branch:** Will this fit in one short-lived branch (1-3 days), or should it split?
- **Estimate commits:** A feature that needs 5+ logical commits might be two features.
- **Name the branch upfront:** `feature/user-export` not `feature/stuff`.

---

## 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

### Git Mapping: Small Changes, Small Commits

- **Commit each successful increment.** Don't accumulate 300+ uncommitted lines.
- **Target ~100 lines per commit/PR.** Over ~1000 lines → split.
- **A large diff is a smell.** If the code is simple, the diff should be small.

---

## 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it — don't delete it.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

The test: Every changed line should trace directly to the user's request.

### Git Mapping: Separate Concerns at Commit Time

- **Formatting changes → their own commit.** Never mix `prettier --write` with behavior changes.
- **Refactoring → its own commit (or PR).** `refactor: extract validation logic` then `feat: add phone validation`.
- **Use Change Summaries** after every modification:

```
CHANGES MADE:
- src/routes/tasks.ts: Added validation middleware to POST endpoint
- src/lib/validation.ts: Added TaskCreateSchema using Zod

THINGS I DIDN'T TOUCH (intentionally):
- src/routes/auth.ts: Has similar validation gap but out of scope

POTENTIAL CONCERNS:
- The Zod schema is strict — rejects extra fields. Confirm this is desired.
```

---

## 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:

```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria let you loop independently. Weak criteria ("make it work") require constant clarification.

### Git Mapping: The Save Point Pattern

Every successful increment gets committed. Git is your safety net:

```
Agent starts work
 │
 ├── Makes a change
 │ ├── Test passes? → git commit → Continue
 │ └── Test fails? → git reset --hard HEAD → Investigate
 │
 ├── Makes another change
 │ ├── Test passes? → git commit → Continue
 │ └── Test fails? → git reset --hard HEAD → Investigate
 │
 └── Feature complete → All commits form a clean, reviewable history
```

**Pre-Commit Hygiene (automate with husky + lint-staged):**

```bash
# 1. Review what you're about to commit
git diff --staged

# 2. Scan for secrets
git diff --staged | grep -i "password\|secret\|api_key\|token"

# 3. Run tests, lint, type check
npm test && npm run lint && npx tsc --noEmit
```

---

## 5. Agent Execution Discipline

As an Agent, you are not just a code author — you are a task executor. These guidelines ensure reliability and reproducibility in complex, multi-step, and cross-session tasks.

### 5.1 Deterministic Operations: Prefer Tools and Scripts

**Never substitute manual steps where a deterministic tool exists.**

When a task involves automatable, deterministic operations:
- **Call scripts/tools first**, not manual line-by-line execution. Batch file operations → write a bash script. Batch data transformation → use Python. Avoid modifying files one by one.
- **Emit structured instructions; consume structured responses.** When calling external APIs, construct explicit request bodies. When parsing results, extract structured data rather than relying on fuzzy matching.
- **Standardize errors.** On tool failure, parse error codes and messages. Classify the response (retry, degrade, abort). Never silently ignore or vaguely summarize.

> **Rule of thumb**: If an operation repeats 10+ times or involves precise format validation, script it. Do not "just do it manually step by step."

### 5.2 Complex Tasks: Decompose, Gate, and Flow

**Multi-step tasks must have clear workflow and data flow.**

When facing complex tasks:

1. **Decompose**: Break into atomic steps. Each step has a single responsibility.
2. **Gate**: Define explicit completion criteria per step (output schema, validation rules, pass/fail condition).
3. **Flow**: Pass data between steps via explicit mechanisms (files, variables, structured output). Do not rely on implicit context.

```
Execution Plan Example:
1. [Gather info] → Output: info.json (with schema validation)
   Gate: info.json exists and all required fields are present
2. [Create resource] → Input: info.json, Output: result.json
   Gate: API returns status=success
3. [Configure linkage] → Input: result.json
   Gate: Linkage query verifies success
```

### 5.3 State Management: Persist, Resume, and Audit

**Long tasks must leave traces.**

For tasks that may span sessions or take significant time:
- **Persist progress**: Write current step, intermediate results, and key variables to a `.state` file or project state directory.
- **Resume from break**: Design tasks with `--resume` capability — check existing state, continue from the breakpoint, never restart from scratch blindly.
- **Audit**: Keep an operation log (timestamp, input, output, error) for future debugging.

> **Cross-session rule**: If a task is expected to need multiple interactions, persist progress to a file before ending the first interaction. On the next start, read state first, then decide where to resume.

### 5.4 Reuse and Extend: Discover Before Inventing

**Do not reinvent wheels.**

- **Hot discovery**: Before executing a new task, check if existing tools, scripts, skills, or templates are already available in the environment.
- **Workflows as files**: If a process recurs, solidify it as a reusable script/template/config in a project convention location (e.g., `scripts/`, `workflows/`).
- **Meta-programming**: When you need "another one of these," write a generator instead of manual copying. E.g., generate form validation code from a schema rather than hand-writing each instance.

### 5.5 Interaction and Execution Pitfalls

**Control complexity; defend against failure.**

| Principle | Execution Standard |
|-----------|-------------------|
| **Nesting limit** | Logic nesting does not exceed 3 levels. Beyond that, extract sub-functions or sub-steps. |
| **Timeout & retry** | Automated operations (network requests, script execution) must include timeout and retry. Never assume one-shot success. |
| **Field control** | When requesting info from the user or emitting intermediate results, keep 3-5 core fields. Split into batches if more. |
| **Explicit failure** | On failure, return explicit error details. Never silently ignore or return "something seems wrong." |

---

## 6. Git Execution Discipline

### Trunk-Based Development (Recommended)

Keep `main` always deployable. Work in short-lived feature branches that merge back within 1-3 days.

```
main ──●──●──●──●──●──●──●──●──●── (always deployable)
 ╲ ╱ ╲ ╱
 ●──●─╱ ●──╱ ← short-lived feature branches (1-3 days)
```

- **Dev branches are costs.** Every day a branch lives, it accumulates merge risk.
- **Feature flags > long branches.** Deploy incomplete work behind flags rather than keeping it on a branch for weeks.

### Atomic Commits

Each commit does one logical thing:

```bash
# Good
git log --oneline
a1b2c3d feat: add task creation endpoint with validation
d4e5f6g feat: add task creation form component
h7i8j9k feat: connect form to API and add loading state
m1n2o3p test: add task creation tests (unit + integration)

# Bad
git log --oneline
x1y2z3a Add task feature, fix sidebar, update deps, refactor utils
```

### Descriptive Messages

Commit messages explain the *why*, not just the *what*:

```
feat: add email validation to registration endpoint

Prevents invalid email formats from reaching the database.
Uses Zod schema validation at the route handler level,
consistent with existing validation patterns in auth.ts.
```

**Format:** `<type>: <subject>` then optional body.

**Types:** `feat` | `fix` | `refactor` | `test` | `docs` | `chore`

### Branch Naming

```
feature/task-creation
fix/duplicate-tasks
chore/update-deps
refactor/auth-module
```

### Working with Worktrees

For parallel agent work, run multiple branches simultaneously:

```bash
git worktree add ../project-feature-a feature/task-creation
git worktree add ../project-feature-b feature/user-settings
# Each directory has its own branch — no switching needed
git worktree remove ../project-feature-a
```

### Handling Generated Files

- **Commit:** `package-lock.json`, Prisma migrations (if project expects them)
- **Never commit:** `node_modules/`, `dist/`, `.env`, `.env.local`, build artifacts
- **Always have `.gitignore`** covering standard exclusions

### Using Git for Debugging

```bash
# Find which commit introduced a bug
git bisect start && git bisect bad HEAD && git bisect good <hash>

# View recent changes
git log --oneline -20
git diff HEAD~5..HEAD -- src/

# Who last changed this line?
git blame src/services/task.ts
```

---

## Common Rationalizations

| Rationalization | Reality |
|-----------------|---------|
| "Accessibility is a nice-to-have" | It's a legal requirement and an engineering quality standard. |
| "The message doesn't matter" | Commit messages are documentation. Future you will need them. |
| "I'll squash it all later" | Squashing destroys the development narrative. Clean commits from the start. |
| "Branches add overhead" | Short-lived branches are free. Long-lived branches (3+ days) are the hidden cost. |
| "I'll commit when the feature is done" | One giant commit is impossible to review, debug, or revert. |
| "I'll split this change later" | Large changes are harder to review and riskier. Split before submitting. |
| "The AI aesthetic is fine for now" | It signals low quality. Use the project's actual design system from the start. |
| "Doing it manually is faster this time" | Manual steps are not reproducible and accumulate error. Script anything that repeats. |
| "The state is in my context window" | Context windows are lost on restart. Persist state to files for cross-session reliability. |
| "I'll just copy-paste and tweak" | Copy-paste creates drift. Use generators or templates for recurring patterns. |

## Red Flags

- Components with more than 200 lines
- Inline styles or arbitrary pixel values
- Missing error/loading/empty states
- Large uncommitted changes accumulating
- Commit messages like "fix", "update", "misc"
- Formatting changes mixed with behavior changes in the same commit
- No `.gitignore` in the project
- Long-lived branches diverging from main
- Force-pushing to shared branches
- Color as the sole indicator of state (red/green without text or icons)
- Repeated manual file edits when a script could do it
- No `.state` or progress file for multi-step tasks
- Silent swallowing of tool/CLI errors
- Logic nesting beyond 3 levels without extraction
- One-shot network/API calls without timeout/retry
- Re-inventing a utility that already exists in the project

## Verification

After building UI or making any code change:

- [ ] Component renders without console errors / Code passes tests
- [ ] All interactive elements are keyboard accessible
- [ ] Screen reader can convey content and structure
- [ ] Responsive: works at 320px, 768px, 1024px, 1440px
- [ ] Loading, error, and empty states all handled
- [ ] Follows the project's design system (spacing, colors, typography)
- [ ] Commit does one logical thing with a descriptive message
- [ ] No secrets in the diff
- [ ] No formatting-only changes mixed with behavior changes
- [ ] `.gitignore` covers standard exclusions
- [ ] Deterministic operations use scripts/tools, not manual steps
- [ ] Multi-step tasks have explicit plan with per-step gates
- [ ] Progress persisted to file for long or cross-session tasks
- [ ] Tool/CLI errors are parsed and handled explicitly, not silently ignored
- [ ] Recurring patterns use generators/templates rather than copy-paste
- [ ] Network/API calls have timeout and retry

**These guidelines are working if:** fewer unnecessary changes in diffs, fewer rewrites due to overcomplication, clarifying questions come before implementation, and every commit is a clean, reviewable save point.

For detailed code examples of each principle, see [references/examples.md](references/examples.md).
For detailed git workflow patterns, see [references/git-workflow.md](references/git-workflow.md).
