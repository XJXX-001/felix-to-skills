# Design System: Ferrari

> **Implementation Notes**
>
> The original site uses proprietary Ferrari typefaces (Ferro Rosso, Ferrari Sans). For self-contained HTML output, use these CDN substitutes:
> - **Display:** `Playfair Display` (elegant high-contrast serif, replaces Ferro Rosso) | **Body:** `DM Sans` (clean geometric, replaces Ferrari Sans)
> - **Font stack (CSS):** `font-family: 'Playfair Display', 'Georgia', 'Times New Roman', serif;`
> - **Body stack (CSS):** `font-family: 'DM Sans', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;`
> ```html
> <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;0,900;1,400&family=DM+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
> ```
> Use standard file writing to create HTML. Serve via local server or deploy as needed.
> Verify visual accuracy in browser after generating.

## 1. Visual Theme & Atmosphere

Ferrari's digital presence is built on chiaroscuro — the Italian Renaissance technique of dramatic light-dark contrast. The canvas oscillates between absolute black (`#000000`) and pure white (`#ffffff`), with a single, searing accent: Ferrari Red (`#ff2800`). This is not a website; it's a cathedral to speed, and every pixel carries the weight of Maranello.

The defining element is the editorial photography: cars shot at low angles, in motion or posed against monumental architecture, with deep shadows that swallow detail into pure black. These images run full-bleed, bleeding edge to edge with zero containers. Text overlaid on dark images appears in white serif type with extreme sparseness — a single headline, sometimes just a model name. The Ferrari wordmark and prancing horse badge provide the only consistent brand anchors.

Typography is split between two worlds: the headline serif (Ferro Rosso, a custom high-contrast display face with razor-thin hairlines) for model names and campaign statements, and a clean geometric sans-serif for technical specifications and UI. The serif headlines are set at monumental sizes with tight tracking, evoking automotive badges and vintage racing posters. The shift from serif to sans-serif creates a deliberate tension between heritage (the prancing horse, Modena, Enzo) and modernity (F1 technology, carbon fiber, 1000hp hybrid systems).

The signature visual device is the extreme crop: a Ferrari photographed so close that the prancing horse badge fills half the frame, or a steering wheel detail shot that becomes abstract sculpture. Ferrari doesn't show you the whole car — it shows you desire.

**Key Characteristics:**
- Chiaroscuro: extreme black/white contrast with deep, light-swallowing shadows
- Ferrari Red (`#ff2800`) as the sole accent — a racing red that's unmistakable
- High-contrast display serif (Ferro Rosso style) for headlines — monumental, editorial
- Clean DM Sans for UI and technical copy — precise, modern
- Full-bleed editorial photography with extreme crops
- Zero border-radius — sharp, engineered, uncompromising
- The prancing horse as a floating brand anchor
- Sparse text — often just model name + single stat

## 2. Color Palette & Roles

### Primary
- **Ferrari Red** (`#ff2800`): The brand. CTAs, the prancing horse badge, the racing stripe, the heart of every Ferrari. A vibrant, slightly orange red — not burgundy, not crimson, but racing red. Used with surgical precision: one or two elements per page, never diluted.
- **Absolute Black** (`#000000`): Dark surfaces, photography backgrounds, footer, immersive sections. Not charcoal — true black.
- **Pure White** (`#ffffff`): Light surfaces, text on dark, the counterpoint to black.

### Accent & Variants
- **Red Dark** (`#d42000`): Darker red for hover states.
- **Yellow (Shield)** (`#ffcc00`): The yellow in the Ferrari shield logo. Used extremely sparingly — sometimes as a subtle detail or secondary accent on motorsport pages. Never for CTAs.
- **Red Glow** (`rgba(255,40,0,0.1)`): Subtle red ambient glow on hover states and featured cards.

### Text
- **Primary Text (Light BG)** (`#000000`): Headlines and body on white surfaces.
- **Secondary Text (Light BG)** (`#444444`): Muted text on white — dark enough for readability, not quite black.
- **Primary Text (Dark BG)** (`#ffffff`): Headlines and body on black.
- **Secondary Text (Dark BG)** (`#999999`): Muted text on dark surfaces.
- **Tertiary Text** (`#777777`): Fine print, legal, least important.

