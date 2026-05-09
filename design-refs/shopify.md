# Design System: Shopify

> **Implementation Notes**
>
> The original site uses proprietary Shopify Sans (Monotype). For self-contained HTML output, use these CDN substitutes:
> - **Primary/Display:** `Inter` (clean, neutral, geometric) | **Body:** `Inter`
> - **Font stack (CSS):** `font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;`
> - **Mono stack (CSS):** `font-family: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;`
> ```html
> <link href="https://fonts.googleapis.com/css2?family=Inter:wght@200;300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
> ```
> Use standard file writing to create HTML. Serve via local server or deploy as needed.
> Verify visual accuracy in browser after generating.

## 1. Visual Theme & Atmosphere

Shopify's digital presence is dark-first cinematic e-commerce — a bold departure from the white-background convention of shopping platforms. The canvas opens on deep charcoal (`#121212`) or true black (`#000000`), with a signature neon green (`#95bf47`) that functions as both brand anchor and conversion accelerator. This isn't the dark mode of a developer tool — it's a cinematic, art-directed dark that makes products glow like they're on display in a gallery after hours.

The type system uses extremely light display weights (200-300) for headlines, creating an ethereal, almost editorial quality that contrasts sharply with the dark background. Headlines float in white at ultra-light weight with generous letter-spacing — the opposite of Nike's shouted urgency. This is sophisticated e-commerce: the product is the star, the platform is the stage but doesn't upstage.

Photography runs full-bleed against the dark background, with products breaking out of their frames. Gradient overlays transition from dark backgrounds into bright product photography, creating cinematic reveals. Cards on dark backgrounds feature subtle borders and soft inner glows. The neon green accent appears sparingly but decisively — in CTAs, in the Shopify "bag" icon, in hover states. It's the green of growth, commerce, and momentum.

**Key Characteristics:**
- Dark-first: `#121212` and `#000000` as primary surfaces
- Signature neon green (`#95bf47`) as the solo accent — fresh, growth-oriented
- Ultra-light display weights (200-300) for headlines — ethereal, editorial
- Full-bleed product photography on dark backgrounds
- Gradient overlays and soft glows for cinematic depth
- Generous, airy spacing — luxury breathing room
- Large border-radius (12-16px) on cards — soft, welcoming
- The Shopify "bag" icon in neon green — instantly recognizable

## 2. Color Palette & Roles

### Primary
- **Shopify Green** (`#95bf47`): The brand. CTAs, bag icon, interactive highlights, success states. A distinctive yellow-green — not teal, not lime, unmistakably Shopify.
- **Dark Surface** (`#121212`): Primary dark background. Slightly lifted from true black for depth.
- **Deep Black** (`#000000`): Deeper sections, hero backgrounds, footer.
- **White** (`#ffffff`): Text on dark, light-mode surfaces when used.

### Accent & Gradient
- **Green Dark** (`#7aa837`): Darker green for hover states.
- **Green Gradient Start** (`#95bf47`): Gradient beginning.
- **Green Gradient End** (`#5e8e2e`): Gradient end for immersive sections.
- **Green Glow** (`rgba(149,191,71,0.15)`): Soft ambient glow behind CTAs and featured elements.

### Text Scale
- **Primary Text (Dark BG)** (`#ffffff`): Headlines and key body.
- **Secondary Text (Dark BG)** (`#a0a0a0`): Secondary body, metadata.
- **Tertiary Text (Dark BG)** (`#666666`): Captions, fine print.
- **Primary Text (Light BG)** (`#121212`): When light mode is used.
- **Secondary Text (Light BG)** (`#666666`): When light mode is used.

### Surface & Border
- **Card Surface** (`#1a1a1a`): Slightly lighter than background for card distinction.
- **Card Border** (`#333333`): Subtle borders on dark cards.
- **Card Border Hover** (`#95bf47`): Green border on card hover — the conversion signal.
- **Divider** (`#2a2a2a`): Section dividers on dark backgrounds.
- **Input Background** (`#1a1a1a`): Dark input fields.
- **Input Border** (`#333333`): Dark input borders.
- **Input Focus** (`#95bf47`): Green focus ring.

