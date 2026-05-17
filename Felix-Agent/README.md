# Engineering Discipline (OpenClaw Skill)

Behavioral guidelines to reduce common LLM coding mistakes, derived from [Andrej Karpathy's observations](https://x.com/karpathy/status/2015883857489522876) on LLM coding pitfalls, combined with disciplined git workflow practices.

Adapted from [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) for **OpenClaw**.

## The Four Principles + Git Execution

| Layer | Principle | Addresses |
|-------|-----------|-----------|
| Mindset | **Think Before Coding** | Wrong assumptions, hidden confusion, missing tradeoffs |
| Mindset | **Simplicity First** | Overcomplication, bloated abstractions |
| Mindset | **Surgical Changes** | Orthogonal edits, touching code you shouldn't |
| Mindset | **Goal-Driven Execution** | Tests-first approach, verifiable success criteria |
| Execution | **Git Discipline** | Atomic commits, clean history, reviewable changes |

## Install

### SkillHub (recommended)

```bash
skillhub install engineering-discipline
```

### Manual

Copy the entire `andrej-karpathy-skills` folder to your skills directory:

```bash
cp -r andrej-karpathy-skills ~/.qclaw/skills/
```

## Structure

```
andrej-karpathy-skills/
├── SKILL.md                    # Core guidelines (4 principles + git discipline)
├── references/
│   ├── examples.md             # Detailed code examples (do/don't)
│   └── git-workflow.md         # Git patterns, commit format, worktrees
└── README.md                   # This file
```

## Key Insight

> "LLMs are exceptionally good at looping until they meet specific goals... Don't tell it what to do, give it success criteria and watch it go."

The "Goal-Driven Execution" principle captures this: transform imperative instructions into declarative goals with verification loops. Combined with git's save-point pattern, every increment becomes a safe, reversible step.

## How to Know It's Working

- **Fewer unnecessary changes in diffs** — Only requested changes appear
- **Fewer rewrites due to overcomplication** — Code is simple the first time
- **Clarifying questions come before implementation** — Not after mistakes
- **Clean, minimal PRs** — No drive-by refactoring or "improvements"
- **Every commit is a clean save point** — Atomic, descriptive, reviewable

## License

MIT