### Surface & Border
- **Light Surface** (`#ffffff`): Content sections on white background.
- **Off-White Surface** (`#f7f7f7`): Rare — only for specification sheets or data tables.
- **Border Light** (`#e0e0e0`): Subtle borders on light surfaces.
- **Border Dark** (`#333333`): Borders on dark surfaces.
- **Red Border** (`#ff2800`): Active/focus states — used sparingly.

## 3. Typography Rules

### Font Family
- **Display (Serif)**: `Ferro Rosso` (proprietary), fallback: `Playfair Display`
- **Body (Sans)**: `Ferrari Sans` (proprietary), fallback: `DM Sans`
- **Monospace**: `JetBrains Mono` for technical specs

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Mega Display | Playfair Display | 96-120px (6-7.5rem) | 900 | 0.85 | -1px | Model name — "SF90", "F80" |
| Hero Title | Playfair Display | 56-80px (3.5-5rem) | 900 | 0.9 | -0.5px | Campaign headlines |
| Display Quote | Playfair Display | 36-48px (2.25-3rem) | 400 italic | 1.1 | normal | Editorial pull quotes |
| Section Head | Playfair Display | 32-40px (2-2.5rem) | 700 | 1.1 | normal | Section titles |
| Subhead | DM Sans | 22-28px (1.4-1.75rem) | 300 | 1.3 | 0.5px | uppercase | Technical section labels |
| Body Large | DM Sans | 18px (1.125rem) | 400 | 1.6 | normal | Feature descriptions |
| Body | DM Sans | 16px (1rem) | 400 | 1.6 | normal | Standard reading |
| Body Small | DM Sans | 14px (0.875rem) | 400 | 1.5 | normal | Secondary body |
| Stat Value | DM Sans | 28-36px (1.75-2.25rem) | 300 | 1.1 | 0.3px | "1000 cv", "2.15 s" |
| Stat Label | DM Sans | 12px (0.75rem) | 500 | 1.2 | 1.5px | uppercase | "Power", "0-100 km/h" |
| Button Text | DM Sans | 14px (0.875rem) | 600 | 1.0 | 0.5px | uppercase | CTAs |
| Nav Link | DM Sans | 13px (0.81rem) | 500 | 1.0 | 1px | uppercase | Navigation |
| Caption | DM Sans | 11px (0.69rem) | 400 | 1.4 | normal | Legal |

### Principles
- **Display serif is the soul**: Model names and campaign headlines use a monumental, high-contrast serif at weight 900. The razor-thin hairlines against thick verticals create the tension between precision engineering and raw passion that defines Ferrari.
- **Uppercase sans-serif for UI**: All navigation, buttons, stat labels, and technical copy use DM Sans in uppercase with generous letter-spacing (0.5-1.5px). This is the precise, technical voice — the engineering department.
- **Italic for editorial moments**: The display serif in italic weight 400 appears for pull quotes and editorial text — a human, crafted counterpoint to the technical sans.
- **Extreme weight contrast**: 900 for serif display vs 300-400 for sans body. The gap is dramatic — heritage vs modernity in typographic form.
- **Stat panels as typographic compositions**: "1000 cv" at 36px weight 300 with "POWER" at 12px weight 500 above — each specification is a miniature typographic design.

## 4. Component Stylings

### Buttons

**Primary CTA (Red)**
- Background: `#ff2800`
- Text: `#ffffff`
- Padding: 14px 36px
- Radius: 0px (sharp — engineered, uncompromising)
- Font: 14px DM Sans weight 600, uppercase, letter-spacing 0.5px
- Hover: `#d42000` background, subtle scale(1.02)
- Transition: 0.3s ease
- Use: "Configure", "Discover", primary conversion

**Secondary (Outline — Dark BG)**
- Background: transparent
- Text: `#ffffff`
- Padding: 14px 36px
- Radius: 0px
- Border: `1.5px solid #ffffff`
- Font: 14px DM Sans weight 600, uppercase, letter-spacing 0.5px
- Hover: `#ffffff` background, `#000000` text

**Secondary (Outline — Light BG)**
- Background: transparent
- Text: `#000000`
- Padding: 14px 36px
- Radius: 0px
- Border: `1.5px solid #000000`
- Font: 14px DM Sans weight 600, uppercase, letter-spacing 0.5px
- Hover: `#000000` background, `#ffffff` text

**Text Link**
- Text: `#ff2800` with subtle underline animation
- Font: inherit
- Hover: underline extends