### Shadow & Glow
- **Card Glow** (`0 0 30px rgba(149,191,71,0.08)`): Ambient green glow on featured content.
- **Elevation Shadow** (`0 8px 32px rgba(0,0,0,0.4)`): Card elevation on dark backgrounds.

## 3. Typography Rules

### Font Family
- **Primary**: `Shopify Sans` (proprietary, Monotype), fallback: `Inter`
- **Display**: `Shopify Sans Display` — ultra-light weights for headlines
- **Monospace**: `JetBrains Mono` for code, technical copy

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Hero Display | Inter | 64-80px (4-5rem) | 200 | 1.05 | -0.5px | Maximum impact display |
| Display Large | Inter | 48-56px (3-3.5rem) | 200 | 1.1 | -0.3px | Section heroes |
| Heading 1 | Inter | 36-44px (2.25-2.75rem) | 300 | 1.15 | normal | Major section heads |
| Heading 2 | Inter | 28-34px (1.75-2.1rem) | 300 | 1.2 | normal | Subsection heads |
| Heading 3 | Inter | 20-26px (1.25-1.6rem) | 400 | 1.25 | normal | Card titles |
| Body Large | Inter | 18-20px (1.125-1.25rem) | 400 | 1.6 | normal | Featured body |
| Body | Inter | 16px (1rem) | 400 | 1.6 | normal | Standard reading |
| Body Small | Inter | 14px (0.875rem) | 400 | 1.5 | normal | Secondary body |
| Button Large | Inter | 16px (1rem) | 600 | 1.0 | normal | Primary CTA |
| Button Small | Inter | 14px (0.875rem) | 600 | 1.0 | normal | Secondary CTA |
| Nav Link | Inter | 15px (0.94rem) | 500 | 1.0 | normal | Navigation |
| Caption | Inter | 12px (0.75rem) | 400 | 1.4 | 0.3px | Labels, metadata |
| Overline | Inter | 11px (0.69rem) | 600 | 1.2 | 1.5px | uppercase | Category labels |

### Principles
- **Ultra-light display as signature**: Weight 200 headlines are Shopify's most distinctive choice. Where others use bold to command, Shopify uses lightness to create sophistication. The headline feels like it's projected onto the dark background rather than printed on it.
- **Weight contrast**: Headlines at 200-300, UI at 400-600. The gap between display and utility creates clear information hierarchy without relying on size alone.
- **Generous leading**: Body text at 1.5-1.6 line-height — editorial breathing room that matches the cinematic dark aesthetic.
- **Uppercase overline with wide tracking**: Category labels at 11px weight 600, 1.5px letter-spacing, uppercase. Used sparingly above headlines for context.
- **Single weight system in display**: Unlike brands that mix weights within headlines, Shopify keeps display text pure — one weight per element.

## 4. Component Stylings

### Buttons

**Primary CTA (Green)**
- Background: `#95bf47`
- Text: `#121212` (dark text on green — not white)
- Padding: 14px 32px
- Radius: 8px (rounded — friendly, modern)
- Font: 16px Inter weight 600
- Box Shadow: `0 0 20px rgba(149,191,71,0.2)` — ambient green glow
- Hover: `#7aa837` background, glow intensifies
- Use: "Start free trial", "Add to cart", primary conversion actions

**Secondary (Dark)**
- Background: `#1a1a1a`
- Text: `#ffffff`
- Padding: 14px 32px
- Radius: 8px
- Border: `1px solid #333333`
- Font: 16px Inter weight 500
- Hover: `#333333` background
- Use: "Learn more", secondary actions

**Ghost**
- Background: transparent
- Text: `#ffffff`
- Padding: 14px 32px
- Radius: 8px
- Font: 16px Inter weight 500
- Hover: `rgba(255,255,255,0.05)` background
- Use: Tertiary actions, navigation CTAs

**Icon Button**
- Background: transparent
- Size: 44px × 44px
- Radius: 8px
- Hover: `rgba(255,255,255,0.1)` background
- Use: Bag icon, search, menu toggle

### Cards
- Background: `#1a1a1a`
- Border: `1px solid #333333`
- Radius: 12px (generous — inviting, soft)
- Padding: 24-32px
- Hover: border shifts to `#95bf47`, subtle green glow `0 0 30px rgba(149,191,71,0.08)`
- Image: top-aligned, border-radius 12px 12px 0 0 if flush with card edges
- Shadow: `0 4px 24px rgba(0,0,0,0.3)`

