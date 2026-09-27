---
name: competitor-analysis
description: "Analyze 2-5 competitors to identify positioning gaps, strengths, weaknesses, and whitespace opportunities. Informs differentiation strategy."
cluster: brandmint-foundation
wave: 1
dependencies:
  - brand-foundation
triggers:
  - "competitor analysis"
  - "competitive landscape"
  - "market analysis"
  - "who are we competing with"
---

# Competitor Analysis Skill

Analyze the competitive landscape to identify positioning opportunities and differentiation strategies.

## Prerequisites

Load upstream outputs:
- `brand-foundation.json` — for product category and positioning context
- `brand-config.yaml` — for product details and price point

## Process

### Step 1: Identify Competitors (2-5)

**Direct competitors:** Same product category, same target audience
**Indirect competitors:** Different product, same problem solved
**Aspirational competitors:** Brands we admire (for positioning reference)

For each competitor, gather:
- Name
- Price point
- Primary value proposition
- Target audience
- Key features

### Step 1b: Regional Required Set (additive)

When `brand-config.yaml` sets `market.region: FR` **or** the product domain is French energy-subsidy / CEE / PNCEE operations, the competitor set **MUST** include these named players (direct or indirect as evidence warrants). Do not substitute generics for them:

| Required name | Typical role in FR energy-subsidy market |
|---------------|------------------------------------------|
| Hellio | Major délégataire / CEE programme actor |
| Économie d'Énergie SAS | CEE / energy-efficiency services competitor |
| Effy | Residential/commercial retrofit & primes player |
| GEO PLC | Energy-services / obligation-market peer |

Rules:
- Still analyze 2–5 competitors total when the brand is not FR energy-subsidy; this required set applies only under the FR / energy-subsidy gate above.
- Other brands (non-FR, non-energy-subsidy) skip this step unchanged.
- Record each required name under `data.competitors[]` with evidence-backed strengths/weaknesses; if a player is adjacent rather than same-category, mark `type: "indirect"` and say why.
- Optionally emit `data.regional_required_competitors: ["Hellio", "Économie d'Énergie SAS", "Effy", "GEO PLC"]` when the gate fires so downstream synthesis can audit coverage.

### Step 2: Feature Comparison Matrix

Create a comparison table:

| Feature | Our Product | Competitor A | Competitor B | Competitor C |
|---------|-------------|--------------|--------------|--------------|
| Price | $X | $Y | $Z | $W |
| Feature 1 | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ |
| Feature 2 | ✓/✗ | ✓/✗ | ✓/✗ | ✓/✗ |
| ... | ... | ... | ... | ... |

### Step 3: Per-Competitor Deep Dive

For each competitor, analyze:

**Positioning:**
- How do they describe themselves?
- What's their headline/tagline?
- What category do they claim?

**Strengths:**
- What do they do well?
- What do customers praise in reviews?
- What features are unique to them?

**Weaknesses:**
- What do customers complain about?
- What's missing from their offering?
- Where do they fall short?

**Pricing strategy:**
- Premium, mid-market, or budget?
- What justifies their price point?

**Customer sentiment:**
- Review summary (if available)
- Common praise points
- Common complaints

### Step 4: Identify Positioning Gaps

**Whitespace analysis:**
- What needs are unmet by current competitors?
- What features does no one offer?
- What audience segments are underserved?

**Differentiation opportunities:**
- Where can we be genuinely different (not just "better")?
- What can we own that competitors can't claim?
- What's our unfair advantage?

### Step 5: Competitive Positioning Statement

Based on analysis, draft positioning against competitors:

```
Unlike [competitor/category], [our brand] [key differentiator] 
because [reason to believe].
```

## Output Schema

```json
{
    "skill": "competitor-analysis",
    "cluster": "foundation",
    "wave": 1,
    "timestamp": "2024-01-15T10:30:00Z",
    "status": "complete",
    "version": "1.0.0",
    "data": {
        "competitors": [
            {
                "name": "string",
                "type": "direct|indirect|aspirational",
                "price": "string",
                "value_proposition": "string",
                "target_audience": "string",
                "key_features": ["string"],
                "positioning": {
                    "headline": "string",
                    "category_claimed": "string"
                },
                "strengths": ["string"],
                "weaknesses": ["string"],
                "customer_sentiment": {
                    "praise_points": ["string"],
                    "complaints": ["string"]
                }
            }
        ],
        "feature_matrix": {
            "features": ["string"],
            "comparison": {
                "our_product": ["boolean"],
                "competitors": {
                    "[name]": ["boolean"]
                }
            }
        },
        "whitespace": {
            "unmet_needs": ["string"],
            "missing_features": ["string"],
            "underserved_segments": ["string"]
        },
        "differentiation": {
            "genuine_differences": ["string"],
            "ownable_territory": "string",
            "unfair_advantage": "string"
        },
        "positioning_statement": "string",
        "regional_required_competitors": ["string (optional; required names when market.region=FR / energy subsidy)"]
    }
}
```

## Quality Checklist

- [ ] Minimum 2 competitors analyzed
- [ ] Each competitor has strengths AND weaknesses
- [ ] Feature matrix includes at least 5 comparison points
- [ ] Whitespace opportunities identified
- [ ] Positioning statement is specific and defensible
- [ ] Analysis is based on evidence, not assumptions
- [ ] If `market.region=FR` or energy-subsidy domain: Hellio, Économie d'Énergie SAS, Effy, and GEO PLC are all present in `competitors[]`
