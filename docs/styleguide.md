# Styleguide

**Note:** This documentation was generated with the help of AI. Since it is documentation and not code, I hope this is okay.

## Theme: Forest Floor Light

A nature-inspired, minimal design with soft greens and neutral tones. Mobile-first approach with breakpoints scaling up.

## Color Palette

### Backgrounds

| Variable            | Value                  | Usage               |
|------------------|------------------------|----------------------|
| `--bg-primary`   | `#F0F3ED`              | Page background      |
| `--bg-surface`   | `#FFFFFF`              | Cards, navbar        |
| `--bg-elevated`  | `rgba(0, 0, 0, 0.03)`  | Subtle raised areas  |

### Accent

| Variable            | Value                       | Usage                  |
|------------------|-----------------------------|------------------------|
| `--accent`       | `#5E9342`                   | Primary accent (green) |
| `--accent-hover` | `#74AA58`                   | Hover state            |
| `--accent-glow`  | `rgba(94, 147, 66, 0.12)`   | Glow / box-shadow      |

### Text

| Variable              | Value     | Usage                  |
|--------------------|-----------|------------------------|
| `--text-primary`   | `#1C1F1A` | Headings, body text    |
| `--text-secondary` | `#6B7062` | Descriptions, labels   |
| `--text-muted`     | `#A0A498` | Tags, meta info        |
| `--text-bright`    | `#EDF0E9` | Light text on dark bg  |

### Borders & Shadows

| Variable             | Value                          |
|-------------------|--------------------------------|
| `--border-subtle` | `rgba(0, 0, 0, 0.08)`          |
| `--shadow-sm`     | `0 2px 8px rgba(0, 0, 0, 0.06)` |
| `--shadow-md`     | `0 8px 32px rgba(0, 0, 0, 0.08)` |

## Typography

**Font:** Sansation (Google Fonts)

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sansation:ital,wght@0,300;0,400;0,700;1,300;1,400;1,700&display=swap" rel="stylesheet">
```

### Weights

| Weight | Value | Usage                                 |
|--------|-------|---------------------------------------|
| Light  | 300   | Body text (default), subheadings      |
| Regular| 400   | Nav links, form labels, accent labels |
| Bold   | 700   | Headings, active nav items            |

### Font Sizes (Mobile -> Tablet -> Desktop)

| Element         | Mobile | Tablet (768px+) | Desktop (992px+) |
|-----------------|--------|-----------------|-------------------|
| Hero header     | 48px   | 72px            | 88px              |
| h1              | 36px   | 48px            | 56px              |
| h3              | 15px   | 18px            | 20px              |
| Nav links       | 14px   | 15px            | 15px              |
| Project title   | 18px   | 18px            | 18px              |
| Body / cards    | 14px   | 14px            | 14px              |
| Tags            | 12px   | 12px            | 12px              |

### Special Treatments

- **Hero header:** gradient text (`--text-primary` to `--accent` at 135deg)
- **Quote (h3#quote):** italic, left-aligned with a 2px accent border-left
- **Accent labels:** uppercase, letter-spacing 0.05em

## Spacing Scale

| Variable         | Value |
|---------------|-------|
| `--space-xs`  | 4px   |
| `--space-sm`  | 8px   |
| `--space-md`  | 16px  |
| `--space-lg`  | 24px  |
| `--space-xl`  | 40px  |
| `--space-2xl` | 64px  |

## Border Radii

| Variable          | Value | Usage                     |
|----------------|-------|---------------------------|
| `--radius-md`  | 12px  | Cards, nav items, form     |
| `--radius-nb`  | 16px  | Navbar                     |
| `--radius-lg`  | 20px  | Main content container     |

## Layout

- **Mobile-first** design, breakpoints scale up
- Centered single-column layout (`.center` with flexbox)
- Main content capped at `max-width: 900px`

### Breakpoints

| Name    | Min-width | Key changes                                       |
|---------|-----------|---------------------------------------------------|
| Tablet  | 768px     | Larger type, 2-column project grid, wider padding  |
| Desktop | 992px     | Largest type sizes, more generous padding           |

### Project Grid

- **Mobile:** single column, vertical stack
- **Tablet+:** 2-column CSS grid (`grid-template-columns: repeat(2, 1fr)`)

## Motion

| Variable               | Value                          |
|----------------------|--------------------------------|
| `--ease-out`         | `cubic-bezier(0.16, 1, 0.3, 1)` |
| `--ease-in-out`      | `cubic-bezier(0.4, 0, 0.2, 1)`  |
| `--duration-fast`    | 0.15s                          |
| `--duration-normal`  | 0.3s                           |
| `--duration-slow`    | 0.5s                           |

### Animations

- **fadeUp:** entry animation on main content and project cards (opacity 0 -> 1, translateY 16px -> 0)
- Project cards stagger with 0.1s incremental delay (up to 6 items)
- `prefers-reduced-motion` is respected — all animations and transitions reduce to near-instant

### Interactive States

- **Nav items:** background transitions on hover
- **Project cards:** border turns accent, accent glow shadow, subtle lift (`translateY(-2px)`) on hover
- **Links:** arrow pseudo-element slides right on hover

## Components

### Navbar

Horizontal pill-bar with surface background, subtle border, and small shadow. Active item gets accent background with white bold text.

### Main Content Card

Full-width (up to 900px) white surface card with rounded corners, medium shadow, and fadeUp entry animation.

### Project Cards

Elevated background cards in a responsive grid. Each card contains a title (accent color), description, tags (uppercase muted), and a link with an animated arrow.

### Contact Form

Stacked form fields inside accent-colored containers with rounded corners and medium shadow. Labels centered, inputs full-width with primary background.
