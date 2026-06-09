---
name: product-description
description: "Create concise product description copy for e-commerce listings, campaign pages, and quick reference. Multiple length variations."
cluster: brandmint-content
wave: 6
dependencies:
  - value-proposition
  - product-positioning
  - messaging-framework
triggers:
  - "product description"
  - "listing copy"
  - "product copy"
  - "Amazon copy"
---

# Product Description Skill

Create product descriptions in multiple lengths for various platforms.

## Prerequisites

Load upstream outputs:
- `value-proposition.json` — for key benefits
- `product-positioning.json` — for features and differentiation
- `messaging-framework.json` — for headlines

## Process

### Step 1: Core Product Information

Extract and organize:

**Essential info:**
- Product name
- Category
- Price
- Key specs/dimensions

**Benefits hierarchy:**
1. Primary benefit (headline-worthy)
2. Secondary benefits (2-3)
3. Features that enable benefits
4. Specs that prove features

### Step 2: Description Lengths

Create variations for different contexts:

| Length | Words | Use Case |
|--------|-------|----------|
| **Micro** | 15-25 | Social bio, quick reference |
| **Short** | 50-75 | Email, ad copy |
| **Medium** | 100-150 | Product cards, listings |
| **Full** | 200-300 | Campaign page, Amazon |
| **Extended** | 400+ | Detailed product page |

### Step 3: Write Each Version

**Micro (15-25 words):**
```
[Product name] is a [category] that [primary benefit]. [Key differentiator].
```

**Short (50-75 words):**
```
[Product name] + [what it is]
[Primary benefit statement]
[2 key features with benefits]
[Call to action or differentiator]
```

**Medium (100-150 words):**
```
[Hook: problem or aspiration]
[Product introduction]
[Primary benefit expanded]
[3-4 features with benefits]
[Differentiator]
[Specs summary]
```

**Full (200-300 words):**
```
[Compelling opening hook]
[Problem agitation]
[Product as solution]
[Full benefit narrative]
[All key features detailed]
[Competitive differentiation]
[Social proof if available]
[Specifications]
[Call to action]
```

### Step 4: Feature-Benefit Mapping

For each feature, ensure benefit is clear:

| Feature | Benefit | Copy Example |
|---------|---------|--------------|
| [feature] | [what it does for user] | "[Feature] so you can [benefit]" |

### Step 5: SEO Considerations

For e-commerce listings:
- Include primary keywords naturally
- Use bullet points for scannability
- Front-load important information
- Include specs searchers look for

## Output Schema

```json
{
    "skill": "product-description",
    "cluster": "content",
    "wave": 6,
    "timestamp": "2024-01-15T10:30:00Z",
    "status": "complete",
    "version": "1.0.0",
    "data": {
        "core_info": {
            "product_name": "string",
            "category": "string",
            "price": "string",
            "key_specs": ["string"]
        },
        "benefits_hierarchy": {
            "primary": "string",
            "secondary": ["string"],
            "features": ["string"]
        },
        "descriptions": {
            "micro": {
                "word_count": "number",
                "copy": "string"
            },
            "short": {
                "word_count": "number",
                "copy": "string"
            },
            "medium": {
                "word_count": "number",
                "copy": "string"
            },
            "full": {
                "word_count": "number",
                "copy": "string"
            },
            "extended": {
                "word_count": "number",
                "copy": "string"
            }
        },
        "feature_benefit_map": [
            {
                "feature": "string",
                "benefit": "string",
                "copy_snippet": "string"
            }
        ],
        "bullet_points": ["string (5-7 key points)"],
        "seo_keywords": ["string"]
    }
}
```

## Quality Checklist

- [ ] All 5 length variations created
- [ ] Primary benefit is clear in all versions
- [ ] Features are tied to benefits
- [ ] Micro version works as standalone
- [ ] Full version is comprehensive
- [ ] Bullet points are scannable
- [ ] SEO keywords included naturally
