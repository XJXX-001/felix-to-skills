# Design System: Tesla

> **Implementation Notes**
>
> The original site uses proprietary Universal Sans. For self-contained HTML output, use these CDN substitutes:
> - **Primary:** `Inter` | **Display:** `Inter` (light weights)
> - **Font stack (CSS):** `font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;`
> - **Mono stack (CSS):** `font-family: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;`
> ```html
> <link href="https://fonts.googleapis.com/css2?family=Inter:wght@200;300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
> ```
> Use standard file writing to create HTML. Serve via local server or deploy as needed.
> Verify visual accuracy in browser after generating.

## 1. Visual Theme & Atmosphere

Tesla's website embodies "radical subtraction" — the design philosophy that every element must fight for its right to exist. The canvas is pure black (`#000000`) or pure white (`#ffffff`), with no gradients, no decorative flourishes, no box shadows on primary surfaces. Content flows through full-viewport photography that acts as both hero image and background, with minimal text floating on top like HUD elements. The result feels less like a website and more like a cinematic interface for a vehicle OS.

Where most automotive sites bury visitors in chrome trim and configurator widgets, Tesla gives you a single vehicle image and a single CTA: "Order Now." The restraint is the brand. Navigation sits as a thin overlay bar — semi-transparent on initial load, fading to solid on scroll. Type runs in Inter at extremely light weights (200-300), with generous letter-spacing that reads as technological and premium. The entire experience communicates: we don't need to persuade you. The product speaks.

The signature visual device is the full-viewport car photograph: a Model S/Y/3 against a stark background, positioned dead-center, with just two lines of text and a button. This repeats section by section — each feature gets its own full-viewport moment. No cards, no columns, no grids. Just the car, the stat, and the next scroll.

**Key Characteristics:**
- Binary light/dark surface system — no intermediate grays, no tints
- Full-viewport photography as the primary layout device — one image per section
- Minimal overlay text: headline + stat + single CTA
- No card components, no shadows, no borders — radical flatness
- Inter at weight 200-300 for headlines, weight 400 for body
- Generous letter-spacing (0.5-1.5px) on all display text
- Horizontal scroll for vehicle comparison sections
- Zero border-radius — every element is sharp-edged

## 2. Color Palette & Roles

### Primary
- **Tesla Black** (`#000000`): Primary dark surface. Hero backgrounds, footer, dark-mode sections. Not a dark gray — true black.
- **Tesla White** (`#ffffff`): Primary light surface. Content sections, light-mode backgrounds. Not off-white — pure white.
- **Tesla Red** (`#e82127`): Brand accent. CTA buttons, interactive elements, the iconic Tesla "T" in specific contexts. Used extremely sparingly — often only appears in the CTA and the badge.

### Text
- **Primary Text (Light BG)** (`#171717`): Body and heading text on white surfaces. Near-black for readability without harshness.
- **Secondary Text (Light BG)** (`#393c41`): Subtitle text, specs, secondary information.
- **Primary Text (Dark BG)** (`#ffffff`): Text on black surfaces.
- **Secondary Text (Dark BG)** (`#a2a3a5`): Muted text on dark surfaces — a cool gray that stays legible.

### Interactive
- **Accent Red** (`#e82127`): Primary CTA color. Used exclusively for "Order Now" buttons and key interactive moments.
- **Red Hover** (`#c91a1f`): Darker red for button hover states.
- **Link Blue** (`#3e6ae1`): Inline links on light backgrounds. Tesla blue — cold, technical, distinct from the warm red.

### Neutral
- **Border Light** (`#e2e3e3`): Subtle borders on light surfaces — nearly invisible.
- **Border Dark** (`#393c41`): Borders on dark surfaces.
- **Overlay Dark** (`rgba(0,0,0,0.4)`): Semi-transparent overlay for text legibility on hero images.
- **Overlay Light** (`rgba(255,255,255,0.1)`): Subtle light overlay for dark mode separators.

