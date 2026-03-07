# Mode B: Evaluate & Refine Existing Skill

Workflow for assessing and improving an existing skill.

## Triggers

- "оцени мой скилл", "review this skill", "evaluate skill"
- "улучши скилл", "improve skill", "refine skill"
- "что не так со скиллом", "what's wrong with this skill"

## Step 1: Read Skill Completely

Read ALL files in skill directory:

```
Read SKILL.md
Read references/* (all files)
Read scripts/* (all files)
Read examples/* (all files)
```

Document: total lines, file count, frontmatter fields present.

## Step 1.5: Pre-Screening (5-Axis Quick Score)

Apply 5-axis screen from `references/quick-reference.md` Section 0 (1-10 each, max 50):

| Axis | Score |
|------|-------|
| Discovery | /10 |
| Clarity | /10 |
| Efficiency | /10 |
| Robustness | /10 |
| Completeness | /10 |
| **Total** | /50 |

IF ≥35/50 → proceed to Step 2 (full rubric).
IF <35/50 → note weak axes in report, still run full rubric for complete picture.

## Step 2: Score by Rubric

Apply `references/scoring-rubric.md` (100-point, 5 dimensions × 4 criteria × 5 points).

Output scoring template:

```
Skill: {name}
Date: {date}

Structural:  File naming ___/5  Directory ___/5  Frontmatter ___/5  Size ___/5
Description: Specificity ___/5  Triggers ___/5  POV ___/5  Length ___/5
Density:     Efficiency ___/5  Imperative ___/5  Slop ___/5  Terms ___/5
Complete:    Examples ___/5  Errors ___/5  Edge cases ___/5  Workflows ___/5
Runtime:     Trigger ___/5  Consistency ___/5  Tokens ___/5  Freedom ___/5

TOTAL: ___/100  Grade: ___
```

## Step 3: Check Architecture Pattern Fit

Using `references/architecture-patterns.md` — 5 named patterns:
(Sequential Workflow | Iterative Refinement | Context-Aware Selection | Domain Intelligence | Multi-MCP Coordination)

```
1. Identify which pattern the skill uses (explicit or implicit)
2. Check: does the skill hit any of the 2 disqualifying criteria for that pattern?
3. IF disqualifying criteria met → flag as Major issue, recommend alternative pattern
4. IF pattern not identifiable → flag as architectural drift risk (Minor)
```

## Step 4: Check Anti-Patterns

Scan for all 20 anti-patterns from `references/anti-patterns.md`.
For each found: note pattern name, severity, location.

## Step 5: Check Sizing Rules

From `references/sizing-rules.md`:
- [ ] SKILL.md ≤500 lines (target ≤250)
- [ ] Description ≤1024 chars (target 130-250)
- [ ] Name ≤64 chars, lowercase + hyphens
- [ ] Body <5000 tokens
- [ ] Total skill ≤15k tokens when loaded

## Step 6: Check Description Quality

From `references/description-patterns.md` — 10-point checklist:

- [ ] Directive pattern (ALWAYS invoke... Do NOT... directly)
- [ ] Single-line YAML (no `|` or `>`, no line breaks)
- [ ] Under 250 characters
- [ ] First 50 chars contain primary trigger keyword
- [ ] Third person voice ("Processes..." not "Process...")
- [ ] Contains WHAT + WHEN
- [ ] Has anti-definition (Do NOT use for...)
- [ ] 5+ trigger keywords covering synonyms
- [ ] Conceptual triggers (not just keyword-based)
- [ ] No implementation details in description

## Step 7: Check Degrees of Freedom

From `references/degrees-of-freedom.md`:

For each output-critical section:
- [ ] Freedom level defined (Low/Medium/High)
- [ ] Calibration test applied ("If Claude deviates, worst case?")
- [ ] Style matches freedom level

## Step 8: Check Single-Line YAML

**CRITICAL:** Multi-line YAML breaks skill recognition entirely.

```
FAIL: description: |
        Multi-line text...

FAIL: description: >
        Folded text...

PASS: description: Single line text without line breaks.
PASS: description: "Quoted single line text."
```

## Step 9: Generate Report

```markdown
# Skill Evaluation: {name}

## Score: {total}/100 (Grade {grade})

### Dimension Breakdown
{scoring table from Step 2}

### Issues Found

#### Critical (must fix before deploy)
- {issue}: {location} — {fix}

#### Major (degrades quality significantly)
- {issue}: {location} — {fix}

#### Minor (reduces effectiveness)
- {issue}: {location} — {fix}

### Description Analysis
{10-point checklist results from Step 5}

### Anti-Patterns Detected
{list from Step 4}

### Architecture Pattern Analysis
{findings from Step 3}

### Recommendations (priority order)
1. {highest impact fix}
2. {next fix}
3. {next fix}
```

## Step 10: Apply Fixes (if user requests)

```
IF user wants fixes:
  FOR EACH issue (Critical first, then Major, then Minor):
    1. Apply fix
    2. Explain change
    3. Re-score affected dimension
  END
  Re-run full scoring → output updated report
  Target: score improvement ≥10 points or ≥85/100
```

## Grading Scale

| Score | Grade | Action |
|-------|-------|--------|
| 90-100 | A | Production-ready |
| 75-89 | B | Minor improvements, deployable |
| 60-74 | C | Needs optimization before deploy |
| 40-59 | D | Significant rework needed |
| 0-39 | F | Rebuild from scratch |
