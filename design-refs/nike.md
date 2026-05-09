# Design System: Nike

> **Implementation Notes**
>
> The original site uses proprietary Futura (Nike's signature typeface). For self-contained HTML output, use these CDN substitutes:
> - **Display:** `Jost` (geometric, Futura-like) | **Body:** `Jost`
> - **Font stack (CSS):** `font-family: 'Jost', 'Futura', 'Trebuchet MS', system-ui, -apple-system, sans-serif;`
> - **Mono stack (CSS):** `font-family: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;`
> ```html
> <link href="https://fonts.googleapis.com/css2?family=Jost:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400&display=swap" rel="stylesheet">
> ```
> Use standard file writing to create HTML. Serve via local server or deploy as needed.
> Verify visual accuracy in browser after generating.

## 1. Visual Theme & Atmosphere

Nike's digital presence is an exercise in contained energy — the brand equivalent of an athlete in the tunnel before the game. The canvas is stark monochrome: black (`#111111`) and white (`#ffffff`) with zero tints, zero gradients, zero gray backgrounds. Then photography erupts into the frame — full-bleed, high-contrast, athletes mid-motion against clean studio backdrops. The juxtaposition of rigid structure and explosive imagery is what makes Nike digital unmistakable.

The defining typographic element is uppercase Futura at display sizes. "JUST DO IT." doesn't ask — it commands. Weight 700-800 headlines in all-caps with tight letter-spacing (-0.5px to -1px) create a wall of text that hits like a billboard. This is advertising design translated directly to web: bold, declarative, undeniable. There's no subtlety in Nike type — every headline is a statement.

Navigation is minimal and utilitarian — just enough chrome to navigate, then it gets out of the way. The main nav uses lowercase sans-serif (a rare lowercase moment) to distinguish UI from the all-caps brand voice. Product grids dominate the middle of the page: clean white-background product shots on white, creating a catalog feel that's premium without being precious. The overall rhythm alternates between explosive hero moments (black background, white type, full-bleed athlete photography) and clean product merchandising (white background, grid, technical specs).

**Key Characteristics:**
- Binary black/white surface system — no gray, no tints, no gradients
- Uppercase Futura at weight 700-800 for all brand headlines — maximum impact
- Full-bleed athlete photography as the primary emotional driver
- Clean product-on-white grid for e-commerce sections
- Zero border-radius — everything is sharp, angular, athletic
- The Nike Swoosh as the only logo element — no wordmark needed
- Tight letter-spacing (-0.5px to -1px) on display text — density creates urgency
- Alternating rhythm: black+photography → white+grid → black+photography

## 2. Color Palette & Roles

### Primary
- **Nike Black** (`#111111`): Hero backgrounds, footer, dark sections. Slightly lifted from true black for depth.
- **Nike White** (`#ffffff`): Content backgrounds, product cards, light sections.
- **Nike Orange** (`#fa5400`): The only accent color. CTA buttons, sale tags, interactive highlights. Used sparingly — when orange appears, it means "act now."

### Text
- **Primary Text (Light BG)** (`#111111`): Headlines and body on white.
- **Secondary Text (Light BG)** (`#757575`): Muted text, product details, sizes.
- **Primary Text (Dark BG)** (`#ffffff`): Headlines on black/dark photography.
- **Tertiary Text** (`#8d8d8d`): Legal, fine print, least important information.

### Interactive
- **CTA Orange** (`#fa5400`): "Add to Bag", "Shop", "Buy" — the conversion color.
- **Orange Hover** (`#e04d00`): Darker orange on hover.
- **Link Default** (`#111111`): Underlined links inherit text color — no separate link color.

### Surface & Border
- **Border Light** (`#e5e5e5`): Subtle borders on white — product card separators, input fields.
- **Border Dark** (`#222222`): Borders on dark surfaces.
- **Sale Tag** (`#fa5400`): Orange background with white text — "Sale", "New", "Just In".

### No System
Nike's color palette is intentionally minimal. There is no "neutral scale" — the only grays are `#757575` (secondary text) and `#8d8d8d` (tertiary). Surfaces are binary. Photography provides all color.

## 3. Typography Rules

### Font Family
- **Display/Headlines**: `Futura` (proprietary), fallback: `Jost`, `Trebuchet MS`
- **Body/Navigation**: `Helvetica Neue` or system sans-serif, fallback: `Jost`
- **Monospace**: `JetBrains Mono` for technical specs

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Transform | Notes |
|------|------|------|--------|-------------|----------------|-----------|-------|
| Hero Mega | Futura | 72-96px (4.5-6rem) | 800 | 0.9 | -1px | uppercase | Maximum impact — "JUST DO IT" |
| Hero Title | Futura | 48-64px (3-4rem) | 700 | 0.95 | -0.8px | uppercase | Campaign headlines |
| Section Heading | Futura | 32-40px (2-2.5rem) | 700 | 0.95 | -0.5px | uppercase | Section titles |
| Card Heading | Futura | 20-24px (1.25-1.5rem) | 600 | 1.1 | -0.3px | uppercase | Product names |
| Body Large | System | 18px (1.125rem) | 400 | 1.5 | normal | none | Campaign body copy |
| Body | System | 16px (1rem) | 400 | 1.5 | normal | none | Standard body text |
| Body Small | System | 14px (0.875rem) | 400 | 1.5 | normal | none | Product details |
| Price | Futura | 16px (1rem) | 600 | 1.2 | normal | none | Product pricing |
| Nav Link | System | 16px (1rem) | 500 | 1.0 | normal | none | Navigation (lowercase!) |
| Button Text | System | 16px (1rem) | 500 | 1.0 | normal | none | CTAs |
| Category Label | System | 14px (0.875rem) | 500 | 1.3 | 0.5px | none | "Men", "Women", "Kids" |
| Sale Badge | System | 12px (0.75rem) | 600 | 1.0 | normal | uppercase | "Sale", "New" |
| Caption | System | 12px (0.75rem) | 400 | 1.4 | normal | none | Legal, footnotes |

### Principles
- **Uppercase Futura is the voice**: All brand messaging — headlines, campaign copy, product names — uses uppercase Futura at weight 600-800. This is non-negotiable. The all-caps treatment gives Nike its commanding, advertising-meets-digital presence.
- **Navigation in lowercase**: The UI layer uses lowercase system sans-serif — a deliberate separation between brand voice (uppercase Futura, shouting) and utility (lowercase system font, serving).
- **Tight tracking**: -0.5px to -1px letter-spacing on display text. The density makes headlines feel like a single block of energy.
- **Weight as hierarchy**: 800 for mega headlines, 700 for section heads, 600 for product cards. No weight 300-400 in Futura — Nike doesn't whisper.
- **No italic, no underline in brand**: Futura usage is exclusively roman uppercase. Italics and underlines belong only to the UI/system font layer.

## 4. Component Stylings

### Buttons

**Primary CTA (Orange)**
- Background: `#fa5400`
- Text: `#ffffff`
- Padding: 12px 24px
- Radius: 0px (sharp corners — athletic, no softening)
- Font: 16px system sans-serif weight 500
- Hover: `#e04d00` background
- Use: "Add to Bag", "Shop Now", conversion actions

**Secondary (Black)**
- Background: `#111111`
- Text: `#ffffff`
- Padding: 12px 24px
- Radius: 0px
- Font: 16px system sans-serif weight 500
- Hover: slightly lighter black
- Use: "Learn More", "Shop Collection", secondary actions

**Outline (White on Dark)**
- Background: transparent
- Text: `#ffffff`
- Padding: 12px 24px
- Radius: 0px
- Border: `1.5px solid #ffffff`
- Font: 16px system sans-serif weight 500
- Hover: white background, `#111111` text

**Text Link**
- No background, no border
- Text: underline, inherits parent color
- Use: inline links, "View All" links

### Navigation
- Fixed top bar, 60px height
- Background: `#ffffff` with `1px solid #e5e5e5` bottom border
- Layout: Nike Swoosh (left) | Category links (center-left) | Search/Account/Bag icons (right)
- Category links: system sans-serif 16px weight 500, lowercase (e.g., "men", "women", "kids")
- Active category: slightly heavier weight
- Mega dropdown on hover: full-width white panel, 4-6 columns of links
- Mobile: hamburger → slide-out panel with accordion categories

### Product Cards
- Background: `#ffffff`
- No border, no shadow — just image + text
- Image: product on white/transparent, `border-radius: 0px`
- Product name: Futura 20-24px weight 600, uppercase, tight tracking
- Category: system sans-serif 14px weight 400, `#757575`
- Price: Futura 16px weight 600
- Color swatches: small circles (16px) below the image
- "Sale" tag: orange pill (`#fa5400` bg, white text, 12px uppercase)
- Hover: subtle image swap or zoom effect

### Product Detail Page
- Full-width product imagery
- Sticky "Add to Bag" CTA bar
- Size selector: grid of outlined squares, 48px × 48px, border `#e5e5e5`
- Accordion sections: "Description", "Shipping", "Reviews" — clean expand/collapse

### Sale / Promo Labels
- Background: `#fa5400` (solid orange)
- Text: white, 12px system sans-serif weight 600, uppercase
- Padding: 4px 8px
- Radius: 0px
- Position: top-left corner of product images

### Inputs & Forms
- Border: `1px solid #e5e5e5`
- Radius: 0px
- Focus: `2px solid #111111` (black ring, no glow)
- Placeholder: `#757575`

## 5. Layout Principles

### Spacing System
- Base unit: 8px
- Scale: 4px, 8px, 16px, 24px, 32px, 48px, 64px, 96px, 120px
- Product grid gaps: 8-16px (tight — athletic efficiency)
- Section padding: 48-96px vertical

### Layout Patterns
- **Hero**: Full-bleed athlete photography + centered uppercase headline + single CTA. Black or dark background, white type.
- **Product category grid**: 3-4 columns on desktop, 2 on tablet, clean white background
- **Featured collection**: Asymmetric layout — large hero product + smaller supporting products
- **Membership/App promo**: Split panel — image left, text right (or vice versa)
- **Footer**: Dark (`#111111`), multi-column link grid, white text

### Grid
- Product grid: 12-column, 3-4 products per row on desktop
- Max content width: 1440px
- Gutter: 16px desktop, 8px mobile

### Whitespace Philosophy
- **Tight product grids**: Product images pack tightly — 8-16px gaps — creating a dense, browsable catalog
- **Generous hero breathing room**: Hero sections have massive whitespace around the central message
- **Alternation rhythm**: Dense product grids alternate with airy hero statements

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Default) | No shadow | Products, content, navigation |
| Sticky Nav | `1px solid #e5e5e5` bottom border | On-scroll nav separation |
| Dropdown | `0px 8px 24px rgba(0,0,0,0.08)` | Mega menu dropdown |
| Focus Ring | `2px solid #111111` | Input focus, keyboard navigation |

