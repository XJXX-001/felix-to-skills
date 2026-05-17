# Felix-Agent — Detailed Examples

Real-world code examples demonstrating the three layers of discipline. Each example shows what LLMs commonly do wrong and how to fix it.

---

## 1. Think Before Coding

### Example: Hidden Assumptions

**User Request:** "Add a feature to export user data"

**❌ What LLMs Do (Wrong Assumptions)**

```python
def export_users(format="json"):
    """Export all users to a file."""
    users = User.query.all()
    if format == "json":
        with open("users.json", "w") as f:
            json.dump([u.to_dict() for u in users], f)
    elif format == "csv":
        with open("users.csv", "w") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "email", "name"])
            writer.writeheader()
            writer.writerows([u.to_dict() for u in users])
    return f"Exported {len(users)} users"
```

**Problems:** Assumed export ALL users (pagination? privacy?), assumed file location, assumed fields, assumed CSV fieldnames.

**✅ What Should Happen (Surface Assumptions)**

```
Before implementing, I need to clarify:
1. Scope: Export all users or filtered subset? (privacy implications)
2. Format: Download in browser / background job / API endpoint?
3. Fields: Which user fields? (some might be sensitive)
4. Volume: How many users typically? (affects approach)
Simplest approach: Add an API endpoint that returns paginated JSON.
```

### Example: Multiple Interpretations

**User Request:** "Make the search faster"

**❌ What LLMs Do (Pick Silently)** — Adds caching, database indexes, and async processing without asking.

**✅ What Should Happen** — Present options: (1) Faster response time (2) More concurrent searches (3) Faster perceived speed. Ask which matters most.

---

## 2. Simplicity First

### Example: Over-abstraction

**User Request:** "Add a function to calculate discount"

**❌ What LLMs Do** — Strategy pattern, abstract base classes, DiscountConfig dataclass, 50+ lines.

**✅ What Should Happen**

```python
def calculate_discount(amount: float, percent: float) -> float:
    """Calculate discount amount. percent should be 0-100."""
    return amount * (percent / 100)
```

Add complexity only when you actually need multiple discount types.

### Example: Speculative Features

**User Request:** "Save user preferences to database"

**❌ What LLMs Do** — PreferenceManager class with caching, validation, merging, notifications (100+ lines).

**✅ What Should Happen**

```python
def save_preferences(db, user_id: int, preferences: dict):
    """Save user preferences to database."""
    db.execute(
        "UPDATE users SET preferences = ? WHERE id = ?",
        (json.dumps(preferences), user_id)
    )
```

Add caching, validation, merging later when needed.

---

## 3. Surgical Changes

### Example: Drive-by Refactoring

**User Request:** "Fix the bug where empty emails crash the validator"

**❌ What LLMs Do** — "Improved" email validation beyond the bug fix, added username validation nobody asked for, changed comments, added docstring.

**✅ What Should Happen** — Only change the specific lines that fix empty email handling. Do not touch unrelated code.

### Example: Style Drift

**User Request:** "Add logging to the upload function"

**❌ What LLMs Do** — Changed quote style, added type hints, added docstring, reformatted whitespace, changed boolean return logic.

**✅ What Should Happen** — Match existing style (single quotes, no type hints, existing boolean pattern). Only add logging lines.

---

## 4. Goal-Driven Execution

### Example: Vague vs. Verifiable

**User Request:** "Fix the authentication system"

**❌ What LLMs Do** — "I'll review the code, identify issues, make improvements, test changes." No clear success criteria.

**✅ What Should Happen**

```
If the issue is "users stay logged in after password change":
1. Write test: Change password → verify old session invalidated → Verify: Test fails (reproduces bug)
2. Implement: Invalidate sessions on password change → Verify: Test passes
3. Check edge cases → Verify: Additional tests pass
4. Verify no regression → Verify: Full test suite green
```

### Example: Incremental with Verification

**User Request:** "Add rate limiting to the API"

**✅ What Should Happen** — Break into verifiable steps:
1. Add basic in-memory rate limiting (single endpoint) → Verify: 11 requests → first 10 succeed, 11th gets 429
2. Extract to middleware → Verify: Rate limits apply to all endpoints, existing tests pass
3. Add Redis backend → Verify: Rate limit persists across restarts
4. Add per-endpoint configuration → Verify: Different rates for different endpoints

---

## 5. Agent Execution Discipline

### Example: Manual Steps vs. Deterministic Scripts

**User Request:** "Rename all 50 component files from `.jsx` to `.tsx`"

**❌ What LLMs Do (Manual Line-by-Line)**

```
I'll rename each file one by one...
- src/components/Button.jsx → Button.tsx
- src/components/Card.jsx → Card.tsx
... (48 more lines)
```