### No Tints, No Gradients
Tesla uses exactly zero gradients, zero opacity-layered color blocks, and zero tinted backgrounds. The color system is binary: black, white, red, and the transparency needed for image overlays. This is the most austere palette of any major brand website.

## 3. Typography Rules

### Font Family
- **Primary**: `Universal Sans` (proprietary), fallback: `Inter`
- **Monospace**: `JetBrains Mono` for technical specs

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Hero Display | Inter | 40-48px (2.5-3rem) | 300 | 1.15 | 0.5px | Vehicle name, main stat |
| Section Heading | Inter | 28-34px (1.75-2.1rem) | 300 | 1.2 | 0.3px | Feature section titles |
| Subheading | Inter | 20-24px (1.25-1.5rem) | 300 | 1.3 | 0.2px | Secondary headings |
| Body Large | Inter | 17px (1.06rem) | 400 | 1.5 | normal | Feature descriptions |
| Body | Inter | 14-15px (0.875-0.94rem) | 400 | 1.5 | normal | Standard reading text |
| Spec Label | Inter | 12px (0.75rem) | 500 | 1.3 | 0.5px | uppercase | Range, acceleration, specs |
| Spec Value | Inter | 24-28px (1.5-1.75rem) | 300 | 1.2 | 0.3px | "396 mi", "1.99 s" |
| Button Text | Inter | 14px (0.875rem) | 500 | 1.0 | 0.5px | CTA buttons |
| Nav Link | Inter | 14px (0.875rem) | 500 | 1.0 | 0.3px | Navigation items |
| Caption | Inter | 12px (0.75rem) | 400 | 1.4 | normal | Legal, footnotes |
| Mono Spec | JetBrains Mono | 13px (0.81rem) | 400 | 1.5 | normal | Technical data |

### Principles
- **Weight 300 as the voice**: Tesla headlines use weight 300 — lighter than most, creating a technological, precise feel. Never bold. Never weight 600+.
- **Positive letter-spacing**: Unlike most brands that track tight, Tesla adds spacing (0.2-0.5px on display text). This creates breathing room that reads as premium and unhurried.
- **Uppercase specs sparingly**: "RANGE", "0-60 MPH", "TOP SPEED" appear in uppercase weight 500 at 12px with 0.5px tracking. Values directly below in weight 300 at 28px.
- **No fancy typography**: No OpenType stylistic sets, no alternate glyphs, no ligature tricks. The type is so restrained it becomes the absence of design — pure information architecture.
- **Monospace for technical data only**: JetBrains Mono appears exclusively in spec comparison tables and technical details — never in marketing copy.

## 4. Component Stylings

### Buttons

