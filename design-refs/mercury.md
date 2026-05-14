# Design System: Mercury

> **Implementation Notes**
>
> The original site uses proprietary fonts. For self-contained HTML output, use these CDN substitutes:
> - **Primary:** `DM Sans` | **Mono:** `JetBrains Mono` | **Serif (financial figures):** `Playfair Display`
> - **Font stack (CSS):** `font-family: 'DM Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;`
> - **Mono stack (CSS):** `font-family: 'JetBrains Mono', 'SF Mono', 'Fira Code', monospace;`
> ```html
> <link href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600;9..40,700&family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,500&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
> ```
> Use standard file writing to create HTML. Serve via local server or deploy as needed.
> Verify visual accuracy in browser after generating.

## 1. Visual Theme & Atmosphere

Mercury's interface is modern banking rendered as breathing space — a design system that proves financial tools can be calm, approachable, and almost luxurious in their restraint. The canvas is a warm near-white (`#fcfcf9`) that feels like premium letterhead, with content elevated on pure white cards (`#ffffff`) that float with the gentlest shadows. This is finance designed for clarity, not intimidation.

The color palette is achromatic at its core — warm grays and near-blacks — with a single accent: Mercury Green (`#4ade80`), a fresh, optimistic green that signals growth, health, and positive financial momentum. It appears sparingly: on primary CTAs, positive-value indicators, and the most important data highlights. Red (`#ef4444`) serves as its necessary counterpart for negative values and alerts, but it's muted — never alarmist.

The typography is clean and geometric: DM Sans for UI and body text, with Playfair Display serif reserved exclusively for large financial figures. This serif/sans-serif division mirrors the Observable pattern — serif numbers carry editorial weight and trustworthiness, while the sans-serif UI remains neutral and unobtrusive. The entire system communicates "your money is safe here" through design restraint alone.

