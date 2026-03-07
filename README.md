# skill-architect

**Gatekeeper protocol for Agent Skills lifecycle.**

Enforces quality gates before any Agent Skill is created, evaluated, imported, or surgically edited in Claude Code.

## Four modes

- **Mode A (Create):** 9-gate workflow — examples → RED baseline → architecture pattern → generation → validation
- **Mode B (Evaluate):** Score existing skills against 100-point rubric, find anti-patterns, refine
- **Mode C (Import):** Security scan external skills before adoption
- **Mode D (Edit):** Surgical fix for a specific symptom without regression — bypasses Gates 1-9

## Structure

```
SKILL.md                          # Core protocol (≤250 lines)
references/
  eval-driven-development.md      # RED phase + Anthropic 5-step cycle
  evaluate-refine.md              # Mode B: full evaluation workflow
  edit-mode.md                    # Mode D: targeted fix protocol
  architecture-patterns.md        # 5 named patterns with disqualifiers
  parallel-eval.md                # Gate 9e: 3-agent evaluation system
  quick-reference.md              # 5 checklists + 5-axis pre-screening
  scoring-rubric.md               # 100-point rubric (20 dimensions)
  anti-patterns.md                # 20 anti-patterns with severity
  description-patterns.md         # Trigger engineering (OR=20.6)
  degrees-of-freedom.md           # Low/Medium/High calibration
  import-assessment.md            # Gate 0i: security scan detail
  sizing-rules.md                 # Spec constraints
  activation-hooks.md             # Hook effectiveness data
  claude-code-extensions.md       # Frontmatter extensions
  tools-ecosystem.md              # skill-scanner, cc-plugin-eval, scripts
  templates/                      # minimal, workflow, expertise, mcp-enhancement
scripts/
  init_skill.py                   # Scaffold new skill directory
  package_skill.py                # Package into distributable .skill file
  validate_skill.py               # Structural validator
  quick_validate.py               # Fast validation (used by package_skill.py)
examples/
  good-skill.md                   # Reference implementation
  bad-skill.md                    # Anti-pattern examples
  scored-review.md                # Annotated evaluation session
  edit-mode-session.md            # Mode D walkthrough (success + escalation)
```

## Key features (v3)

- **RED Phase** — mandatory baseline before writing any skill (Type 1 executable / Type 2 hypothetical)
- **5 architecture patterns** with disqualifying criteria (Sequential, Iterative, Context-Aware, Domain Intelligence, Multi-MCP)
- **Mode D (Edit)** — Specificity Test routes to surgical fix vs full audit
- **Gate 9e** — opt-in 3-agent parallel evaluation (Grader / Comparator / Analyzer)
- **5-axis pre-screening** before 100-point rubric
- 100-point scoring rubric (20 dimensions, 5 categories)
- Degrees of Freedom calibration (Low/Medium/High per section)
- Description engineering with empirical trigger data (OR=20.6)
- 20 anti-patterns with severity levels
- Gate 0i security scan for imported skills (Cisco AI Defense skill-scanner)

## Usage

Install into Claude Code:

```bash
# Copy to your skills directory
cp -r skill-architect ~/.claude/skills/

# Scaffold a new skill
python ~/.claude/skills/skill-architect/scripts/init_skill.py my-skill --path ~/.claude/skills/

# Validate an existing skill
python ~/.claude/skills/skill-architect/scripts/validate_skill.py ~/.claude/skills/my-skill/

# Package for distribution
python ~/.claude/skills/skill-architect/scripts/package_skill.py ~/.claude/skills/my-skill/
```

Then reference `skill-architect` in your Claude Code system prompt or CLAUDE.md.

---

*Part of the Claude Code Agent Skills ecosystem.*