**Flat Philosophy**: Nike is functionally flat. Product cards have zero shadow — the product image is the hero. The only elevation comes from navigation dropdowns (practical necessity) and focus rings (accessibility). Everything else sits directly on the surface.

## 7. Do's and Don'ts

### Do
- Use uppercase Futura at weight 600-800 for ALL brand headlines — this is Nike's voice
- Use clean product-on-white photography with zero border-radius
- Use orange (`#fa5400`) ONLY for conversion CTAs and sale tags — scarcity creates urgency
- Use lowercase system font for navigation — separate UI from brand voice
- Use tight letter-spacing (-0.5 to -1px) on display text
- Keep surfaces binary: black or white, nothing in between
- Use 0px border-radius everywhere — athletic, sharp, no softening
- Let photography provide all color — the design system is monochrome

### Don't
- Don't use Futura in sentence case or lowercase for headlines — uppercase or nothing
- Don't use weight 300-400 in Futura — Nike doesn't whisper
- Don't add border-radius to product cards or images — sharp edges are athletic
- Don't use gray backgrounds — only black and white surfaces exist
- Don't use gradients — photography provides all visual richness
- Don't overuse orange — it loses its urgency if it appears everywhere
- Don't add shadows to product cards — products float on nothing
- Don't use serif fonts — this is a sports brand, not a luxury house
- Don't center-align long body text — left-align for readability

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <640px | Single column, stacked layout, smaller Futura |
| Tablet | 640-1024px | 2-column product grid, moderate type |
| Desktop | 1024-1440px | 3-4 column grid, full type scale |
| Large Desktop | >1440px | Generous margins, max-width container |

