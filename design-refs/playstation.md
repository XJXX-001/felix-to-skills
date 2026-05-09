# Design System: PlayStation

> **Implementation Notes**
>
> The original site uses proprietary SST typefaces (Sony's custom family). For self-contained HTML output, use these CDN substitutes:
> - **Primary/Display:** `Rajdhani` (geometric, technical, similar to SST) | **Body:** `Rajdhani`
> - **Font stack (CSS):** `font-family: 'Rajdhani', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;`
> - **Mono stack (CSS):** `font-family: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;`
> ```html
> <link href="https://fonts.googleapis.com/css2?family=Rajdhani:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
> ```
> Use standard file writing to create HTML. Serve via local server or deploy as needed.
> Verify visual accuracy in browser after generating.

## 1. Visual Theme & Atmosphere

PlayStation's digital presence is built on the three-surface channel layout — a distinctive UI pattern where the screen is divided into left navigation, center content, and right detail panels. This isn't a website that scrolls through sections; it's a console interface rendered in the browser. The dark canvas (`#1a1c23` deep navy-black) creates a premium gaming atmosphere — not pure black (which would feel like a blank screen) but a rich, deep blue-black that recalls the PS5's default system theme.

The signature color is PlayStation Blue (`#003791`) — the same deep indigo that's been the brand anchor since the PS2 era. It appears in the iconic square-triangle-circle-cross button symbols ( , , , ), in the PS logo, and in interactive elements. The blue is deep and authoritative — not the bright gaming blue of competitors, but a mature, premium blue that says "we've been doing this for 30 years."

The most distinctive interaction pattern is the hover-scale-reveal: cards and thumbnails enlarge on hover (scale 1.02-1.05) while revealing additional content — game trailers auto-play, screenshots slide, "Learn More" buttons fade in. This creates a browsing experience that feels alive and responsive, like thumbing through a digital game library. The transition timing (0.3s ease) is tuned to feel snappy — responsive enough for a gamer's expectations, smooth enough for premium hardware.

Layout cadence follows a channel rhythm: headline → hero tile → 3-4 card grid → headline → hero tile. The constant alternation between full-width hero moments and dense card grids creates a browsing pattern that's both dramatic and efficient. Background gradients shift subtly between sections — navy to deep purple to near-black — creating atmospheric depth without distracting from content.

**Key Characteristics:**
- Three-surface channel layout: nav | content | detail (the UI signature)
- Deep navy-black canvas (`#1a1c23`) — a premium gaming atmosphere
- PlayStation Blue (`#003791`) as the sole brand accent — mature, authoritative
- Hover-scale-reveal: cards enlarge + reveal content on hover (scale 1.02-1.05)
-  , , ,  button symbols as iconic UI punctuation
- Dense game card grids alternating with full-width hero tiles
- Subtle gradient backgrounds creating atmospheric depth
- Generous border-radius (12-24px) — the opposite of sharp, aggressive gaming aesthetics

## 2. Color Palette & Roles

### Primary
- **PlayStation Blue** (`#003791`): The brand. PS logo, button symbols, primary CTAs, active states, highlights. A deep indigo blue — not bright, not cyan — that carries 30 years of gaming heritage.
- **Deep Navy** (`#1a1c23`): Primary dark surface. Page background, side navigation, cards on dark.
- **Near-Black** (`#0f1013`): Deeper sections, footer, immersive backgrounds.
- **White** (`#ffffff`): Text on dark, primary button text, occasional light-mode cards.

### Accent & Interactive
- **Blue Hover** (`#002a6e`): Darker blue for hover states.
- **Blue Glow** (`rgba(0,55,145,0.15)`): Ambient blue glow on featured elements.
- **PS Plus Gold** (`#d4af37`): Exclusive to PlayStation Plus branding — membership tiers, premium badges. Used sparingly, never for general CTAs.
- **Gradient Start** (`#1a1c23`): Section background top.
- **Gradient End** (`#252840`): Section background bottom — subtle navy-to-purple atmospheric shift.

### Text
- **Primary Text (Dark BG)** (`#ffffff`): Headlines, body on dark surfaces.
- **Secondary Text (Dark BG)** (`#8b8d96`): Descriptions, metadata, secondary information.
- **Tertiary Text (Dark BG)** (`#555761`): Captions, dates, least important info.
- **Primary Text (Light BG)** (`#1a1c23`): Text on white cards/surfaces.

### Surface & Border
- **Card Surface** (`#242631`): Slightly lifted from background for card distinction.
- **Card Surface (Light)** (`#ffffff`): White cards when used in light-mode sections.
- **Card Border** (`#2e303b`): Subtle borders on dark cards.
- **Card Border Hover** (`#003791`): Blue border on hover — the PS signature.
- **Divider** (`#2a2c36`): Section dividers.
- **Input Background** (`#242631`): Dark input fields.
- **Input Border** (`#2e303b`): Input borders.
- **Input Focus** (`#003791`): Blue focus ring.

### Shadow & Glow
- **Card Elevation** (`0 4px 20px rgba(0,0,0,0.3)`): Standard card shadow.
- **Card Hover Elevation** (`0 8px 32px rgba(0,55,145,0.15)`): Blue-tinted elevated shadow.
- **Hero Glow** (`0 0 60px rgba(0,55,145,0.08)`): Ambient atmosphere behind hero tiles.

## 3. Typography Rules

### Font Family
- **Primary**: `SST` (Sony's proprietary), fallback: `Rajdhani`
- **Display**: `SST` heavier weights for headlines
- **UI**: `SST` lighter weights for body and navigation

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Hero Title | Rajdhani | 48-64px (3-4rem) | 700 | 1.0 | -0.5px | Game title, campaign headline |
| Section Title | Rajdhani | 32-40px (2-2.5rem) | 600 | 1.1 | normal | Category headers |
| Card Title | Rajdhani | 20-24px (1.25-1.5rem) | 600 | 1.15 | normal | Game names |
| Body Large | Rajdhani | 18px (1.125rem) | 400 | 1.5 | normal | Feature descriptions |
| Body | Rajdhani | 16px (1rem) | 400 | 1.5 | normal | Standard text |
| Body Small | Rajdhani | 14px (0.875rem) | 400 | 1.45 | normal | Descriptions, metadata |
| Button Large | Rajdhani | 16px (1rem) | 600 | 1.0 | normal | Primary CTAs |
| Button Small | Rajdhani | 14px (0.875rem) | 600 | 1.0 | normal | Secondary CTAs |
| Nav Link | Rajdhani | 15px (0.94rem) | 500 | 1.0 | normal | Side nav items |
| Price | Rajdhani | 20px (1.25rem) | 700 | 1.0 | normal | Game prices |
| Release Date | Rajdhani | 13px (0.81rem) | 500 | 1.0 | 0.5px | uppercase | "OUT NOW", "PRE-ORDER" |
| Caption | Rajdhani | 12px (0.75rem) | 400 | 1.4 | normal | Legal, ESRB ratings |
| Badge | Rajdhani | 11px (0.69rem) | 600 | 1.0 | 1px | uppercase | "PS5", "PS4", "PS PLUS" |

### Principles
- **SST/Rajdhani everywhere**: PlayStation uses a single type family for everything — headlines and body differ in weight and size, not font. This creates a unified, console-UI feel.
- **Weight-driven hierarchy**: 700 hero → 600 card titles → 500 nav → 400 body. Clear, systematic, like a game's menu system.
- **High x-height, open counters**: Rajdhani (like SST) has a high x-height and open letterforms — designed for readability on screens at all sizes, especially on TV-distance displays.
- **Tight display tracking**: Hero titles at -0.5px letter-spacing — dense and impactful without being cramped.
- **Uppercase for metadata**: "OUT NOW", "PRE-ORDER", "PS5" — metadata labels use uppercase at 11-13px with spacing.

## 4. Component Stylings

### The Three-Surface Layout (Signature Pattern)

**Left Nav Panel**
- Width: 280px (desktop), hidden off-canvas (mobile)
- Background: `#1a1c23` or slightly darker for separation
- Logo: PS logo at top
- Links: Rajdhani 15px weight 500, `#8b8d96`, hover to `#ffffff`
- Active link: `#ffffff` with blue left border accent (`#003791`, 3px wide)
- Section dividers: `1px solid #2a2c36`
- Icons: 20px outline icons in `#8b8d96`

**Center Content Panel**
- Main scrolling area
- Hero tiles + card grids
- Full height, scrollable

**Right Detail Panel (Contextual)**
- Width: 360px (desktop), slides in from right
- Background: `#242631`
- Shows: selected game details, trailer, screenshots, price, buy button
- Close: X button top-right

### Buttons

**Primary CTA (Blue)**
- Background: `#003791`
- Text: `#ffffff`
- Padding: 14px 28px
- Radius: 12px (generous — friendly, modern gaming)
- Font: 16px Rajdhani weight 600
- Hover: `#002a6e` background, scale(1.02)
- Hover Transition: 0.3s ease
- Use: "Buy Now", "Add to Library", "Download"

**Secondary (Outline)**
- Background: transparent
- Text: `#ffffff`
- Padding: 14px 28px
- Radius: 12px
- Border: `1.5px solid #2e303b`
- Font: 16px Rajdhani weight 500
- Hover: border shifts to `#003791`, text to `#003791`
- Use: "Learn More", "Wishlist"

**Ghost**
- Background: transparent
- Text: `#8b8d96`
- Padding: 10px 20px
- Radius: 8px
- Hover: `rgba(255,255,255,0.05)` background, `#ffffff` text
- Use: Navigation CTAs, "View All"

**Icon Button (PS Symbols)**
- The  ,  ,  ,  symbols used as interactive buttons
- Size: 40-48px circles
- Background: `rgba(255,255,255,0.05)`
- Hover: `rgba(0,55,145,0.15)` background with blue glow
- Use: Carousel navigation, contextual actions

### Game Cards
- Background: `#242631`
- Border: `1px solid #2e303b`
- Radius: 12px
- Overflow: hidden (image flush to top)
- Image: full card width, `border-radius: 12px 12px 0 0`
- Padding (content area): 16px
- Hover: scale(1.03), border shifts to `#003791`, box-shadow `0 8px 32px rgba(0,55,145,0.15)`
- Hover content reveal: "Learn More" button fades in, additional info appears
- Transition: 0.3s cubic-bezier(0.4, 0, 0.2, 1) — console-smooth
- Content: game art → title (20px Rajdhani 600) → platform badge → price → rating stars

### Hero Tile
- Full-width featured game tile
- Background: game art + gradient overlay (`rgba(26,28,35,0.3)` to `rgba(26,28,35,0.8)`)
- Height: 400-560px
- Radius: 16px (larger than cards — hero distinction)
- Content overlaid at bottom-left: game logo/title (48px Rajdhani 700 white) + platform badges + CTA
- Hover: subtle parallax or light animation
- Navigation:   /   arrows (PS controller buttons) on sides

### Platform Badges
- Small pill badges indicating platform
- PS5: `#003791` background, white text
- PS4: `#1a1c23` background, `#003791` text, `#003791` border
- PS Plus: `#d4af37` background (gold), `#1a1c23` text (rare, premium only)
- Font: 11px Rajdhani weight 600, uppercase, 1px letter-spacing
- Padding: 3px 10px, Radius: 20px (pill)

### Navigation (Top Bar)
- Fixed top, height: 56px
- Background: `rgba(26,28,35,0.85)` + `backdrop-filter: blur(12px)`
- Logo: PS logo left
- Links: Rajdhani 14px weight 500, `#8b8d96`, hover `#ffffff`
- Active: `#ffffff` with subtle blue underline
- Right: Search icon + Account avatar + Cart
- Mobile: hamburger → slide-out menu

## 5. Layout Principles

### Spacing System
- Base unit: 8px
- Scale: 4px, 8px, 12px, 16px, 20px, 24px, 32px, 40px, 48px, 64px, 80px, 120px
- Card grid gaps: 16-20px
- Section padding: 48-64px

### Three-Panel Layout
```
| Nav (280px) | Content (flex) | Detail (360px) |
|   fixed     |    scrollable   |   slide-in    |
```

### Grid
- 12-column grid within content panel
- Game cards: 4 columns per row (desktop), 3 (tablet), 2 (mobile)
- Hero tile: full width (12 columns)
- Gutter: 20px

### Cadence
- Hero tile (full-width featured game)
- Section heading
- 4-column game card grid (8-12 cards)
- Divider / gradient transition
- Hero tile (next category/game)
- Section heading
- 4-column grid
- Repeat

### Whitespace Philosophy
- **Dense but organized**: Game cards pack tightly (16-20px gaps) but the grid is rigidly organized — like a game library shelf.
- **Hero breathing room**: Hero tiles get generous space (400-560px height) to let game art dominate.
- **Nav anchoring**: The fixed left nav creates a stable frame — only the center content scrolls.

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Base Canvas | `#1a1c23` | Page background |
| Nav Panel | Same as base or `#16181e` | Side navigation |
| Card (Level 1) | `#242631` + `0 4px 20px rgba(0,0,0,0.3)` | Game cards |
| Card Hover (Level 2) | `#242631` + `0 8px 32px rgba(0,55,145,0.15)` + scale(1.03) | Hovered game cards |
| Detail Panel (Level 3) | `#242631` + `0 -4px 24px rgba(0,0,0,0.4)` | Right slide-in panel |
| Modal (Level 4) | `#1a1c23` + `0 16px 48px rgba(0,0,0,0.5)` + backdrop | Full modals |
| Focus | `2px solid #003791` outline | Keyboard navigation |

**Depth Philosophy**: PlayStation depth is layered but soft. Cards lift with scale animation (not just shadow) creating a tactile, console-UI feel. The blue-tinted hover shadow (`rgba(0,55,145,0.15)`) ties elevation to the brand color. The right detail panel slides over content with a solid shadow — the only hard elevation in the system.

## 7. Do's and Don'ts

### Do
- Use the three-surface layout (nav | content | detail) — PlayStation's UI signature
- Use hover-scale-reveal: scale(1.02-1.05) + blue border + new content on hover
- Use deep navy (`#1a1c23`) — not pure black — for the atmospheric background
- Use PlayStation Blue (`#003791`) as the exclusive accent color
- Use 12-16px border-radius — soft, friendly, modern gaming
- Use Rajdhani for everything — one type family, weight-driven hierarchy
- Use gradient backgrounds to create atmospheric depth between sections
- Use the   ,  ,  ,  symbols as iconic interactive elements

### Don't
- Don't use pure black — `#1a1c23` navy-black is the PlayStation atmosphere
- Don't skip hover animations — scale+reveal is fundamental to the browsing experience
- Don't use sharp corners — PlayStation is rounded and welcoming, not aggressive
- Don't introduce secondary accent colors — blue is the only one (gold for PS Plus only)
- Don't use card layouts without hover effects — cards should feel alive
- Don't use multiple typefaces — SST (Rajdhani) is the only type family
- Don't make the detail panel modal — it's a persistent slide-in panel, not a popup
- Don't overuse the blue glow effect — reserve for hero moments and featured cards

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <768px | No side panels, single-column, bottom nav |
| Tablet | 768-1024px | Left nav collapses to icon rail, no detail panel |
| Desktop | 1024-1440px | Full three-surface layout |
| Large Desktop | >1440px | All panels at full width |

### Collapsing Strategy
- Left nav: 280px full → 64px icon rail → hidden, bottom tab bar
- Right detail panel: 360px slide-in → hidden, detail becomes full-screen modal
- Hero tiles: 560px → 400px → 300px, maintaining game art focus
- Game cards: 4 columns → 3 → 2 → 1.5-wide scrollable row
- PS symbols: maintain recognizable size, may reposition
- Top nav: keep fixed at all sizes

### Touch Targets
- Game cards: minimum 160px wide for touch
- Buttons: minimum 44px height
- PS symbol buttons: 40-48px circular targets
- Card hover effects: convert to tap-and-hold or long-press on touch devices

### Image Behavior
- Game art: center-crop, maintains aspect ratio
- Hero tile backgrounds: `object-fit: cover`, focal point on game character/logo
- Gradient overlays: maintain opacity ratios across sizes

## 9. Agent Prompt Guide

### Quick Color Reference
- PlayStation Blue: `#003791`
- Blue Hover: `#002a6e`
- Deep Navy: `#1a1c23`
- Near-Black: `#0f1013`
- Card Surface: `#242631`
- White: `#ffffff`
- Secondary Text: `#8b8d96`
- Tertiary Text: `#555761`
- Card Border: `#2e303b`
- Card Border Hover: `#003791`
- Divider: `#2a2c36`
- PS Plus Gold: `#d4af37` (exclusive to PS Plus)
- Blue Glow: `rgba(0,55,145,0.15)`

### Example Component Prompts
- "Create a PlayStation game card: #242631 background, 1px solid #2e303b border, 12px radius, overflow hidden. Game art at top, flush to card edges with 12px top radius. Title at 20px Rajdhani weight 600 #ffffff. Platform badge 'PS5' at 11px weight 600 uppercase #003791 bg + white text, pill shape 3px 10px padding. Price at 20px weight 700 #ffffff. On hover: scale(1.03), border shifts to #003791, box-shadow 0 8px 32px rgba(0,55,145,0.15). Button 'Learn More' fades in, transition 0.3s cubic-bezier(0.4, 0, 0.2, 1)."
- "Build a hero tile: full-width, 480px height, game art background with gradient overlay rgba(26,28,35,0.3) to rgba(26,28,35,0.8). Game title at 48px Rajdhani weight 700 #ffffff at bottom-left. Platform badges row below. Blue CTA 'Buy Now' — #003791 bg, white text, 12px radius. PS symbol navigation arrows on sides."
- "Create the left nav panel: 280px width, #1a1c23 background. PS logo at top (32px padding). Nav items at 15px Rajdhani weight 500 #8b8d96 with 20px icons. Active item: #ffffff text with 3px #003791 left border. Section dividers 1px solid #2a2c36. Padding 16px throughout."
- "Design a platform badge: 'PS5' — #003791 background, white text, 11px Rajdhani weight 600 uppercase 1px letter-spacing, padding 3px 10px, border-radius 20px. 'PS4' — transparent bg, #003791 text, 1px solid #003791 border."
- "Create a PS symbol nav button: 44px circle, rgba(255,255,255,0.05) background, centered   symbol in #8b8d96. On hover: rgba(0,55,145,0.15) bg,    becomes #003791, subtle blue glow."

### Iteration Guide
1. Everything sits on `#1a1c23` deep navy — pure black is too harsh.
2. Three-surface layout is the signature: nav | content | detail. Start there.
3. Every interactive card must scale + reveal on hover. This is non-negotiable PlayStation UX.
4. PlayStation Blue (`#003791`) is the only accent. Gold (`#d4af37`) is PS Plus exclusive.
5. Use Rajdhani at weights 400-700. Same family, weight-driven hierarchy.
6. 12px border-radius minimum on cards. 16px on hero tiles. PlayStation is soft and premium.
7. Gradient background shifts between sections: `#1a1c23` → `#252840` → `#0f1013`.
8.   ,  ,  ,  symbols as iconic interactive elements — use them for carousel nav, confirm/cancel.
