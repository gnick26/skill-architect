# Scored Review: code-writing Skill (71/100, Grade C+)

Real community skill evaluated against scoring rubric. Source: UQS Section 11.

## The Skill

```yaml
---
name: code-writing
description: |
  Universal quality coding process: plan, TDD, reviews.
  Use whenever code needs to be written - ad-hoc or as part of a task.
  Use when: "write code", "implement", etc.
  For planning tasks -> tech-spec-planning skill.
  For specs -> user-spec-planning skill.
---
```

## Evaluation

### Structural Compliance: 16/20

| Criterion | Score | Notes |
|-----------|-------|-------|
| File naming | 5/5 | SKILL.md in code-writing/ — correct |
| Directory structure | 4/5 | References to testing-guide.md, universal-patterns.md — good disclosure |
| Frontmatter validity | 4/5 | Name + description present, valid format |
| Size compliance | 3/5 | ~110 lines body — good. But reads 6+ files at startup — heavy |

### Description Quality: 14/20

| Criterion | Score | Notes |
|-----------|-------|-------|
| Specificity | 4/5 | "Universal quality coding process: plan, TDD, reviews" — clear WHAT |
| Trigger conditions | 4/5 | Has "Use when" + anti-definitions pointing to other skills |
| Point of view | 3/5 | Acceptable but body mixes imperative with passive |
| Length optimization | 3/5 | **CRITICAL: Multi-line YAML (`|`) — skill may be invisible!** |

### Instruction Density: 14/20

| Criterion | Score | Notes |
|-----------|-------|-------|
| Token efficiency | 3/5 | "Clarify ambiguities", "Handle edge cases" — Claude already knows |
| Action orientation | 4/5 | Mostly imperative: "Parse Requirements", "Extract what needs to be built" |
| AI slop | 4/5 | Minimal filler, mostly actionable |
| Terminology consistency | 3/5 | Mixes "requirements", "acceptance criteria", "what done looks like" |

### Completeness: 13/20

| Criterion | Score | Notes |
|-----------|-------|-------|
| Examples | 1/5 | **Zero input/output examples.** Biggest weakness |
| Error handling | 3/5 | "Fix any failures" — no specific recovery procedures |
| Edge cases | 2/5 | "Handle edge cases explicitly" — but doesn't describe which |
| Workflows | 5/5 | Excellent: 3-phase with checkpoints, parallel reviews |

### Runtime Performance: 14/20

| Criterion | Score | Notes |
|-----------|-------|-------|
| Trigger accuracy | 4/5 | Good trigger words + anti-definitions for related skills |
| Output consistency | 3/5 | Checkpoints help but no examples = variable format |
| Token consumption | 3/5 | Reads 6+ files regardless of task complexity |
| Freedom calibration | 4/5 | High freedom for code, medium for process — appropriate |

## Total: 71/100 (Grade C+)

## Top 3 Fixes (Priority Order)

### 1. Fix multi-line YAML description (Critical)
**Current:** `description: |` (multi-line — skill may be invisible)
**Fix:** Single-line directive pattern:
```yaml
description: ALWAYS invoke for code writing when user asks to "write code", "implement", "build feature", or "fix bug". Do NOT write code directly -- use this skill's TDD workflow first.
```
**Impact:** Description score +3, potential trigger rate from 0% to 97-100%.

### 2. Add 3-5 concrete examples (+8 points potential)
**Current:** Zero examples — Claude produces different formats each run.
**Fix:** Add examples of checkpoint output, commit message format, summary section.
**Impact:** Completeness/Examples from 1/5 to 4/5.

### 3. Remove redundant instructions (+2 points)
**Current:** "Handle edge cases explicitly", "Comment WHY not WHAT" — Claude knows this.
**Fix:** Remove all instructions that duplicate Claude's training knowledge.
**Impact:** Density/Efficiency from 3/5 to 4/5.

## After Fixes: Estimated 84/100 (Grade B)

| Dimension | Before | After | Delta |
|-----------|--------|-------|-------|
| Structural | 16 | 16 | 0 |
| Description | 14 | 18 | +4 |
| Density | 14 | 16 | +2 |
| Completeness | 13 | 20 | +7 |
| Runtime | 14 | 14 | 0 |
| **Total** | **71** | **84** | **+13** |
