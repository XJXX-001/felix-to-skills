# Felix-Agent

Behavioral guidelines to reduce common LLM coding and execution mistakes, derived from [Andrej Karpathy's observations](https://x.com/karpathy/status/2015883857489522876) on LLM coding pitfalls, combined with disciplined git workflow and agent execution practices.

Adapted from [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills), expanded with Agent Execution Discipline.

**Compatible with:** Claude Code, Kimi Code, OpenCode, OpenClaw, Hermes Agent, and other CLI-based AI coding agents.

## Three Layers of Discipline

| Layer | Principle | Addresses |
|-------|-----------|-----------|
| Mindset | **Think Before Coding** | Wrong assumptions, hidden confusion, missing tradeoffs |
| Mindset | **Simplicity First** | Overcomplication, bloated abstractions |
| Mindset | **Surgical Changes** | Orthogonal edits, touching code you shouldn't |
| Mindset | **Goal-Driven Execution** | Tests-first approach, verifiable success criteria |
| Coding Execution | **Git Discipline** | Atomic commits, clean history, reviewable changes |
| Agent Execution | **Agent Execution Discipline** | Deterministic tooling, workflow design, state management, reuse before invention |

## Install

### SkillHub / CLI Agent (recommended)

```bash
skillhub install Felix-Agent
```

Or copy the entire `Felix-Agent` folder to your agent's skills directory:

```bash
# Kimi Code / OpenCode / Generic
mkdir -p ~/.config/agents/skills && cp -r Felix-Agent ~/.config/agents/skills/

# OpenClaw / qclaw
cp -r Felix-Agent ~/.qclaw/skills/

# Hermes
cp -r Felix-Agent ~/.hermes/skills/
```

## Structure

```
Felix-Agent/
├── SKILL.md                    # Core guidelines (4 principles + Agent Execution + Git discipline)
├── references/
│   ├── examples.md             # Detailed code examples (do/don't)
│   └── git-workflow.md         # Git patterns, commit format, worktrees
└── README.md                   # This file
```

## Key Insights

> "LLMs are exceptionally good at looping until they meet specific goals... Don't tell it what to do, give it success criteria and watch it go."

The "Goal-Driven Execution" principle captures this: transform imperative instructions into declarative goals with verification loops. Combined with git's save-point pattern, every increment becomes a safe, reversible step.

> "If an operation repeats 10+ times or involves precise format validation, script it. Do not 'just do it manually step by step.'"

The "Agent Execution Discipline" extends this from code to task execution: deterministic operations through tools/scripts, complex tasks decomposed into gated steps, state persisted for cross-session resumption, and existing capabilities discovered before reinventing.

## How to Know It's Working

- **Fewer unnecessary changes in diffs** — Only requested changes appear
- **Fewer rewrites due to overcomplication** — Code is simple the first time
- **Clarifying questions come before implementation** — Not after mistakes
- **Clean, minimal PRs** — No drive-by refactoring or "improvements"
- **Every commit is a clean save point** — Atomic, descriptive, reviewable
- **Batch operations use scripts/tools** — Not manual line-by-line execution
- **Cross-session tasks resume from `.state`** — Progress is never lost

## License

MIT