### Navigation
- Fixed top bar, 72px height
- Background: transparent on load → `rgba(0,0,0,0.85)` on scroll with `backdrop-filter: blur(16px)`
- Logo: Prancing Horse badge (left) + "FERRARI" wordmark
- Links: DM Sans 13px weight 500, uppercase, 1px letter-spacing
- Layout: Logo left | Model links center | Configurator/Dealers right
- Active state: Ferrari Red underline accent
- Mobile: hamburger → full-screen black overlay with centered links

### Hero Section
- Full-viewport image or video background
- Dark overlay (gradient: `rgba(0,0,0,0)` to `rgba(0,0,0,0.4)`) for text contrast
- Model name in mega serif: 120px Playfair Display weight 900, white, centered
- Single stat or tagline below in DM Sans uppercase
- One CTA — usually "Discover" or "Configure"
- Scrolling down transitions to next full-bleed experience

### Specification Panels
- Clean typographic layouts — no card containers
- Layout: horizontal row of stat blocks
- Each block: Stat label (12px DM Sans weight 500, uppercase, 1.5px spacing, `#999999`) + Stat value (32px DM Sans weight 300, `#ffffff` on dark / `#000000` on light)
- Separated by generous spacing (48-64px) or subtle vertical rules
- No borders, no backgrounds — pure typography

### Cards (Rare)
When cards appear (news, models, configurator options):
- Background: `#ffffff` (light) or `#111111` (dark)
- Border: none — cards are defined by content, not containers
- Image: full-bleed to card edge, no border-radius
- Text below image in clean DM Sans
- Hover: subtle red accent appears (underline or dot)

### Prandcing Horse Mark
- The Ferrari shield/SF badge functions as a punctuation mark
- Appears at section transitions, footer, or as a subtle watermark
- Size: 40-60px, always in Ferrari Red or monochrome
- Positioned as a floating element, not locked to grid

## 5. Layout Principles

### Spacing System
- Base unit: 8px
- Primary scale: 4px, 8px, 12px, 16px, 24px, 32px, 48px, 64px, 80px, 120px, 160px, 200px
- Section padding: 120-200px vertical
- Stat panel gaps: 48-64px between stats

### Layout Patterns
- **Full-bleed hero**: Photography fills the entire viewport. Minimal text overlay.
- **Chiaroscuro sections**: Deep shadow photography sections alternate with clean white typographic sections
- **Stat panels**: Horizontal rows of typographic stat blocks — no visual containers
- **Editorial spreads**: Image + text in asymmetric layouts, magazine-inspired
- **Model comparison**: Clean comparison tables with subtle row rules
- **Configurator**: Full-screen interactive — 3D model dominates, controls minimal

### Grid & Container
- Max content width: 1280px (when content is contained)
- Full-bleed: no container — images extend to viewport edges
- Text columns: centered, max 680px for editorial copy

### Whitespace Philosophy
- **Monumental breathing room**: 120-200px section padding. The emptiness around a Ferrari image is part of the reverence.
- **Content is sparse**: Ferrari's site might have 5-7 pieces of content per page. Each one gets a full viewing moment.
- **Scroll is ceremonial**: Each scroll position is a complete composition. You don't browse Ferrari — you experience it.

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Default) | No shadow, no elevation | Most content, photography |
| Image Overlay | Gradient `rgba(0,0,0,0)` → `rgba(0,0,0,0.4)` | Text legibility on images |
| Nav Overlay | `rgba(0,0,0,0.85)` + `backdrop-filter: blur(16px)` | Scrolled navigation |
| Red Glow | `0 0 40px rgba(255,40,0,0.1)` | Rare — on CTAs or featured cards |

**Flat by Default**: Ferrari uses almost no traditional elevation (shadows, cards, layers). The drama comes from the photography and typography, not from UI tricks. The only "elevation" is the navigation overlay and the image text gradient.

## 7. Do's and Don'ts

### Do
- Use Ferrari Red (`#ff2800`) with surgical precision — 1-2 elements per page maximum
- Use monumental serif (Playfair Display weight 900) at 96-120px for model names
- Use uppercase DM Sans with letter-spacing (0.5-1.5px) for all UI/technical text
- Let photography run full-bleed to viewport edges
- Use extreme contrast: pure black vs pure white, monumental serif vs technical sans
- Keep text sparse — often just a model name and one stat
- Use the prancing horse as punctuation, not decoration
- Use 0px border-radius everywhere — sharp, engineered, Italian

