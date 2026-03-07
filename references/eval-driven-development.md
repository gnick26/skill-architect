# Eval-Driven Development

Anthropic's recommended methodology for building effective skills.

**Official term:** "eval-driven development" (lowercase, no abbreviation)
**Source:** Anthropic Skill Authoring Best Practices, Anthropic Demystifying Evals blog

## 5-Step Cycle (Anthropic)

1. **Identify gaps** — Run Claude on representative tasks WITHOUT a skill. Document specific failures.
2. **Create evaluations** — Build three scenarios that test these gaps.
3. **Establish baseline** — Measure Claude's performance without the skill.
4. **Write minimal instructions** — Create just enough content to address gaps and pass evaluations.
5. **Iterate** — Execute evaluations, compare against baseline, refine.

## Baseline Template

Use this template to capture baseline before writing skill:

```markdown
## Eval-Driven Development: {Skill Name}

### Task Description
{What the skill should accomplish}

### Gap Analysis (Step 1)
Without any skill, Claude:
- [ ] Fails at: {specific failure 1}
- [ ] Fails at: {specific failure 2}
- [ ] Fails at: {specific failure 3}

### Test Scenarios (Step 2)

#### Scenario 1: {name}
- **Input:** "{exact user prompt}"
- **Expected output:** {what correct result looks like}
- **Without skill:** {what Claude actually produces}
- **Gap:** {specific deficiency}

#### Scenario 2: {name}
- **Input:** "{exact user prompt}"
- **Expected output:** {what correct result looks like}
- **Without skill:** {what Claude actually produces}
- **Gap:** {specific deficiency}

#### Scenario 3: {name}
- **Input:** "{exact user prompt}"
- **Expected output:** {what correct result looks like}
- **Without skill:** {what Claude actually produces}
- **Gap:** {specific deficiency}

### Baseline Metrics (Step 3)
| Metric | Without Skill | Target |
|--------|--------------|--------|
| Task completion | ___% | ≥90% |
| Output format correct | ___% | 100% |
| Trigger rate | N/A | ≥90% |

### After Skill (Step 5 — fill after building)
| Metric | Without Skill | With Skill | Delta |
|--------|--------------|------------|-------|
| Task completion | ___% | ___% | +___% |
| Output format correct | ___% | ___% | +___% |
| Trigger rate | N/A | ___% | — |
```

## Scaling by Complexity

| Skill Complexity | Scenarios | Baseline Method |
|-----------------|-----------|-----------------|
| Simple (1 workflow) | 3 minimum | Manual: run task once without skill |
| Standard (2-3 workflows) | 5-7 | Manual: one scenario per workflow |
| Complex (5+ workflows) | 10+ | Consider cc-plugin-eval automation |

## Key Principles

- **Minimal instructions first** — add content only to fix observed failures, not hypothetical ones
- **3 scenarios minimum** — but don't over-engineer for simple skills
- **Measure, don't assume** — "it should work" is not a baseline
- **Iterate after deploy** — real usage reveals gaps no test catches

## What This Is NOT

- NOT a formal test suite requirement (3 scenarios suffice for most skills)
- NOT blocking: if gaps are obvious, write the skill and validate after
- NOT the same as cc-plugin-eval (which measures triggering, not task quality)