**Key Characteristics:**
- Warm near-white canvas (#fcfcf9) with pure white cards (#ffffff) — premium stationery aesthetic
- Mercury Green (#4ade80) as the sole positive accent — fresh, growth-oriented, optimistic
- Dual-font financial hierarchy: Playfair Display serif for monetary figures, DM Sans for all UI
- Generous card-based layout with subtle shadow elevation
- 12px border radius (rounded-rectangle) — the unified shape language
- Muted red (#ef4444 at 85% opacity) for negative values — clear but never alarming
- Warm gray neutral scale — every gray carries a subtle amber undertone
- Financial tables with alternating subtle row backgrounds (not zebra stripes — zone-based grouping)

## 2. Color Palette & Roles

### Surface & Background
- **Warm Canvas** (`#fcfcf9`): The primary page background — an off-white with a micro-warmth that eliminates clinical coldness. Like fine paper.
- **Card White** (`#ffffff`): Card and container surfaces — pure white for maximum crispness.
- **Warm Zone** (`#f7f6f3`): Subtle zone differentiation for sidebars, secondary sections, and grouped table rows.

### Neutrals & Text
- **Near Black** (`#1a1a1a`): Primary text — a warm black, never pure #000.
- **Body Charcoal** (`#3d3d3d`): Standard body text — softer than Near Black for extended reading comfort.
- **Caption Warm Gray** (`#6b6b63`): Secondary text, labels, metadata — a gray with warm undertones.
- **Disabled Warm Gray** (`#9c9c94`): Placeholder and disabled text.
- **Border Warm** (`#e8e7e2`): Universal 1px border — warm-toned, barely visible.

### Accent & Semantic
- **Mercury Green** (`#4ade80`): The signature positive accent — CTAs, positive value indicators, success states, growth arrows. Fresh and optimistic.
- **Deep Green** (`#22c55e`): Darker green for hover states on green elements.
- **Green Tint** (`#ecfdf5`): Subtle green-tinted background for positive-value rows and success callouts.
- **Muted Red** (`#ef4444` at 85% opacity): Negative values and alerts. Deliberately muted — financial stress shouldn't scream.
- **Red Tint** (`#fef2f2`): Subtle red-tinted background for negative-value rows and warning callouts.
- **Amber** (`#f59e0b`): Caution/warning indicators — used only for pending states.

### Gradient System
- **None for UI chrome.** Mercury uses flat, clean surfaces. Gradients, if they appear at all, are limited to hero backgrounds as ultra-subtle radial glows (white → warm canvas).

## 3. Typography Rules

### Font Family
- **Primary UI**: `DM Sans` (weights 400, 500, 600, 700)
- **Financial Figures**: `Playfair Display` (weights 500, 600, 700; italic 500)
- **Code/Mono**: `JetBrains Mono` (weights 400, 500)

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Page Title | DM Sans | 36px (2.25rem) | 700 | 1.15 | -1px | Bold but approachable |
| Section Heading | DM Sans | 28px (1.75rem) | 600 | 1.2 | -0.5px | Clean hierarchy anchor |
| Card Title | DM Sans | 18px (1.125rem) | 600 | 1.3 | -0.2px | Compact card headers |
| Body | DM Sans | 16px (1rem) | 400 | 1.6 | normal | Comfortable reading |
| Body Small | DM Sans | 14px (0.875rem) | 400 | 1.5 | normal | Secondary content |
| Caption / Label | DM Sans | 12px (0.75rem) | 500 | 1.4 | 0.2px | Table headers, metadata, form labels |
| Financial Figure Large | Playfair Display | 42px (2.625rem) | 700 | 1.1 | -0.5px | Hero KPI numbers |
| Financial Figure Medium | Playfair Display | 32px (2rem) | 600 | 1.15 | -0.3px | Dashboard metric cards |
| Financial Figure Small | Playfair Display | 24px (1.5rem) | 600 | 1.2 | normal | Inline financial data |
| Table Numeric | Playfair Display | 16px (1rem) | 500 | 1.2 | normal | Right-aligned table values |
| Positive/Negative | DM Sans | 14px (0.875rem) | 600 | 1.4 | normal | Δ indicators, percentage changes |
| Code | JetBrains Mono | 13px (0.8125rem) | 400 | 1.5 | normal | Technical references |

### Principles
- **Serif signals money**: All monetary values (¥, $, € amounts) use Playfair Display serif. This creates an immediate perceptual distinction — the reader's eye knows "this is a financial figure" before reading the number.
- **Weight 700 for hero numbers, 600 for dashboard, 500 for tables**: A clear numeric weight hierarchy that mirrors the data's importance.
- **DM Sans at weight 400 for body**: The geometric sans-serif is clean but humanist enough to feel warm, not mechanical.
- **Positive/Negative indicators use DM Sans weight 600**: The semi-bold weight gives directional indicators (▲ +12.5%, ▼ -3.2%) the visual confidence they need.
- **Tabular numbers everywhere**: All numeric columns use `font-variant-numeric: tabular-nums` for perfect vertical alignment.

## 4. Component Stylings

### Buttons

**Primary Green**
- Background: Mercury Green (`#4ade80`)
- Text: Near Black (`#1a1a1a`)
- Padding: 12px 24px
- Radius: 12px
- Border: none
- Font: DM Sans, 15px, weight 600
- Hover: bg → Deep Green (`#22c55e`), subtle lift (translateY -1px)
- Focus: 3px ring (`rgba(74,222,128,0.4)`)
- For primary CTAs: "Generate Report," "Export," "Approve"

**Secondary Outline**
- Background: transparent
- Text: Body Charcoal (`#3d3d3d`)
- Padding: 12px 24px
- Radius: 12px
- Border: `1.5px solid #e8e7e2`
- Hover: bg → Warm Zone (`#f7f6f3`), border → `#d4d3ce`
- For secondary actions

**Ghost / Text Button**
- Background: transparent
- Text: Body Charcoal (`#3d3d3d`)
- Padding: 8px 16px
- Radius: 12px
- Hover: bg → Warm Zone (`#f7f6f3`)
- For navigation, links, tool actions

**Danger Button**
- Background: transparent
- Text: Muted Red (`rgba(239,68,68,0.85)`)
- Padding: 12px 24px
- Radius: 12px
- Border: `1.5px solid rgba(239,68,68,0.2)`
- Hover: bg → Red Tint (`#fef2f2`)
- Used rarely — only for destructive actions

### Cards & Containers

**Standard Card**
- Background: Card White (`#ffffff`)
- Border: `1px solid #e8e7e2`
- Radius: 12px
- Shadow: `0px 1px 3px rgba(0,0,0,0.04), 0px 1px 2px rgba(0,0,0,0.02)`
- Hover (interactive): shadow deepens to `0px 4px 12px rgba(0,0,0,0.06)`
- Padding: 24px
- The fundamental surface unit

**Financial Statement Card**
- A Standard Card variant for P&L, balance sheets, cash flow statements
- Internal padding: 32px (extra room for tabular data)
- Optional section dividers: `1px solid #e8e7e2` between statement sections
- Total/Subtotal rows: background → Warm Zone (`#f7f6f3`), heavier top border

**Metric Card (KPI)**
- Background: Card White
- Border: `1px solid #e8e7e2`
- Radius: 12px
- Padding: 20px
- Large Playfair Display figure at top
- Small DM Sans label beneath with Caption Warm Gray
- Optional: color-coded trend indicator (▲ green / ▼ red) in top-right corner
- Optional: inline sparkline at bottom

### Data Tables (Financial)

**Table Container**
- Background: Card White
- Border: `1px solid #e8e7e2`
- Radius: 12px
- Width: 100%
- Overflow: auto (horizontal scroll for wide tables)

**Header Row**
- Background: transparent
- Border-bottom: `1.5px solid #e8e7e2`
- Text: DM Sans, 12px, weight 500, Caption Warm Gray, uppercase, letter-spacing 0.3px
- Padding: 14px 20px
- Sticky on scroll (position: sticky, top: 0)

**Data Row**
- Background: transparent
- Border-bottom: `1px solid #f0efe9`
- Text: DM Sans (labels) / Playfair Display (values), 14-16px
- Padding: 12px 20px
- Hover: bg → Warm Zone (`#f7f6f3`)

**Positive Value Row**
- Optional Green Tint (`#ecfdf5`) background for rows with positive financial outcomes
- Playfair Display value in Deep Green (`#22c55e`)

**Negative Value Row**
- Optional Red Tint (`#fef2f2`) background for rows with negative outcomes
- Playfair Display value in Muted Red

**Subtotal / Section Row**
- Background: Warm Zone (`#f7f6f3`)
- Top border: `1.5px solid #e8e7e2`
- Text: DM Sans, weight 600, Body Charcoal
- Playfair Display for values, weight 600

**Total / Grand Total Row**
- Background: Warm Canvas (`#fcfcf9`)
- Top border: `2px solid #d4d3ce`
- Bottom border: `2px solid #d4d3ce` (double-struck accounting convention)
- Text: DM Sans, weight 700, Near Black
- Playfair Display for values, weight 700

### Navigation
- Clean top-bar navigation
- Background: Card White with bottom border `1px solid #e8e7e2`
- Active nav item: Mercury Green underline (3px) or left-border accent
- Hover: text → Near Black, subtle background shift
- Minimal — navigation is a utility, not a destination

### Distinctive Components

**Financial Dashboard Grid**
- 2–4 Metric Cards in a row
- Each card shows: KPI name (label) + large serif value + Δ indicator (▲/▼ + percentage)
- Color-coded: green for positive Δ, red for negative Δ
- The grid's density varies — key metrics get larger cards

**P&L Statement Card**
- A dedicated card type for profit & loss statements
- Vertical layout with clear section grouping (Revenue → COGS → Gross Profit → OpEx → Net Income)
- Each line: label (left), value (right-aligned), optional % of revenue column
- Subtotals in Warm Zone background
- Net Income row: double-struck border, Mercury Green if positive

**Balance Sheet Card**
- Two-column layout: Assets (left) | Liabilities + Equity (right)
- Each side has its own column header
- Final row (Total Assets = Total Liabilities + Equity): double-struck border across both columns
- The accounting equation is the visual anchor

**Cash Flow Statement**
- Three-section layout: Operating → Investing → Financing
- Each section: inflow items above, outflow items below, net subtotal
- Positive net: green background tint; negative net: red background tint
- Bottom line: Net Change in Cash with Mercury Green emphasis

**Trend Indicator**
- Compact component for KPI cards
- Arrow (▲ or ▼) + percentage change
- Color: Mercury Green for positive, Muted Red for negative
- Font: DM Sans, 14px, weight 600
- Positioned adjacent to the KPI figure

**Waterfall Chart Card**
- For MoM/QoQ variance analysis
- Green bars for positive contributions, red for negative
- Starting value → intermediate changes → ending value
- Clean, minimal grid lines

**Approval / Status Badge**
- Pill shape (12px radius, 4px 12px padding)
- Green: "Approved," "Completed," "Paid"
- Amber: "Pending," "In Review," "Processing"
- Red: "Rejected," "Overdue," "Failed"
- Font: DM Sans, 11px, weight 600, uppercase, letter-spacing 0.3px

## 5. Layout Principles

### Spacing System
- Base unit: 4px
- Scale: 4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96
- Card padding: 20px (compact KPI), 24px (standard), 32px (financial statement)
- Section gap: 32px (dense dashboard), 48px (standard), 64px (report view)
- Table row padding: 12px 20px

### Grid & Container
- Max content width: 1280px (centered)
- Dashboard: full-width with 32px margins
- Report view: 960px max-width for focused reading
- 12-column grid with 20px gutters
- Metric cards: 4 per row (desktop), 2 (tablet), 1 (mobile)

### Whitespace Philosophy
- **Breathing numbers**: Financial data is dense — the surrounding whitespace must be generous to prevent cognitive overload. Every table needs 24px+ of margin around it.
- **Card isolation**: Each financial statement or dashboard card is visually isolated by generous gaps — the eye processes one data story at a time.
- **Content density gradient**: Dashboards are denser (more data per view), report views are airier (reading rhythm matters).

### Border Radius Scale
- Sharp (0px): Table cells (internal)
- Rounded (12px): The universal radius — buttons, cards, inputs, tags, badges. Consistent everywhere.
- Pill (9999px): Toggle buttons, status indicators, filter chips

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow, no border | Page background, inline text |
| Bordered (Level 1) | `1px solid #e8e7e2` | Cards, tables, inputs |
| Subtle Float (Level 2) | `0px 1px 3px rgba(0,0,0,0.04)` | Standard cards |
| Elevated (Level 3) | `0px 4px 12px rgba(0,0,0,0.06)` | Interactive card hover |
| Tooltip (Level 4) | `0px 4px 16px rgba(0,0,0,0.08)` | Dropdowns, tooltips |
| Modal (Level 5) | `0px 8px 32px rgba(0,0,0,0.12)` + backdrop | Dialogs, modals |

**Depth Philosophy**: Mercury uses subtly layered cards — each card has the gentlest possible shadow (barely visible on white) plus a 1px warm-gray border. The effect is of cards resting on fine paper. Hover states deepen the shadow slightly. The overall impression is premium stationery, not a control panel.

## 7. Do's and Don'ts

### Do
- Use Playfair Display serif for ALL monetary values — it's the financial voice
- Use DM Sans for all UI text, labels, and non-financial numbers
- Keep the canvas warm (#fcfcf9) — never pure white, never cool gray
- Apply Mercury Green (#4ade80) only for positive indicators, CTAs, and growth signals
- Use muted red (#ef4444 at 85% opacity) — financial stress shouldn't scream
- Double-strike totals rows (2px top + 2px bottom border) — accounting convention as design
- Right-align all numeric columns with tabular-nums
- Use 12px radius on all cards and buttons — consistency creates trust
- Add warm-tinted backgrounds (#f7f6f3) to subtotal/section rows
- Provide generous whitespace around dense financial tables

### Don't
- Don't use pure black (#000000) — always the warm near-black (#1a1a1a)
- Don't use bright/saturated red for negative values — mute it
- Don't use zebra striping — warm zone grouping (by section) is cleaner
- Don't use dark backgrounds — this is a light-mode financial design
- Don't use sharp corners (0px radius) on cards or buttons — 12px is the standard
- Don't overuse Mercury Green — it's an accent, not a pervasive color
- Don't mix financial figures with sans-serif — Playfair Display is non-negotiable for money
- Don't center-align text — left-aligned labels, right-aligned numbers
- Don't skip the hover state on interactive rows — financial tools live in their details

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <640px | Single column, tables become card lists, reduced font sizes |
| Tablet | 640–960px | 2-column grids, tables with horizontal scroll |
| Desktop | 960–1280px | 3–4 column grids, full statement layouts |
| Wide | 1280px+ | Centered content, ample margins |

### Touch Targets
- Minimum 44px height for all interactive elements
- Table rows: 44px minimum height for tap targets
- Card hover states → subtle active states on touch

### Collapsing Strategy
- **Financial statements**: Side-by-side (Assets | Liabilities) → stacked vertically
- **Dashboard grids**: 4 columns → 2 → 1
- **Tables**: Full table → horizontal scroll → card-per-row
- **Navigation**: Full bar → hamburger menu

### Number Scaling
- Financial Figure Large: 42px → 32px → 28px → 24px
- Financial Figure Medium: 32px → 24px → 20px → 18px
- Table values maintain readability at all sizes

## 9. Agent Prompt Guide

### Quick Color Reference
- Page Background: "Warm Canvas (#fcfcf9)"
- Card Surface: "Card White (#ffffff)"
- Primary Text: "Near Black (#1a1a1a)"
- Body Text: "Body Charcoal (#3d3d3d)"
- Secondary Text: "Caption Warm Gray (#6b6b63)"
- Border: "#e8e7e2"
- Positive Accent: "Mercury Green (#4ade80)"
- Negative: "Muted Red (rgba(239,68,68,0.85))"
- Warm Zone: "#f7f6f3"
- Green Tint: "#ecfdf5"
- Red Tint: "#fef2f2"

### Example Component Prompts
- "Create a financial KPI dashboard with 4 metric cards. Each card: Warm Canvas background, Card White card with 1px #e8e7e2 border and 12px radius. Large Playfair Display value (32px, weight 600, Near Black), DM Sans label (12px, Caption Warm Gray), and a trend indicator (▲ +12.5%, Mercury Green, DM Sans 14px weight 600) in the top-right corner."
- "Design a P&L statement card. Sections: Revenue → COGS → Gross Profit → OpEx → Net Income. Each line: DM Sans label (left, 14px, Body Charcoal) + Playfair Display value (right, 16px, weight 500, tabular-nums). Subtotals in Warm Zone (#f7f6f3) with 1.5px top border. Net Income: double-struck (2px top + 2px bottom border #d4d3ce), Mercury Green if positive, Muted Red if negative."
- "Build a balance sheet card with two columns: Assets (left) and Liabilities + Equity (right). Each column has 11px DM Sans header in Caption Warm Gray, uppercase. Rows: 14px DM Sans labels + 16px Playfair Display values. Final row spanning both columns with double-struck border."
- "Create a financial data table: Card White container, 12px radius, 1px #e8e7e2 border. Header: 12px DM Sans weight 500, uppercase, Caption Warm Gray, sticky. Rows: 14px/16px text, 12px 20px padding. Positive rows: Green Tint (#ecfdf5) background, negative: Red Tint (#fef2f2). Hover: Warm Zone (#f7f6f3)."
- "Design a cash flow waterfall: green bars (#4ade80) for inflows, red bars (rgba(239,68,68,0.85)) for outflows. Net change bar in Mercury Green with double-struck endpoint. Clean grid lines in #e8e7e2."

### Iteration Guide
1. Start with Warm Canvas (#fcfcf9) — the paper-like background sets the entire tone
2. Playfair Display = money, DM Sans = everything else — never cross the streams
3. 12px radius everywhere — this consistency IS the brand
4. Mercury Green is precious — use it for CTAs and positive values only
5. Muted red — full red is too alarming for financial contexts
6. Double-struck totals (2px top + 2px bottom borders) — the accounting visual signature
7. Warm neutrals only — every gray has an amber undertone
8. Generous whitespace between financial sections — dense data needs breathing room