**Primary CTA (Red)**
- Background: `#e82127` (on hover: `#c91a1f`)
- Text: `#ffffff`
- Padding: 12px 32px
- Radius: 4px (Tesla's only rounded element)
- Font: 14px Inter weight 500, letter-spacing 0.5px
- Border: none
- Use: "Order Now", "Demo Drive" — only 1-2 per page, never repeating

**Secondary (Outline)**
- Background: transparent
- Text: `#171717` (light bg) or `#ffffff` (dark bg)
- Padding: 12px 32px
- Radius: 4px
- Border: `3px solid #171717` (light bg) or `3px solid #ffffff` (dark bg)
- Font: 14px Inter weight 500, letter-spacing 0.5px
- Hover: background fills to `#171717` (light) or `#ffffff` (dark), text inverts
- Use: "Learn More", "Compare" — secondary actions

**Text Link**
- No background, no border
- Text: `#3e6ae1` with underline on hover
- Font: inherit
- Use: inline links in body copy

### Navigation
- Fixed top bar, 56px height, full-width
- Background: `rgba(0,0,0,0)` initially → `#ffffff` (or `#000000` on dark pages) on scroll with `backdrop-filter: blur(12px)`
- Logo: Centered SVG Tesla "T" logo
- Links: Inter 14px weight 500, letter-spacing 0.3px
- Layout: Vehicle models (left) | Logo (center) | Shop/Account/Menu (right)
- No dropdowns on desktop — persistent visible links
- Mobile: hamburger menu with slide-out overlay

### Spec Panels
- Horizontal row of spec cards, no visible card boundaries
- Each spec: label (12px uppercase weight 500) + value (28px weight 300)
- Separated by thin vertical rules or generous spacing
- No background, no border, no shadow — pure text on surface

### Vehicle Comparison
- Horizontal scroll container with snap points
- Each vehicle: image + name + starting price
- Active vehicle: slightly larger, more prominent
- Smooth scroll behavior, no pagination dots

### Image Treatment
- Full-viewport images: `object-fit: cover`, `width: 100vw`, `height: 100vh` (or proportional)
- No border-radius — images bleed edge-to-edge
- No overlays except semi-transparent black for text contrast
- Car photography: 3/4 front angle on white/black seamless background
- Interior photography: wide-angle, clean, minimal staging

## 5. Layout Principles

### Spacing System
- Base unit: 8px
- Scale: 4px, 8px, 12px, 16px, 24px, 32px, 48px, 64px, 96px, 128px
- Sections: minimum 80px vertical padding, often 120-160px
- Section margins: generous but consistent — 80-120px between major sections

### Layout Pattern
- **Single-column, full-width**: Tesla rejects multi-column layouts in favor of a vertical narrative. Each section is a full-viewport statement.
- **Hero**: Full-viewport vehicle image + centered headline + single CTA
- **Specs bar**: Horizontal stats row — no card containers, just aligned text
- **Feature sections**: Alternating image + text, each full-viewport or near-full
- **Comparison**: Horizontal scroll with snap — the one place Tesla breaks vertical flow
- **Footer**: Black background, dense link columns, minimal branding

### Grid & Container
- Content max-width: `1200px` for text/content sections
- Full-bleed images: `100vw` with no container constraint
- Text column: centered, max 720px for body copy

### Whitespace Philosophy
- **Breathing room is the luxury**: Spacing is Tesla's primary design tool. Generous margins and padding signal premium without ornament.
- **One thing per screen**: Each scroll position presents exactly one message — a vehicle, a feature, a stat. No competing CTAs or sidebars.
- **Horizontal movement is rare**: Scrolling is vertical. Horizontal scroll only for vehicle comparison — and even that is contained.

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Default) | No shadow, no border | All content surfaces, navigation (after scroll) |
| Overlay | `rgba(0,0,0,0.4)` gradient | Text contrast on hero images |
| Menu Overlay | `rgba(255,255,255,0.98)` | Mobile menu background |
| Border Only | `3px solid` for buttons | The only visual "elevation" — button borders |

**No Shadow Philosophy**: Tesla uses zero box shadows in its core design. Elevation is communicated through:
1. **Opacity overlays** — navigation transitions from transparent to solid
2. **Border thickness** — 3px borders on outline buttons signal solidity
3. **Content contrast** — dark sections alternated with light sections create depth through color
4. **Image scale** — full-bleed images feel monumental, creating depth through scale

This is the most aggressively flat elevation system of any major brand. Cards don't exist. Modals are rare. Everything sits directly on the surface.

## 7. Do's and Don'ts

### Do
- Use weight 300 for all headlines — lightness is the brand voice
- Use pure black (`#000000`) and pure white (`#ffffff`) as the only surface colors
- Add letter-spacing (0.2-0.5px) to all display text — breathing room is premium
- Use one CTA per viewport — never stack competing actions
- Let images bleed edge-to-edge with no border-radius
- Use the red accent (`#e82127`) only for primary CTAs — scarcity creates impact
- Keep navigation minimal — 5-8 links maximum
- Use 3px borders (not 1px) for outline buttons — substance over delicacy

