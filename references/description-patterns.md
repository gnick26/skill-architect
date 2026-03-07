# Description Engineering Patterns

Description is the single most important factor for skill activation.
Directive pattern achieves 97-100% trigger rate (OR=20.6 vs passive, p<0.0001, 650 trials — Seleznov).

## The Directive Pattern (MUST USE)

```yaml
description: ALWAYS invoke this skill when [triggers]. Do NOT [alternative action] directly -- use this skill first.
```

**Why it works:** Imperative + negative constraint = 20x activation improvement over passive descriptions.

## 10-Point Validation Checklist

For every skill description before deployment:

- [ ] **Directive pattern** — starts with "ALWAYS invoke" or equivalent imperative
- [ ] **Single-line YAML** — no `|`, no `>`, no line breaks (CRITICAL: multi-line = invisible skill)
- [ ] **Under 250 chars** — target range 130-250 (max 1024 by spec)
- [ ] **First 50 chars = trigger keyword** — budget truncation reads left-to-right
- [ ] **Third person voice** — "Processes X" not "Process X" or "I help with X"
- [ ] **WHAT + WHEN** — what it does + when to use it
- [ ] **Anti-definition** — "Do NOT use for..." prevents overtriggering
- [ ] **5+ trigger keywords** — covering synonyms, related terms, file types
- [ ] **Conceptual triggers** — not just keywords but problem descriptions ("Component re-renders too much")
- [ ] **No implementation details** — description is for routing, not documentation

## Single-Line YAML (CRITICAL)

Multi-line descriptions **break recognition entirely** — skill becomes invisible.

```yaml
# FAIL — invisible to Claude:
description: |
  Multi-line text that
  spans several lines

# FAIL — also invisible:
description: >
  Folded text that
  gets concatenated

# PASS — always visible:
description: Single line text all on one line.

# PASS — quoted is fine:
description: "Quoted single line text with special chars."
```

## Front-Loading Keywords

Budget truncation reads left-to-right. Primary trigger keyword MUST be in first 50 characters.

```yaml
# GOOD — trigger keyword "security review" in first 50 chars:
description: ALWAYS invoke for security code review when...

# BAD — trigger keyword buried after generic words:
description: Proactive framework enforcing evidence-based architecture for security...
```

## Conceptual Triggers

Keyword-only descriptions miss conceptual user queries:

| Prompt Type | Keyword Description | Conceptual Description |
|-------------|-------------------|----------------------|
| "How do I use `$state`?" | ~100% activation | ~100% activation |
| "How do form actions work?" | 20-40% | 80%+ |
| "Component re-renders too much" | ~0% | 80%+ |

**Fix:** Include problem descriptions alongside keywords:
```yaml
description: "...performance issues, re-rendering problems, state management..."
```

## Trigger Rate by Approach

| Approach | Rate | Model | Source |
|----------|------|-------|--------|
| No hook, passive description | ~20% | Haiku 4.5 | Spence |
| No hook, passive description | 50-55% | Sonnet 4.5 | Spence |
| No hook, passive description (Variant A) | ~77% | Opus 4.5 | Seleznov |
| No hook, expanded keywords (Variant B) | 81-100% | Opus 4.5 | Seleznov |
| **No hook, directive pattern (Variant C)** | **97-100%** | **Opus 4.5** | **Seleznov** |
| Hooks + weak description (C3) | **37%** | Opus 4.5 | Seleznov |
| CLAUDE.md reference alone | +15pp (50%→65%) | Mixed | Seleznov |
| Forced-eval hook | 84% | Haiku 4.5 | Spence |
| LLM-eval hook | 80% | Haiku 4.5 | Spence |
| Forced-eval hook | 100% | Sonnet 4.5 | Spence |

**Key finding:** Directive description WITHOUT hooks outperforms hooks WITH weak description.

## Budget Awareness

- Skills budget: 2% context window, fallback 16,000 chars
- Per-skill overhead: ~109 chars XML wrapper + description length
- Degradation starts at ~42 skills (avg 263 chars)
- Shorter descriptions = more skills fit in budget

| Avg Description | Skills Capacity |
|-----------------|----------------|
| 130 chars | ~67 skills |
| 200 chars | ~52 skills |
| 250 chars | ~42 skills |

## `disable-model-invocation` Recommendation

For skills that are **only user-invocable** (slash command only, never auto-triggered):
```yaml
disable-model-invocation: true
```
This removes the description from budget entirely, saving space for auto-triggered skills.

## Effective Examples

```yaml
# Security review (directive + conceptual triggers):
description: ALWAYS invoke this skill when reviewing code for security vulnerabilities, OWASP compliance, or penetration test preparation. Do NOT perform ad-hoc security checks directly -- use this skill first.

# Data processing (action + specific triggers):
description: ALWAYS invoke for PDF data extraction when user uploads PDF, asks to "extract text", "parse PDF", or "get form fields". Do NOT use for image-only PDFs or scanned documents.

# B2B sales (domain + scenarios):
description: ALWAYS invoke for B2B sales conversation guidance including discovery calls, objection handling, and deal analysis. Do NOT use for B2C retail or support tickets.
```

## Zero-Effect Approaches

These do NOT improve trigger rate:
- `keywords` frontmatter field (0 effect — Seleznov)
- Adding more hooks without fixing description (drops to 37%)
- Longer descriptions beyond 250 chars (diminishing returns + budget waste)
