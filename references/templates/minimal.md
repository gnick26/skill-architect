# Minimal Skill Template

Use for simple, focused procedures under 100 lines.

```yaml
---
name: {skill-name}
description: ALWAYS invoke this skill when {trigger1}, {trigger2}. Do NOT {alternative} directly -- use this skill first.
---

# {Skill Name}

## When to Use
- {Trigger condition 1}
- {Trigger condition 2}

## When NOT to Use
- {Boundary 1}
- {Boundary 2}

## Instructions

{Step-by-step procedure, imperative voice}

1. {Action 1}
2. {Action 2}
3. {Action 3}

## Validation

Before completing:
- [ ] {Success criterion 1}
- [ ] {Success criterion 2}
```

## When to Use This Template

- Single-purpose utility
- <5 decision branches
- No external references needed
- Fits in 50-100 lines