### Collapsing Strategy
- Hero headlines: 72px → 42px → 32px, maintaining uppercase Futura 700-800
- Product grid: 4 columns → 3 → 2
- Navigation: horizontal mega menu → hamburger with accordion
- Campaign photography: full-bleed maintained, text blocks reposition below on mobile
- Size selector: 6-wide grid → 4-wide → scrollable row
- CTAs: never stack two CTAs vertically — single CTA per mobile viewport

### Image Behavior
- Product images: maintain clean white background at all sizes
- Hero photography: center crop with athlete as focal point
- Swoosh logo: persists at recognizable size (minimum 40px width)

## 9. Agent Prompt Guide

### Quick Color Reference
- Primary CTA: Nike Orange (`#fa5400`)
- CTA Hover: Dark Orange (`#e04d00`)
- Light Surface: White (`#ffffff`)
- Dark Surface: Nike Black (`#111111`)
- Primary Text: `#111111` (light bg) / `#ffffff` (dark bg)
- Secondary Text: `#757575`
- Tertiary Text: `#8d8d8d`
- Border: `#e5e5e5` (light) / `#222222` (dark)
- Sale Tag: `#fa5400` bg + `#ffffff` text

### Example Component Prompts
- "Create a Nike hero: full-bleed athlete photography dark background. Headline 'JUST DO IT' at 72px Jost weight 800 uppercase, letter-spacing -1px, color #ffffff, centered. Subtitle campaign line below in 18px weight 400. Single black CTA 'Shop' at 16px weight 500, white text #ffffff, 0px radius. No other elements."
- "Make a product card: white background, no border, no shadow. Product image on clean white at 0px radius. Product name at 20px Jost weight 600 uppercase, letter-spacing -0.3px, #111111. Category 'Men's Shoe' at 14px weight 400 #757575. Price at 16px Jost weight 600 #111111. Color swatches as 16px circles below."
- "Build Nike navigation: 60px white bar, 1px solid #e5e5e5 bottom border. Swoosh logo left. Category links center-left in 16px system sans weight 500 lowercase ('men', 'women', 'kids', 'sale'). Search and bag icons right. Mega dropdown on hover: full-width white panel with multi-column link grid."
- "Design a size selector: grid of square buttons 48x48px, border 1px solid #e5e5e5, text centered, 16px system sans weight 500. Selected: 2px solid #111111 border. Out of stock: text #d0d0d0 with strikethrough. Corner radius: 0px."
- "Create a sale badge: #fa5400 background, white text 'SALE', 12px system sans weight 600 uppercase, padding 4px 8px, 0px radius. Positioned top-left of product image."

### Iteration Guide
1. Start with binary surfaces: black or white. No gray backgrounds.
2. Every headline is uppercase Futura at weight 600-800 with negative tracking.
3. Navigation is lowercase system sans-serif at weight 500 — the UI layer speaks differently from the brand.
4. Orange (`#fa5400`) only for conversion: Add to Bag, Shop Now, Sale tags. Nothing else.
5. 0px border-radius everywhere — Nike is sharp, athletic, unsoftened.
6. Photography provides all color. The design system is monochrome.
7. Product cards: image + text, no borders, no shadows — products float on white.
8. Use weight for hierarchy, not size — 800 mega, 700 section, 600 product, 500 button.