### Navigation
- Fixed top bar, dark background (`rgba(18,18,18,0.8)`), `backdrop-filter: blur(20px)`
- Height: 64px
- Logo: Shopify wordmark, left
- Links: Inter 15px weight 500, `#a0a0a0`, hover to `#ffffff`
- Active link: `#ffffff` with subtle green underline accent
- CTA: "Start free trial" green button, right-aligned
- Mobile: hamburger → full-screen dark overlay with centered links

### Input & Forms
- Background: `#1a1a1a`
- Border: `1px solid #333333`
- Radius: 8px
- Padding: 12px 16px
- Text: `#ffffff`, 16px Inter weight 400
- Placeholder: `#666666`
- Focus: `2px solid #95bf47`, green ambient glow
- Label: `#a0a0a0`, 14px weight 400, above input

### Tags & Badges
- Background: `rgba(149,191,71,0.1)`
- Text: `#95bf47`
- Padding: 4px 12px
- Radius: 20px (pill)
- Font: 12px Inter weight 500

### Dividers
- `1px solid #2a2a2a`
- Full width or inset
- Use: section separation, card content separation

## 5. Layout Principles

### Spacing System
- Base unit: 8px
- Scale: 4px, 8px, 12px, 16px, 24px, 32px, 48px, 64px, 80px, 96px, 120px, 160px
- Section padding: 80-160px vertical
- Card gaps: 24-32px

### Layout Patterns
- **Hero**: Full-bleed dark background + ultra-light headline + green CTA. Photography element breaking the frame.
- **Feature grid**: 3-column card layout, generous 32px gaps
- **Alternating sections**: Dark section → featured product (dark bg, product photography) → dark section → testimonial
- **Gradient reveals**: Sections transition via gradient overlays — dark fades into product imagery
- **Footer**: Darkest section (`#000000`), multi-column, minimal color

### Grid & Container
- Max content width: 1200px
- 12-column grid, 32px gutter
- Content centered with generous side margins

### Whitespace Philosophy
- **Air is luxury**: Shopify uses dramatic whitespace — 120-160px section padding, 32px card gaps. The emptiness makes the green accents and product photography feel more significant.
- **Content density is low**: Unlike traditional e-commerce, Shopify's own site is sparse. One message per section, one product per hero.
- **Dark background absorbs**: The dark background makes whitespace feel even more expansive — content floats rather than sits.

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Default) | `#121212` background | Page base |
| Card (Level 1) | `#1a1a1a` bg + `0 4px 24px rgba(0,0,0,0.3)` | Standard cards |
| Elevated (Level 2) | `#1a1a1a` bg + `0 8px 32px rgba(0,0,0,0.4)` | Featured cards, modals |
| Glow (Level 3) | Ambient green glow `0 0 30px rgba(149,191,71,0.08)` | CTAs, hover states |
| Focus | `2px solid #95bf47` + green glow | Input focus, keyboard nav |

**Depth Philosophy**: On dark backgrounds, elevation is created through:
1. **Lighter surfaces** — `#1a1a1a` cards float above `#121212` background
2. **Dark shadows** — `rgba(0,0,0,0.4)` creates depth that's visible against the dark background
3. **Green glow** — ambient neon green light adds an ethereal, technological depth
4. **Backdrop blur** — nav bar uses `backdrop-filter: blur(20px)` for frosted glass elevation

## 7. Do's and Don'ts

### Do
- Use dark backgrounds as the default — `#121212` is the canvas, not a mode
- Use ultra-light weight 200-300 for display headlines — ethereal sophistication
- Use green (`#95bf47`) exclusively for primary CTAs and key brand moments
- Use generous border-radius (8-12px on cards, 8px on buttons) — soft and friendly
- Add ambient green glow to primary CTAs — the signature Shopify effect
- Use gradient overlays for section transitions — cinematic reveals
- Keep body text at generous line-height (1.5-1.6) — editorial breathing room
- Use `#1a1a1a` cards on `#121212` background — subtle elevation through color

