# Design References — Usage Guide

This directory contains 58 design system references extracted from real-world product websites. Use them when the user asks for UI, web design, landing pages, or any visual work.

## When to Use

- Building landing pages, marketing sites, dashboards, or product UI
- User says "make it look like X" or "reference Y's style"
- User asks for design without specifying a style — consult `catalog.md` to recommend one

## Workflow

1. **Read `catalog.md` first** — it contains a compact summary of all 56 design systems (colors, fonts, key traits). This lets you understand the full palette of options without reading 56 files.

2. **Match to user's intent** — based on what the user is building, pick 1–3 systems from the catalog that fit best. Consider:
   - Product type (SaaS, e-commerce, developer tool, AI product, consumer app)
   - Mood (premium, playful, technical, warm, minimal, energetic)
   - Surface preference (light, dark, mixed)

3. **Read the specific `.md` file(s)** — load the full design system reference for the chosen style(s) to get detailed tokens, spacing, component rules, and Do's/Don'ts.

4. **Apply selectively** — you don't need to copy every rule. Extract the design tokens (colors, typography, spacing, radius, shadows) and apply them to the user's project. Adapt as needed.

## File Naming

- `catalog.md` — compact index of all 56 systems (read this first)
- `README.md` — human-readable category index with usage recommendations
- `[brand].md` — full design system reference for a specific brand
- `linear.app.md`, `mistral.ai.md`, etc. — brands with domain suffixes in their names

## Important Notes

- These references are **inspiration and token sources**, not rigid templates. Adapt to the user's actual content and constraints.
- Font substitutions are provided for each system (Google Fonts or system fonts). Use them when building self-contained HTML.
- Many systems use proprietary fonts; the suggested substitutes are close approximations.
- When in doubt between multiple styles, pick the one whose personality matches the user's product most closely.