### Don't
- Don't use box shadows — Tesla is radically flat
- Don't use card components — there are no cards in Tesla's design system
- Don't use gradients — binary black/white only
- Don't use weight 600+ for any text — the brand speaks in light weights
- Don't use border-radius except on buttons (4px only)
- Don't use multi-column layouts for marketing content — vertical narrative only
- Don't use more than one CTA color — red is reserved for primary action
- Don't tint backgrounds — gray doesn't exist in the Tesla palette
- Don't use decorative icons or illustrations — photography is the only imagery

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <768px | Stacked single-column, reduced type scale, simpler nav |
| Tablet | 768-1024px | Same single-column, larger type |
| Desktop | 1024-1440px | Full layout, full-viewport images |
| Large Desktop | >1440px | Centered with generous margins, larger images |

### Collapsing Strategy
- Hero images: maintain full-bleed at all sizes, text overlays reposition to bottom
- Navigation: horizontal links → hamburger menu with slide-out
- Spec panels: horizontal row → stacked 2-column grid → single column
- Vehicle comparison: horizontal scroll maintained, touch-friendly snap
- Button pairs: stack vertically on mobile (Order Now above Learn More)
- Type scale: 40px hero → 32px tablet → 28px mobile, weight 300 maintained
- Section spacing: 120px → 80px → 48px across breakpoints

### Image Behavior
- Hero images: `object-fit: cover` with strategic focal points for mobile crop
- No lazy-load distortion — images maintain aspect ratio
- Vehicle photography: center-framed, works at all crop ratios
- Interior shots: may switch to tighter crops on mobile

## 9. Agent Prompt Guide

### Quick Color Reference
- Primary CTA: Tesla Red (`#e82127`)
- CTA Hover: Dark Red (`#c91a1f`)
- Light Surface: Pure White (`#ffffff`)
- Dark Surface: Pure Black (`#000000`)
- Primary Text (light): Near Black (`#171717`)
- Secondary Text (light): Gray (`#393c41`)
- Primary Text (dark): White (`#ffffff`)
- Secondary Text (dark): Cool Gray (`#a2a3a5`)
- Link: Tesla Blue (`#3e6ae1`)
- Border (light): `#e2e3e3`
- Border (dark): `#393c41`
- Image Overlay: `rgba(0,0,0,0.4)`

### Example Component Prompts
- "Create a Tesla-style hero: full-viewport dark image background with object-fit cover. Headline 'Model S' at 48px Inter weight 300, letter-spacing 0.5px, color #ffffff, centered. Subtitle 'Plaid' below. Single red CTA button 'Order Now' — #e82127 background, white text, 4px radius, 12px 32px padding. No other elements."
- "Create a spec bar: horizontal row of spec panels on white background. Each: label 'RANGE' at 12px Inter weight 500 uppercase #393c41, value '396 mi' at 28px Inter weight 300 #171717. No borders, no backgrounds, no shadows — pure text aligned in row."
- "Build navigation: fixed top bar 56px, initially transparent, on-scroll becomes white with backdrop-filter blur(12px). Logo centered. Model links left in Inter 14px weight 500 #171717. No dropdowns. Mobile: hamburger toggle."
- "Design a feature section: half-viewport image left, text right. Headline 28px weight 300, body 15px weight 400 #393c41. Outline button 'Learn More' — transparent bg, 3px solid #171717 border, 4px radius, 12px 32px padding. Hover fills to #171717 with white text."
- "Create an outline button: transparent background, 3px solid border (not 1px — Tesla uses thickness as design signal), 4px radius, 12px 32px padding, Inter 14px weight 500, letter-spacing 0.5px. On light bg: border #171717, text #171717. On dark bg: border #ffffff, text #ffffff."

### Iteration Guide
1. Start with black or white — no gray backgrounds ever
2. Weight 300 for all headlines, weight 400-500 for UI text
3. Add 0.2-0.5px letter-spacing to all display text — breathing room is premium
4. Use 3px borders on outline buttons (not 1px) — Tesla's only visual "weight"
5. One CTA per viewport, always red (`#e82127`), never diluted with secondary red elements
6. Zero shadows, zero cards, zero gradients — radical flatness
7. Full-viewport photography as the primary layout device — images drive the scroll
8. Navigation: transparent → solid on scroll with blur backdrop
9. Spec panels: pure text rows with no container — the opposite of cards