### Don't
- Don't use white backgrounds as the default — Shopify is dark-first
- Don't use bold weights (700+) for headlines — the brand voice is light and sophisticated
- Don't overuse green — it loses impact if diluted across too many elements
- Don't use sharp corners — Shopify is inviting, use 8px+ radius
- Don't use the green accent for body text or non-interactive elements
- Don't use multi-colored accent systems — green is the only accent color
- Don't use box shadows with gray tints — shadows should be pure black with opacity
- Don't crowd content — Shopify's own site is sparse and cinematic

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <768px | Single column, stacked layout |
| Tablet | 768-1024px | 2-column grids, reduced type |
| Desktop | 1024-1440px | Full layout, full type scale |
| Large Desktop | >1440px | Generous margins |

### Collapsing Strategy
- Hero display: 64px → 40px → 32px, maintaining weight 200
- Feature cards: 3 columns → 2 → 1 stacked
- Navigation: horizontal → hamburger overlay
- Section padding: 120px → 80px → 48px
- CTAs: full-width on mobile, inline on desktop
- Green glow: subtle on all sizes, proportionally sized

### Image Behavior
- Product photography: center-cropped, maintains dark background context
- Full-bleed: extends to viewport edges on all sizes
- Gradient overlays: maintain direction, adjust opacity for smaller screens

## 9. Agent Prompt Guide

### Quick Color Reference
- Primary CTA: Shopify Green (`#95bf47`)
- CTA Hover: Dark Green (`#7aa837`)
- Dark Surface: `#121212`
- Deep Black: `#000000`
- Card Surface: `#1a1a1a`
- Primary Text: `#ffffff` (dark bg) / `#121212` (light bg)
- Secondary Text: `#a0a0a0`
- Tertiary Text: `#666666`
- Card Border: `#333333`
- Card Border Hover: `#95bf47`
- Input Border: `#333333`
- Focus: `#95bf47`
- Green Glow: `rgba(149,191,71,0.15)`
- Divider: `#2a2a2a`

### Example Component Prompts
- "Create a Shopify hero: #121212 full-viewport background. Headline 'The global commerce platform' at 64px Inter weight 200, letter-spacing -0.5px, color #ffffff, centered. Subtitle at 18px weight 400 #a0a0a0. Green CTA 'Start free trial' — #95bf47 bg, #121212 text, 8px radius, box-shadow 0 0 20px rgba(149,191,71,0.2). Product image floating with gradient overlay from dark to transparent."
- "Build a Shopify card: #1a1a1a background, 1px solid #333333 border, 12px radius, 24px padding. Title at 24px Inter weight 300 #ffffff. Body at 16px weight 400 #a0a0a0. Footer CTA in #95bf47. On hover: border shifts to #95bf47, box-shadow 0 0 30px rgba(149,191,71,0.08)."
- "Create dark navigation: fixed top bar, 64px, background rgba(18,18,18,0.8) with backdrop-filter blur(20px). Logo left. Links in 15px Inter weight 500 #a0a0a0, hover #ffffff. Green 'Start free trial' CTA right, 8px radius."
- "Design a dark input: #1a1a1a background, 1px solid #333333 border, 8px radius, 12px 16px padding. Placeholder text #666666. On focus: 2px solid #95bf47 border, box-shadow 0 0 10px rgba(149,191,71,0.1). Label above in 14px #a0a0a0."
- "Create a green glow CTA: #95bf47 background with 8px radius, #121212 text, 14px 32px padding. box-shadow: 0 0 20px rgba(149,191,71,0.2). On hover: #7aa837 bg, glow intensifies."

### Iteration Guide
1. Every surface is dark (#121212) unless explicitly overridden. White backgrounds are the exception.
2. Display headlines at weight 200 — ultra-light is the brand's typographic signature.
3. Green (#95bf47) only for CTAs, bag icon, and interactive states. Never for body text.
4. Use color-based elevation: lighter dark (#1a1a1a) floats above darker background (#121212).
5. 8-12px border-radius everywhere — sharp corners don't exist in Shopify's soft, cinematic world.
6. Add green glow (0 0 20-30px rgba(149,191,71,0.08-0.2)) to elevated or hovered interactive elements.
7. Generous spacing: 24-32px card gaps, 80-160px section padding, 1.5-1.6 body line-height.
8. One accent color, one surface color family (dark grays), one type family — elegant restraint.
