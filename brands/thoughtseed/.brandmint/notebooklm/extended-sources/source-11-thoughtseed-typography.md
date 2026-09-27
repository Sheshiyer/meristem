# Source 11: Thoughtseed Typography

*Typefaces (Tyros Pro, SubjectivitySerif, Fira Code), type scale, hierarchy, implementation.*

_Source: meristem pipeline output at `wave-3-identity/typography.json`_

---

## Rationale

- **Brand Personality:** Founder-led systems translator: clear, calm, technically precise, human, editorially restrained. Cross-disciplinary, founder-led, precise, editorial, grounded.

- **Type Direction:** Bold geometric display type paired with refined editorial serif body and monospace technical. The display carries authority and confidence; the serif carries humanity and craft; the monospace carries operational precision and proof.

- **Pairing Logic:** Tyros Pro (display) for headlines, hero text, and campaign identifiers — establishes presence. SubjectivitySerif (body) for product descriptions, narrative text, and editorial copy — establishes craft. Fira Code (data) for specs, metadata, and system artifacts — establishes precision. The three create a typographic rhythm: bold claim → refined explanation → technical proof.

## Typefaces

### Primary

- **Name:** Tyros Pro

- **Foundry:** Paratype

- **Style:** geometric sans-serif (humanist warmth)

#### Weights

- 400

- 500

- 600

- 700

- 800

- 900

- **Use For:** Display, headlines, hero text, campaign identifiers, CTA buttons

- **Source:** Paratype Foundry

- **Fallback Stack:** Tyros Pro, 'Helvetica Neue', Helvetica, Arial, sans-serif

### Secondary

- **Name:** SubjectivitySerif

- **Foundry:** Production Type

- **Style:** transitional serif (editorial humanity)

#### Weights

- 300

- 400

- 500

- 600

- 700

- **Use For:** Body copy, product descriptors, narrative text, editorial body, email sequences

- **Source:** Production Type

- **Fallback Stack:** SubjectivitySerif, Georgia, 'Times New Roman', serif

### Monospace

- **Name:** Fira Code

- **Foundry:** Mozilla

- **Style:** humanist monospace

#### Weights

- 300

- 400

- 500

- 600

- 700

- **Use For:** Specs, metadata, system artifacts, technical labels, data/ops surfaces

- **Source:** Mozilla (open source)

- **Fallback Stack:** 'Fira Code', 'SF Mono', Menlo, Monaco, Consolas, monospace

## Type Scale

- **Ratio:** 1.25

- **Base Size:** 16

### Sizes

#### Xs

- **Size:** 12px

- **Line Height:** 1.5

#### Sm

- **Size:** 14px

- **Line Height:** 1.5

#### Base

- **Size:** 16px

- **Line Height:** 1.6

#### Lg

- **Size:** 18px

- **Line Height:** 1.6

#### Xl

- **Size:** 20px

- **Line Height:** 1.5

#### 2Xl

- **Size:** 24px

- **Line Height:** 1.4

#### 3Xl

- **Size:** 32px

- **Line Height:** 1.3

#### 4Xl

- **Size:** 40px

- **Line Height:** 1.2

#### 5Xl

- **Size:** 56px

- **Line Height:** 1.1

#### 6Xl

- **Size:** 72px

- **Line Height:** 1.05

#### 7Xl

- **Size:** 96px

- **Line Height:** 1.0

## Hierarchy

### Display

- **Font:** Tyros Pro

- **Size:** 72-96px

- **Weight:** Bold

- **Letter Spacing:** tight

- **Line Height:** 1.0

- **Color:** #1A237E

### H1

- **Font:** Tyros Pro

- **Size:** 56px

- **Weight:** Bold

- **Letter Spacing:** tight

- **Line Height:** 1.1

- **Color:** #1A237E

### H2

- **Font:** Tyros Pro

- **Size:** 40px

- **Weight:** SemiBold

- **Letter Spacing:** normal

- **Line Height:** 1.2

- **Color:** #1A237E

### H3

- **Font:** Tyros Pro

- **Size:** 32px

- **Weight:** SemiBold

- **Letter Spacing:** normal

- **Line Height:** 1.3

- **Color:** #37474F

### H4

- **Font:** Tyros Pro

- **Size:** 24px

- **Weight:** SemiBold

- **Letter Spacing:** normal

- **Line Height:** 1.4

- **Color:** #37474F

### H5

- **Font:** Tyros Pro

- **Size:** 20px

- **Weight:** Medium

- **Letter Spacing:** normal

- **Line Height:** 1.5

- **Color:** #37474F

### H6

- **Font:** SubjectivitySerif

- **Size:** 18px

- **Weight:** SemiBold

- **Letter Spacing:** normal

- **Line Height:** 1.5

- **Color:** #37474F

### Body

- **Font:** SubjectivitySerif

- **Size:** 16-18px

- **Weight:** Regular

- **Letter Spacing:** normal

- **Line Height:** 1.6

- **Color:** #37474F

### Body Small

- **Font:** SubjectivitySerif

- **Size:** 14px

- **Weight:** Regular

- **Letter Spacing:** normal

- **Line Height:** 1.6

- **Color:** #37474F

### Caption

- **Font:** Tyros Pro

- **Size:** 12-14px

- **Weight:** Regular

- **Letter Spacing:** wide

- **Line Height:** 1.4

- **Color:** #37474F

### Label

- **Font:** Fira Code

- **Size:** 11-13px

- **Weight:** Regular

- **Letter Spacing:** normal

- **Line Height:** 1.4

- **Color:** #37474F

## Implementation

- **Css Variables:** :root {
  --font-primary: 'Tyros Pro', 'Helvetica Neue', Helvetica, Arial, sans-serif;
  --font-secondary: 'SubjectivitySerif', Georgia, 'Times New Roman', serif;
  --font-mono: 'Fira Code', 'SF Mono', Menlo, Monaco, Consolas, monospace;
  --color-primary: #1A237E;
  --color-accent: #00897B;
  --color-cta: #F57C00;
  --color-text: #37474F;
  --color-bg: #FFFFFF;
  --color-growth: #B8E986;
}

- **Loading Strategy:** Use font-display: swap for all web fonts. Preload Tyros Pro 700 for hero text. SubjectivitySerif 400/600 for body. Fira Code 400 for code blocks and metadata.

- **Font Display:** swap

## Prompt Workflow Integration

- **Triptych Hero:** Bold geometric display (Tyros Pro character) for central THOUGHTSEED repetition in triptych hero banner

- **Campaign Attribution:** Clean sans-serif, all-caps, tracked (Tyros Pro character) for MIRA / DIGITAL WILDERNESS attribution blocks

- **Product Labels:** SubjectivitySerif character for product descriptors on concrete-botanical and product photography

- **System Artifacts:** Fira Code monospace for technical specs in product knolling compositions

- **Logo Object Labels:** Manrope Regular style for small monochrome labels on tier 1 logo objects (per Amir prompt conventions)