### Don't
- Don't use rounded corners — Ferrari is sharp, precise, uncompromising
- Don't dilute the red — it's the only accent color, keep it scarce
- Don't use multiple typefaces beyond serif (brand) + sans (technical)
- Don't use card containers for content — Ferrari's content lives free on the surface
- Don't over-explain — the photography should do 80% of the communication
- Don't use shadows or elevation tricks — the drama is in the imagery
- Don't use gradients as decorative elements — only for text contrast overlays
- Don't use warm/accent colors other than red — yellow shield detail is motorsport-only

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <768px | Stacked single-column, reduced serif size |
| Tablet | 768-1024px | 2-column layouts where used, moderate type |
| Desktop | 1024-1280px | Full layout, full type scale |
| Large Desktop | >1280px | Generous margins, maximum image impact |

### Collapsing Strategy
- Mega display: 120px → 64px → 42px, maintaining weight 900 serif
- Full-bleed photography: maintains edge-to-edge at all sizes
- Stat panels: horizontal row → 2-column stack → single column
- Navigation: full desktop nav → simplified → hamburger menu
- CTAs: full-width on mobile, centered
- Section padding: 200px → 120px → 64px

### Image Behavior
- Photography: `object-fit: cover` with focal point on vehicle
- Extreme crops may tighten or loosen based on viewport
- Prancing horse badge: scales proportionally, never drops below 32px

## 9. Agent Prompt Guide

### Quick Color Reference
- Ferrari Red: `#ff2800`
- Red Hover: `#d42000`
- Black: `#000000`
- White: `#ffffff`
- Primary Text (dark bg): `#ffffff`
- Secondary Text (dark bg): `#999999`
- Primary Text (light bg): `#000000`
- Secondary Text (light bg): `#444444`
- Border (light): `#e0e0e0`
- Border (dark): `#333333`
- Image Overlay: `rgba(0,0,0,0)` to `rgba(0,0,0,0.4)` gradient

### Example Component Prompts
- "Create a Ferrari hero: full-bleed dark automotive photography. Model name 'SF90 STRADALE' at 96px Playfair Display weight 900, letter-spacing -1px, color #ffffff, centered near bottom. Tagline '1000 cv' below at 14px DM Sans weight 600 uppercase letter-spacing 0.5px #999999. Red CTA 'DISCOVER' — #ff2800 bg, white text, 0px radius, 14px 36px padding, DM Sans weight 600 uppercase."
- "Build a stat panel: horizontal row of 4 stat blocks on black background. Each: label 'POWER' at 12px DM Sans weight 500 uppercase 1.5px letter-spacing #999999 + value '1000 cv' at 32px DM Sans weight 300 #ffffff. 64px gaps between blocks. No borders, no containers."
- "Create Ferrari navigation: 72px fixed bar, transparent on load → rgba(0,0,0,0.85) on scroll with backdrop-filter blur(16px). Prancing horse badge (40px) left + 'FERRARI' wordmark. Links in 13px DM Sans weight 500 uppercase 1px letter-spacing. Active link gets #ff2800 underline."
- "Design an editorial section: white background. Left: 48px Playfair Display weight 400 italic quote in #000000. Right: 16px DM Sans weight 400 body in #444444. Clean separation — no borders, generous whitespace."
- "Create an outline CTA: transparent bg, 1.5px solid #ffffff border, 0px radius, 14px 36px padding, DM Sans 14px weight 600 uppercase 0.5px letter-spacing, white text. Hover: #ffffff bg, #000000 text."

### Iteration Guide
1. Model names in monumental serif (Playfair Display 900) at 96-120px. This is non-negotiable.
2. All UI text in uppercase DM Sans with 0.5-1.5px letter-spacing.
3. Ferrari Red (#ff2800) appears 1-2 times per page. Never more. Scarcity = power.
4. 0px border-radius everywhere. Ferrari is Italian sharpness, not softness.
5. Let photography do the work — text is sparse, just model name + one stat + one CTA.
6. Use the prancing horse as a floating punctuation mark — a 40-60px badge at section transitions.
7. Black and white are the only surfaces. No grays (except for secondary text).
8. Extreme crops: show the badge, the wheel, the exhaust — not always the whole car.
