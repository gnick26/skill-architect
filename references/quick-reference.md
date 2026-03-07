# Quick Reference Card

4 checklists for skill creation — use as pre-flight checks at each stage.

## 1. Before Writing a Skill

```
[ ] Identified a gap Claude can't cover without the skill
[ ] Created 3+ test scenarios (positive, negative, edge case)
[ ] Measured baseline (without skill): success rate, output quality
[ ] Confirmed this needs a SKILL (not agent, MCP, or script)
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
[ ] Compared baseline vs with-skill (improvement measurable)
[ ] validate_skill.py passes without errors
[ ] No overlap with existing skills (scan-all --check-overlap)
[ ] Score ≥85/100 by scoring rubric
```
