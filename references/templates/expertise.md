# Domain Expertise Template

Use for packaging non-code knowledge: marketing, pedagogy, operations, consulting.

```yaml
---
name: {domain}-{capability}
description: ALWAYS invoke for {domain activity} guidance when {trigger1}, {trigger2}, or {trigger3}. Do NOT handle {boundary1} or {boundary2} directly -- use this skill first.
allowed-tools: Read, Write
---

# {Domain} {Capability} Framework

## When to Use
- {User scenario 1}
- {User scenario 2}
- {User scenario 3}

## When NOT to Use
- {Out of scope 1}
- {Out of scope 2}

## Core Principles

1. **{Principle 1}:** {Brief explanation}
2. **{Principle 2}:** {Brief explanation}
3. **{Principle 3}:** {Brief explanation}

## Decision Framework

### Step 1: Assessment
Gather information:
- {Question 1}
- {Question 2}
- {Question 3}

### Step 2: Classification
Based on assessment:

IF {condition A} → Category: {X}
   Action: {recommended approach}
ELSE IF {condition B} → Category: {Y}
   Action: {different approach}
ELSE → Category: {Z}
   Action: {default approach}

### Step 3: Execution
Apply framework:
1. {Action based on category}
2. {Action}
3. {Action}

## Quality Rubric

| Criterion | Poor (1) | Adequate (2) | Good (3) | Excellent (4) |
|-----------|----------|--------------|----------|---------------|
| {Criterion 1} | {Description} | {Description} | {Description} | {Description} |
| {Criterion 2} | {Description} | {Description} | {Description} | {Description} |

Target: Average score ≥3.0

## Anti-Patterns

❌ **{Mistake 1}:** {Why it fails}
   ✅ Instead: {Correct approach}

❌ **{Mistake 2}:** {Why it fails}
   ✅ Instead: {Correct approach}

## Examples

### Good Example
**Scenario:** {Description}
**Approach:** {What was done}
**Result:** {Outcome}

### Bad Example
**Scenario:** {Description}
**Mistake:** {What went wrong}
**Lesson:** {What to learn}

## Validation

- [ ] {Verification item 1}
- [ ] {Verification item 2}
- [ ] {Verification item 3}

## References

- [references/detailed-rubrics.md](references/detailed-rubrics.md): Extended quality criteria
- [examples/](examples/): Template outputs
```

## When to Use This Template

- Marketing playbooks, pedagogical methodologies
- Sales frameworks, operational procedures
- Any domain requiring structured decision-making

## Key Additions for Non-Code Skills

1. **Decision trees** — Explicit IF/ELSE logic
2. **Quality rubrics** — Measurable success criteria
3. **Anti-patterns** — Common mistakes with corrections
4. **Examples** — Both good and bad for pattern matching
5. **Checklists** — Self-verification points
