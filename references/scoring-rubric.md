# Universal Scoring Rubric

Score each dimension 0-5. Total possible: 100 points (20 criteria x 5 points).

## Dimension 1: Structural Compliance (20 points)

| Criterion | 0 | 1-2 | 3 | 4-5 |
|-----------|---|-----|---|-----|
| **File naming** | Wrong filename or casing | Some issues | SKILL.md correct, minor folder issues | Perfect: SKILL.md, kebab-case dir |
| **Directory structure** | No structure | Flat files | Scripts/references exist but unorganized | Clean progressive disclosure hierarchy |
| **Frontmatter validity** | Missing or broken YAML | Missing required fields | Name + description present, minor issues | All fields valid, optional fields where needed |
| **Size compliance** | >1000 lines | 500-1000 lines | 300-500 lines | <300 lines, well-split with references |

## Dimension 2: Description Quality (20 points)

| Criterion | 0 | 1-2 | 3 | 4-5 |
|-----------|---|-----|---|-----|
| **Specificity** | "Helps with things" | Generic but has some keywords | Specific WHAT | Precise WHAT with domain keywords |
| **Trigger conditions** | No WHEN clause | Vague when-to-use | Clear WHEN with some triggers | Comprehensive WHEN + anti-definitions |
| **Point of view** | First person "I help" | Mixed | Mostly third person | Consistently third person |
| **Length optimization** | Too short (<20 chars) or too long (>1024) | Suboptimal length | Good length, could be tighter | Optimal: maximum information density within 130-250 chars |

## Dimension 3: Instruction Density (20 points)

| Criterion | 0 | 1-2 | 3 | 4-5 |
|-----------|---|-----|---|-----|
| **Token efficiency** | Explains what Claude knows | Some redundancy | Mostly unique knowledge | Only procedural knowledge Claude lacks |
| **Action orientation** | Passive, descriptive | Mixed | Mostly imperative | Fully imperative: "Use", "Run", "Check" |
| **AI slop** | Pervasive filler | Noticeable filler | Occasional | Zero filler, every sentence earns its tokens |
| **Terminology consistency** | 3+ terms for same concept | 2 terms for same concept | Mostly consistent | One term per concept throughout |

## Dimension 4: Completeness (20 points)

| Criterion | 0 | 1-2 | 3 | 4-5 |
|-----------|---|-----|---|-----|
| **Examples** | None | 1-2 abstract examples | 3 concrete examples | 5+ realistic input/output pairs |
| **Error handling** | None | Mentions errors exist | Documents common failures | Full recovery procedures with scripts |
| **Edge cases** | Not addressed | Mentioned | Documented | Documented with handling instructions |
| **Workflows** | No structure | Linear steps | Steps with checkpoints | Checklist pattern with feedback loops |

## Dimension 5: Runtime Performance (20 points)

| Criterion | 0 | 1-2 | 3 | 4-5 |
|-----------|---|-----|---|-----|
| **Trigger accuracy** | <50% | 50-70% | 70-90% | >90% with F1 > 0.85 |
| **Output consistency** | Different every run | Some variation | Mostly consistent | Identical structure 5/5 runs |
| **Token consumption** | More tokens than no-skill | Same as no-skill | 20-50% reduction | >50% reduction vs baseline |
| **Freedom calibration** | Mismatch (low freedom for flexible tasks) | Partial match | Good match for main use case | Perfect match across all use cases |

## Grading Scale

| Score | Grade | Meaning |
|-------|-------|---------|
| 90-100 | A | Production-ready, reference quality |
| 75-89 | B | Good quality, minor improvements possible |
| 60-74 | C | Functional but needs optimization |
| 40-59 | D | Significant issues, needs rework |
| 0-39 | F | Fundamentally broken, rebuild required |

## Quick Scoring Template

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
