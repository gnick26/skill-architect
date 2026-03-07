# Eval-Driven Development

Anthropic's recommended methodology for building effective skills.

**Official term:** "eval-driven development" (lowercase, no abbreviation)
**Source:** Anthropic Skill Authoring Best Practices, Anthropic Demystifying Evals blog

## RED Phase (Prerequisite — before writing any skill content)

Run the target task WITHOUT a skill. Two types depending on feasibility:

**Type 1 (executable):** Task can be run right now without external dependencies.
Execute: take one real query from Gate 1 examples → run in Claude → capture exact output.

**Type 2 (hypothetical):** Task requires domain tooling, MCP, or specialist context unavailable now.
Document: "Without skill, Claude would [X]. Specific gaps: [list them explicitly]."

BLOCK: neither Type 1 nor Type 2 completed → cannot proceed.
"Run the task first or document the hypothetical gap. No baseline = no skill."

Stop condition: IF Type 1 shows Claude completes task at ≥90% with correct format →
STOP Mode A. "Skill not needed — Claude handles this already. Document why and close."

**Simple skill exception:** If ALL three conditions hold simultaneously, Type 2 is sufficient without running Type 1:
- ≤1 workflow, ≤3 decision branches (Gate 3 metrics confirm)
- Gap is domain knowledge unavailable to base Claude (company rules, locale-specific legal, internal taxonomy)
- Gap is already demonstrated clearly in Gate 1 examples

This is not a skip — it is a documented Type 2 baseline.
NOT a domain gap: behavioral instructions ("always ask for examples"), output formatting ("use a table").

## 5-Step Cycle (Anthropic)

1. **Identify gaps** — Compare RED output vs Gate 1 expected output. Document specific failures only.
2. **Create evaluations** — Build three scenarios that test these gaps.
3. **Establish baseline** — Record RED phase metrics (completion %, format correct %, domain gaps).
4. **Write minimal instructions** — Create just enough content to address gaps and pass evaluations.
5. **Iterate** — Execute evaluations, compare against baseline, refine.

## Baseline Template

Use this template to capture baseline before writing skill:

```markdown
## Eval-Driven Development: {Skill Name}

### Task Description
{What the skill should accomplish}

### RED Phase
Type: [ ] Type 1 (executed) / [ ] Type 2 (hypothetical)
RED output summary: {what Claude produced or would produce without skill}

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
| Metric | RED (without skill) | Target | With skill |
|--------|---------------------|--------|------------|
| Task completion | ___% | ≥90% | ___% |
| Output format correct | ___% | 100% | ___% |
| Domain gaps | [list] | 0 critical | [list] |
| Trigger rate | N/A | ≥90% | ___% |
```

## Scaling by Complexity

| Skill Complexity | Scenarios | RED Method |
|-----------------|-----------|------------|
| Simple (1 workflow) | 3 minimum | Type 1: run once without skill |
| Standard (2-3 workflows) | 5-7 | Type 1: one run per workflow |
| Complex (5+ workflows) | 10+ | Type 1 + cc-plugin-eval automation |
| Domain/MCP-dependent | 3 minimum | Type 2: documented hypothetical |

## Key Principles

- **RED first, always** — no content before baseline exists
- **Minimal instructions** — add content only to fix observed failures, not hypothetical ones
- **3 scenarios minimum** — but don't over-engineer for simple skills
- **Measure, don't assume** — "it should work" is not a baseline
- **Iterate after deploy** — real usage reveals gaps no test catches

## What This Is NOT

- NOT a formal test suite requirement (3 scenarios suffice for most skills)
- NOT the same as cc-plugin-eval (which measures triggering, not task quality)
- NOT optional — RED phase is a hard prerequisite to Gate 3 (exception: simple skill — see above)