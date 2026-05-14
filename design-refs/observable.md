# Design System: Observable

> **Implementation Notes**
>
> The original site uses system-native fonts. For self-contained HTML output, use these CDN substitutes:
> - **Primary:** `Inter` | **Mono:** `JetBrains Mono` | **Serif (data labels):** `Lora`
> - **Font stack (CSS):** `font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;`
> - **Mono stack (CSS):** `font-family: 'JetBrains Mono', 'SF Mono', 'Fira Code', monospace;`
> ```html
> <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&family=Lora:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">
> ```
> Use standard file writing to create HTML. Serve via local server or deploy as needed.
> Verify visual accuracy in browser after generating.

## 1. Visual Theme & Atmosphere

Observable's interface is a gallery for data — a design philosophy where the canvas recedes entirely, leaving only the data to speak. The background is a clean, luminous white (`#ffffff`) with subtle cool-gray surfaces (`#f8f9fa`) that quietly define spatial zones without announcing themselves. There is no "brand color" in the traditional sense — the color comes exclusively from the data visualizations, which pop against the achromatic canvas like paintings on a white gallery wall.

The typography is understated and functional: system-native fonts with comfortable sizing that prioritizes readability over spectacle. Headings use weight 600 (SemiBold), body text sits at weight 400 (Regular), and data labels use a serif face (Lora) for a touch of editorial precision that distinguishes numeric callouts from UI text. Nothing shouts — the loudest element on any Observable page should be the data visualization, never the interface chrome.

This is the polar opposite of dark-themed, neon-accented analytics tools. Observable proves that data doesn't need darkness — it needs space. The generous whitespace, minimal borders, and nearly invisible UI chrome create a reading experience more akin to a scientific journal than a developer dashboard.

