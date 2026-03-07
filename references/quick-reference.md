# Quick Reference Card

5 checklists for skill lifecycle — use as pre-flight checks at each stage.

## 0. Pre-Screening: 5-Axis Quick Score

Before running full Mode B audit, screen with 5-axis (1-10 each, max 50):

| Axis | Question |
|------|----------|
| Discovery | Does Claude find and activate this skill reliably? |
| Clarity | Would another Claude understand instructions unambiguously? |
| Efficiency | Does the skill reduce token cost vs baseline? |
| Robustness | Does it handle edge cases without breaking? |
| Completeness | Does it cover all scenarios from Gate 1 examples? |

| Score | Action |
|-------|--------|
| ≥35/50 | Run full Mode B (scoring-rubric.md) |
| <35/50 | Identify weak axes, fix before full rubric |

Note: 5-axis is screening only. Final standard = 100-point rubric (≥85/100).

## 1. Before Writing a Skill

```
[ ] Identified a gap Claude can't cover without the skill
[ ] RED Phase completed (Type 1 run OR Type 2 documented)
[ ] RED shows gap exists (Claude <90% without skill)
[ ] Created 3+ test scenarios (positive, negative, edge case)
[ ] Confirmed this needs a SKILL (not agent, MCP, or script)
[ ] Architecture pattern selected and validated (Gate 5)
```

## 2. YAML Frontmatter Checklist

```
[ ] name: lowercase + hyphens, ≤64 chars, matches dirname
[ ] description: single-line YAML, ≤250 chars (max 1024)
[ ] description: directive pattern (ALWAYS invoke... Do NOT...)
[ ] description: third person, WHAT + WHEN, trigger keywords in first 50 chars
[ ] No XML angle brackets in frontmatter
[ ] allowed-tools: set if needed (least privilege)
[ ] disable-model-invocation: true if user-invocable only
[ ] context: fork if >3 references or risky operations
```

## 3. SKILL.md Body Checklist

```
[ ] ≤250 lines (spec max 500), body <5000 tokens
[ ] Only procedural knowledge Claude doesn't have
[ ] Imperative voice throughout ("Execute X", not "You should...")
[ ] 3-5 concrete input/output examples with realistic data
[ ] Error handling with specific recovery procedures
[ ] Consistent terminology (one term per concept)
[ ] References to external files with WHEN to read each
[ ] No AI slop, no filler, no general explanations
[ ] Workflows as checklists with checkpoints
[ ] Degrees of Freedom defined for output-critical sections
```

## 4. Post-Creation Checklist

```
[ ] Tested with 10 relevant queries (trigger rate ≥90%)
[ ] Tested with 5 irrelevant queries (false positive rate <10%)
[ ] Run same request 3-5 times (output format consistent)
[ ] Compared baseline vs with-skill (delta measurable, >10%)
[ ] validate_skill.py passes without errors
[ ] No overlap with existing skills (scan-all --check-overlap)
[ ] Score ≥85/100 by scoring rubric
```

## 5. Mode D: Before Editing an Existing Skill

```
[ ] Symptom is specific and named (not "плохо работает" but "не триггерится на X")
[ ] Symptom maps to a signal location (see edit-mode.md Step 1 table)
[ ] Asked clarifying question if symptom was vague — got specific answer
[ ] Hypothesis stated BEFORE touching anything (Root cause + Prediction)
[ ] Read ONLY the section containing the signal (not the whole skill)
[ ] Fix touches ≤3 lines in ≤1 file
[ ] No systemic issues discovered during read (if yes → switch to Mode B)
[ ] Ran 2+ unaffected paths to verify no regression
[ ] Output: "Fixed: X | Root cause: Y | Changed: Z | Verified: W"
```