**Problems:** Tedious, error-prone, not reproducible, no audit trail.

**✅ What Should Happen (Script First)**

```bash
find src/components -name "*.jsx" -exec bash -c 'mv "$1" "${1%.jsx}.tsx"' _ {} \;
# Verify: find src/components -name "*.tsx" | wc -l → 50
git add -A && git commit -m "refactor: migrate all components to .tsx"
```

> **Rule of thumb**: If it repeats 10+ times, script it.

---

### Example: Missing State Persistence

**User Request:** "Process this 10,000-row CSV and generate reports"

**❌ What LLMs Do (All in Memory)**

Process all 10,000 rows in one go. If interrupted or context-compacted, start from scratch. No record of which rows were already processed.

**✅ What Should Happen (Persist, Resume, Audit)**

```python
import json, os

STATE_FILE = ".state.processing"

def load_state():
    if os.path.exists(STATE_FILE):
        return json.load(open(STATE_FILE))
    return {"processed": 0, "failed": [], "outputs": []}

def save_state(state):
    json.dump(state, open(STATE_FILE, "w"), indent=2)

state = load_state()
for i, row in enumerate(csv_rows[state["processed"]:], start=state["processed"]):
    try:
        result = process(row)
        state["outputs"].append(result)
        state["processed"] += 1
        if i % 100 == 0:
            save_state(state)  # Checkpoint every 100 rows
    except Exception as e:
        state["failed"].append({"row": i, "error": str(e)})
        save_state(state)

# On next run: checks .state, resumes from last checkpoint
```

---

### Example: Complex Task Without Decomposition

**User Request:** "Set up a new microservice with auth, database, and API"

**❌ What LLMs Do (Monolithic Execution)**

Attempts to create all files, configure everything, and wire them together in one shot. When something fails, rolls back everything or leaves the project in a broken state.

**✅ What Should Happen (Decompose, Gate, Flow)**

```
Execution Plan:
1. [Scaffold project] → Output: project/ directory with package.json, tsconfig.json
   Gate: `npm install` succeeds with zero errors

2. [Add database layer] → Input: project/, Output: src/db/schema.ts, src/db/client.ts
   Gate: `npx prisma migrate dev` succeeds; test connection returns `pong`

3. [Add auth middleware] → Input: project/ + db layer, Output: src/middleware/auth.ts
   Gate: Unit test: valid token → 200, invalid token → 401

4. [Add API routes] → Input: project/ + db + auth, Output: src/routes/*.ts
   Gate: Integration test: full request round-trip succeeds

5. [Wire together] → Input: all above, Output: src/app.ts
   Gate: `npm run dev` starts without errors; health check endpoint returns 200
```

Each step has a clear input, output, and gate. If step 3 fails, steps 1-2 are still valid and don't need re-execution.

---

### Example: Reinventing Existing Tools

**User Request:** "Parse this JSON config file and validate the schema"

**❌ What LLMs Do (Hand-rolled Parser)**

Write a custom regex-based JSON parser with manual field validation — 80+ lines, brittle, untested.

**✅ What Should Happen (Discover Before Inventing)**

```python
import json
from pydantic import BaseModel, ValidationError

class Config(BaseModel):
    host: str
    port: int
    debug: bool = False

# One-liner parsing + validation
config = Config(**json.load(open("config.json")))
```

Check environment first: `jq`, `python -m json.tool`, Pydantic, Zod — use what exists.

## Anti-Patterns Summary

| Principle | Anti-Pattern | Fix |
|-----------|-------------|-----|
| Think Before Coding | Silently assumes format/fields/scope | List assumptions, ask for clarification |
| Simplicity First | Strategy pattern for single calculation | One function until complexity is actually needed |
| Surgical Changes | Reformats quotes, adds type hints while fixing bug | Only change lines that fix the reported issue |
| Goal-Driven | "I'll review and improve the code" | "Write test for bug X → make it pass → verify no regressions" |
| Deterministic Operations | Manual line-by-line for batch tasks | Script it: `find`, `sed`, `jq`, Python — anything repeatable |
| State Management | All-in-memory processing | Write `.state` checkpoints; design for `--resume` |
| Task Decomposition | Monolithic "do everything at once" | Atomic steps with explicit gates and data flow |
| Reuse & Extend | Hand-rolling parsers/validators | Check existing tools/skills first; use Pydantic/Zod/jq |

**Key Insight:** The "overcomplicated" examples are not obviously wrong — they follow design patterns. The problem is **timing**: adding complexity before it's needed. Good code solves today's problem simply, not tomorrow's problem prematurely. Good execution uses tools before muscle, checkpoints before memory, and decomposition before monoliths.