**Key Characteristics:**
- Luminous white canvas (#ffffff) with cool-gray zone surfaces (#f8f9fa) — data is the only color
- System-native font stack: Inter for UI, JetBrains Mono for code, Lora serif for data callouts
- Minimal chrome — the interface is intentionally invisible
- Color is data's domain: categorical palettes, sequential gradients, and diverging scales exist only inside charts
- Generous whitespace: 48–96px section spacing creates a breathable reading rhythm
- Subtle 1px cool-gray borders (#e9ecef) — barely-there containment
- No brand accent color — interactive elements use a reserved slate blue (#4263eb) that feels like a utility, not a brand statement
- Soft 4px radius on everything — gentle, unassuming, never draws attention to itself

## 2. Color Palette & Roles

### Surface & Background
- **Canvas White** (`#ffffff`): The primary page background — pure, luminous, gallery-grade.
- **Cool Zone** (`#f8f9fa`): Subtle zone backgrounds for code blocks, sidebar areas, and section differentiation.
- **Warm Zone** (`#fefefe`): A micro-warm white for card surfaces that need the gentlest possible elevation.

### Neutrals & Text
- **Ink** (`#111111`): Primary text — near-black with a hint of warmth, never pure #000.
- **Body Gray** (`#4a4a4a`): Standard body text — comfortable contrast on white.
- **Caption Gray** (`#6b7280`): Secondary text, metadata, axis labels.
- **Disabled Gray** (`#9ca3af`): Muted placeholder text and disabled states.

### UI Chrome
- **Border** (`#e9ecef`): The universal 1px border — cool gray, barely visible.
- **Hover Surface** (`#f1f3f5`): Subtle hover background for interactive rows and list items.
- **Divider** (`#dee2e6`): Slightly stronger border for section dividers.

### Accent & Interactive
- **Slate Blue** (`#4263eb`): Reserved for interactive links, buttons, and focus states. Deliberately muted — never a "brand color," always a functional signal.
- **Hover Blue** (`#3b5ccc`): Link and button hover state — a shade darker.
- **Focus Ring** (`#4263eb` with 40% opacity): 3px focus ring for accessibility.

### Data Color Scales
- **Categorical**: A 10-color palette designed for maximum distinguishability on white — muted jewel tones: slate, rust, teal, amber, plum, moss, rose, cobalt, olive, lavender.
- **Sequential**: Single-hue gradients from light to saturated — used for continuous data.
- **Diverging**: Two-hue gradients meeting at a neutral midpoint — for data with a meaningful center.

### Gradient System
- **None for UI chrome.** Gradients exist only within data visualizations. The interface itself is rigorously flat.

## 3. Typography Rules

### Font Family
- **Primary UI**: `Inter` (weights 300, 400, 500, 600, 700)
- **Code**: `JetBrains Mono` (weights 400, 500)
- **Data Serif**: `Lora` (weights 400, 500, 600; italic 400) — for numeric data callouts and chart annotations

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Page Title | Inter | 32px (2rem) | 600 | 1.25 | -0.5px | Confident but not shouting |
| Section Heading | Inter | 24px (1.5rem) | 600 | 1.3 | -0.3px | Clear hierarchy without heaviness |
| Card Title | Inter | 18px (1.125rem) | 600 | 1.4 | normal | Compact but readable |
| Body | Inter | 16px (1rem) | 400 | 1.6 | normal | Generous line-height for long-form |
| Body Small | Inter | 14px (0.875rem) | 400 | 1.5 | normal | Secondary descriptions |
| Caption / Label | Inter | 12px (0.75rem) | 500 | 1.4 | 0.3px | Axis labels, metadata, timestamps |
| Data Callout | Lora | 36px (2.25rem) | 500 | 1.2 | -0.5px | Big numbers — editorial, not technical |
| Data Callout Small | Lora | 24px (1.5rem) | 400 | 1.3 | normal | Secondary metrics |
| Chart Annotation | Lora Italic | 14px (0.875rem) | 400 | 1.5 | normal | Contextual notes on visualizations |
| Code Block | JetBrains Mono | 14px (0.875rem) | 400 | 1.6 | normal | Code and queries |
| Inline Code | JetBrains Mono | 13px (0.8125rem) | 400 | 1.4 | normal | Inline technical references |

### Principles
- **Data gets the serif**: Numeric data callouts use Lora serif — this is the system's most distinctive typographic move. The serif numbers feel editorial, scholarly, and precise — a deliberate contrast to the sans-serif UI.
- **Weight 400 rules body text**: Regular weight for all body copy. No light weights (300) for readability — only for subtle metadata.
- **Generous line-height**: 1.5–1.6 on body text — the extra breathing room is essential for the spacious, gallery-like feel.
- **Minimal weight contrast**: Only three active weights in any layout (400, 500, 600). The hierarchy comes from size and spacing, not weight changes.

## 4. Component Stylings

### Buttons

**Primary Action**
- Background: Slate Blue (`#4263eb`)
- Text: White (`#ffffff`)
- Padding: 10px 20px
- Radius: 4px
- Border: none
- Font: Inter, 14px, weight 500
- Hover: bg → Hover Blue (`#3b5ccc`), subtle lift (translateY -1px, shadow)
- Focus: 3px ring (`rgba(66,99,235,0.4)`)
- The only solid-color button — used sparingly, one per view maximum

**Secondary / Ghost**
- Background: transparent
- Text: Body Gray (`#4a4a4a`)
- Padding: 10px 20px
- Radius: 4px
- Border: `1px solid #e9ecef`
- Hover: bg → Cool Zone (`#f8f9fa`), border → `#dee2e6`
- Default action for most interactions

**Link / Text Button**
- Background: transparent
- Text: Slate Blue (`#4263eb`)
- Padding: none (inline)
- Hover: text → Hover Blue, subtle underline
- For navigation and inline actions

**Chart Control**
- Background: transparent
- Text: Caption Gray (`#6b7280`)
- Padding: 4px 12px
- Radius: 4px
- Font: Inter, 12px, weight 500
- Active: bg → `#edf2ff`, text → Slate Blue
- For chart toggle buttons, time range selectors

### Cards & Containers

**Standard Card**
- Background: Canvas White (`#ffffff`)
- Border: `1px solid #e9ecef`
- Radius: 6px
- Shadow: none (flat by default)
- Hover (interactive card): shadow `0px 2px 8px rgba(0,0,0,0.06)` + border → `#dee2e6`
- Padding: 24px
- For chart containers, metric cards, data summaries

**Zone Container**
- Background: Cool Zone (`#f8f9fa`)
- Border: none
- Radius: 6px
- Padding: 24px
- For code blocks, configuration panels, sidebar areas
- The subtle background shift defines spatial zones without visible borders

**Metric Card**
- A Standard Card variant optimized for KPI display
- Large Data Callout number (Lora, 36px) at top
- Small label beneath (Inter, 12px, Caption Gray)
- Optional sparkline or mini-chart fills remaining card space
- Minimal internal padding (16px) — the number IS the card

### Data Tables

**Table Container**
- Background: White
- Border: none (top and bottom borders only for header/footer)
- Width: 100%
- No zebra striping — clean rows with minimal separation

**Header Row**
- Background: transparent
- Border-bottom: `1px solid #dee2e6`
- Text: Inter, 11px, weight 600, Caption Gray, uppercase, letter-spacing 0.5px
- Padding: 12px 16px

**Data Row**
- Background: transparent
- Border-bottom: `1px solid #f1f3f5` (subtler than header)
- Text: Inter, 14px, weight 400, Ink
- Padding: 10px 16px
- Hover: bg → Cool Zone (`#f8f9fa`) — the row highlights as a unit

**Numeric Column**
- Right-aligned
- Tabular numbers (font-variant-numeric: tabular-nums) for alignment
- Lora serif at 14px for financial/statistical data columns

### Navigation
- Clean top bar or sidebar
- Background: White with bottom border `1px solid #e9ecef`
- Active item: subtle left-border accent (Slate Blue, 3px) for sidebar; underline for top bar
- Hover: bg → Cool Zone (`#f8f9fa`)
- Text: Body Gray, weight 500
- No brand logo color explosion — logo is grayscale or muted

### Distinctive Components

**KPI Dashboard Grid**
- 3–4 Metric Cards in a row
- Each card: large serif number + tiny sans-serif label
- Optional: inline sparkline beneath number (no axis, no labels — pure shape)
- The grid breathes: 24px gap between cards
- This is the signature "data + whitespace" component

**Chart Canvas**
- White background with subtle grid lines (`#f1f3f5`)
- Axis labels: Inter, 11px, Caption Gray
- Chart colors from the categorical/sequential palettes
- No chart borders — the chart area is defined by axes alone
- Tooltip: white card with subtle shadow, Inter 12px, appears on hover

**Code/Query Block**
- Background: Cool Zone (`#f8f9fa`)
- Border: `1px solid #e9ecef`
- Radius: 6px
- Font: JetBrains Mono, 14px, weight 400
- Syntax highlighting: muted tones — blue for keywords, teal for strings, gray for comments
- Padding: 20px
- Copy button: top-right corner, Ghost style, 28px square

**Time Series Selector**
- Horizontal pill group
- Each option: 4px 12px padding, 12px Inter 500
- Active: blue-tinted bg + Slate Blue text
- Inactive: transparent, Caption Gray text
- No borders — just background shifts

## 5. Layout Principles

### Spacing System
- Base unit: 4px
- Scale: 4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96, 128
- Component padding: 16px (compact), 24px (standard), 32px (generous)
- Section gap: 48px (standard), 64px (generous), 96px (major section breaks)
- Card gap: 24px
- The spacing is deliberately generous — whitespace is the primary luxury

### Grid & Container
- Max content width: 1200px (centered)
- Dashboard: full-width with 32px page margins
- Standard page: 760px max-width for reading comfort
- 12-column grid with 24px gutters
- Metric cards: 3 or 4 per row on desktop, 2 on tablet, 1 on mobile

### Whitespace Philosophy
- **Gallery principle**: Data is art; the white space is the gallery wall. Every visualization needs room to breathe.
- **Content-first**: The UI chrome should occupy less than 15% of any viewport. If you notice the interface, there's too much interface.
- **Vertical rhythm**: Sections are separated by 64–96px of pure white. No dividing lines — the space itself creates the separation.
- **Asymmetric balance**: Dense data areas (tables, charts) are balanced by expansive white space on the opposing side.

### Border Radius Scale
- Sharp (0px): Table cells, code blocks (internal)
- Subtle (4px): Buttons, inputs, tags
- Comfortable (6px): Cards, containers, chart areas
- The radius is never a personality trait — it's purely functional

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow, no border | Page background, text content |
| Zone (Level 1) | Background color shift only (#f8f9fa) | Sidebars, code blocks, section differentiation |
| Bordered (Level 2) | `1px solid #e9ecef` | Standard cards, tables |
| Hover Lift (Level 3) | `0px 2px 8px rgba(0,0,0,0.06)` + translateY(-1px) | Interactive card hover |
| Tooltip (Level 4) | `0px 4px 16px rgba(0,0,0,0.10)` | Floating tooltips, dropdowns |
| Modal Overlay (Level 5) | `0px 8px 32px rgba(0,0,0,0.15)` + backdrop | Modals, dialogs |

**Depth Philosophy**: Observable barely uses shadows. Depth comes from background color shifts and, at most, subtle 1px borders. The only significant shadow appears on floating elements (tooltips, modals) that genuinely need to separate from the surface. The flatness keeps attention on the data.

## 7. Do's and Don'ts

### Do
- Let data provide the color — the UI should be achromatic
- Use generous whitespace — 64px+ between major sections
- Use Lora serif for numeric data callouts — it distinguishes data from UI
- Keep borders to 1px solid #e9ecef — barely visible containment
- Use background color shifts (#f8f9fa zones) for spatial organization
- Apply 1.5–1.6 line-height on body text — breathing room is essential
- Right-align numeric columns with tabular-nums
- Show one Primary button per view maximum — restraint creates clarity
- Use subtle hover states (background shifts, not dramatic color changes)

### Don't
- Don't add a "brand color" — Slate Blue (#4263eb) is a utility, not an identity
- Don't use dark backgrounds — this is a light-mode-native system
- Don't use heavy font weights (700+) for anything except possibly page titles
- Don't add shadows to cards by default — flat is the default state
- Don't use zebra striping on tables — clean rows with minimal separators
- Don't crowd elements — if you need a divider line, you probably need more whitespace
- Don't use saturated/bright UI colors — all color comes from the data
- Don't center-align text blocks — left-aligned, comfortable measure (65–75 chars)
- Don't use gradients in UI chrome — flat, clean surfaces only

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <640px | Single column, metric cards stack, tables become cards |
| Tablet | 640–960px | 2-column grids, reduced section spacing |
| Desktop | 960–1200px | 3–4 column grids, full spacing |
| Wide | 1200px+ | Centered content, max-width caps, extra margin |

### Touch Targets
- Minimum 44px height for interactive elements on mobile
- Card hover states convert to subtle active states on touch
- Table horizontal scroll on narrow screens (with sticky first column)

### Collapsing Strategy
- **KPI grid**: 4 columns → 2 → 1
- **Tables**: Full table → horizontal scroll → card list
- **Charts**: Maintain aspect ratio, scale down proportionally
- **Navigation**: Horizontal → hamburger drawer

## 9. Agent Prompt Guide

### Quick Color Reference
- Page Background: "Canvas White (#ffffff)"
- Zone Surface: "Cool Zone (#f8f9fa)"
- Primary Text: "Ink (#111111)"
- Body Text: "Body Gray (#4a4a4a)"
- Secondary Text: "Caption Gray (#6b7280)"
- Border: "#e9ecef"
- Interactive: "Slate Blue (#4263eb)"
- Hover Surface: "#f1f3f5"

### Example Component Prompts
- "Create a KPI dashboard grid with 4 metric cards on Canvas White (#ffffff). Each card: large Lora serif number (36px, weight 500, Ink #111111) with a tiny Inter caption (12px, Caption Gray) beneath. Cards use 1px solid #e9ecef border, 6px radius, no shadow. 24px gap between cards."
- "Design a data table with clean rows: no zebra striping. Header: 11px Inter weight 600, uppercase, Caption Gray, bottom border 1px solid #dee2e6. Data rows: 14px Inter weight 400, Ink, bottom border 1px solid #f1f3f5. Hover: bg #f8f9fa. Numeric columns right-aligned with Lora serif."
- "Build a chart area: white background with subtle grid lines (#f1f3f5), axis labels in 11px Inter Caption Gray. Chart data colors from a muted categorical palette (slate, rust, teal, amber, plum). Tooltip: white card, subtle shadow, 12px Inter."
- "Create a page layout with generous spacing: 48px page margins, 64-96px between major sections. Content max-width 1200px, centered. One Primary button (Slate Blue, 10px 20px, 4px radius) per section maximum. All other actions use Ghost style."
- "Design a metric callout: the number 3,847,291 in Lora serif 36px weight 500, with a 12px Inter label 'Monthly Active Users' in Caption Gray beneath. 8px gap between number and label. No card — the number floats in whitespace."

### Iteration Guide
1. Start with pure white canvas — add color only where data lives
2. Lora serif for numbers, Inter sans for UI — never mix these roles
3. 4px radius on everything — consistency over expression
4. Borders are 1px #e9ecef — if you want stronger separation, use whitespace, not thicker borders
5. Hover states are background shifts (#f1f3f5 or #f8f9fa), never color explosions
6. One Slate Blue element per view — if you have multiple, convert some to Ghost style
7. Data colors are muted jewel tones — the data should be clear, not loud
