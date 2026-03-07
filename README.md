# skill-architect

**Gatekeeper protocol for Agent Skills lifecycle.**

Enforces quality gates before any Agent Skill is created, evaluated, or imported into Claude Code.

## Three modes

- **Mode A (Create):** 9-gate workflow from examples → eval → architecture → generation → validation
- **Mode B (Evaluate):** Score existing skills against 100-point rubric, find anti-patterns, refine
- **Mode C (Import):** Security scan external skills before adoption

## Structure

```
SKILL.md              # Core protocol (≤250 lines)
references/           # On-demand detail files
scripts/              # validate_skill.py, quick_validate.py
examples/             # good-skill, bad-skill, scored-review
```

## Key features

- 100-point scoring rubric (20 dimensions, 5 categories)
- Degrees of Freedom calibration (Low/Medium/High per section)
- Description engineering with empirical trigger data (OR=20.6)
- 20 anti-patterns with severity levels
- Gate 0i security scan for imported skills

---

*Part of the Claude Code Agent Skills ecosystem.*
