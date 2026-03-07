---
name: skill-architect
description: ALWAYS invoke for Agent Skills creation, evaluation, or import when user says "create skill", "build skill", "evaluate skill", "review skill", "import skill", or discusses packaging expertise into reusable instructions. Do NOT create or modify skills directly -- use this protocol first.
---

# Skill Architect Protocol v2

Gatekeeper for Agent Skills lifecycle. No creation proceeds until ALL gates pass.
Three modes: Create (A), Evaluate (B), Import (C).

## Gate 0: Intent Classification

```
IF "create skill", "build skill", "new skill", "design skill" → Mode A: Gate 1
IF "import skill", "check downloaded skill" → Mode C: Gate 0i
IF "evaluate skill", "review skill", "улучши скилл" → Mode B: references/evaluate-refine.md
IF general question about skills → Answer directly. Do NOT start protocol.
```

## Gate 0i: Import Security Scan (Mode C)

```bash
skill-scanner scan <path> --use-behavioral --use-trigger --yara-mode strict --fail-on-findings --format json
```

IF exit ≠0 (CRITICAL/HIGH) → BLOCK: "Import rejected. Manual audit required."
IF MEDIUM findings → WARNING: show findings, user decides.
IF clean → PASS → Mode B (quality evaluation).

Details: references/import-assessment.md

## Gate 1: Examples Collection (BLOCK: <3)

Request 3+ concrete examples: `[User says "..." → Expected action/output]`
Analyze for: common patterns, required tools, output format, edge cases.
IF insufficient → BLOCK: "What exact phrases trigger this? What tangible output?"
- [ ] Checkpoint: ≥3 examples with triggers and expected outputs

## Gate 2: Eval-Driven Development

Anthropic's 5-step cycle:
1. **Identify gaps** — run task WITHOUT skill, document failures
2. **Create evaluations** — 3 test scenarios from examples
3. **Establish baseline** — record unassisted performance
4. **Write minimal instructions** — only what fixes observed gaps
5. **Iterate** — compare with baseline after building

Simple skills: informal baseline. Complex: use references/eval-driven-development.md template.
- [ ] Checkpoint: gaps identified, 3+ scenarios, baseline noted

## Gate 3: Complexity Assessment

| Metric | OK | Split |
|--------|----|-------|
| Decision branches | ≤5 | >5 |
| Tool types | ≤2 | >3 |
| Workflow steps | ≤7 | >10 |

IF split → recommend decomposition: Skill A + Skill B + Orchestrator.

## Gate 4: Domain Knowledge

IF expertise demonstrated in examples → PROCEED.
IF domain unclear → REQUIRE research. BLOCK until completed.
Non-code skills: require decision trees, quality rubrics, success criteria.

## Gate 5: Architecture Selection

```
Encodes expertise/knowledge? → SKILL
Needs autonomous multi-step? → AGENT (Task tool)
Needs external API/data? → MCP SERVER
Simple automation? → SCRIPT (bash/python)
Hybrid valid: Skill+MCP, Skill+Agent
```

## Gate 6: Structure Design (BLOCK: no freedom level)

### Sizing
| Component | Target | Spec Max |
|-----------|--------|----------|
| SKILL.md | ≤250 lines | <500 lines, <5000 tokens |
| Description | 130-250 chars | 1024 chars |
| Name | — | 64 chars, lowercase+hyphens |

Details: references/sizing-rules.md

### Progressive Disclosure
```
skill-name/
├── SKILL.md        # Core workflow (≤250 lines)
├── references/     # On-demand details
├── scripts/        # Validation
├── examples/       # Few-shot
└── assets/         # Static (not loaded)
```
IF >3 references → recommend `context: fork`.

### Degrees of Freedom (MANDATORY)

For EACH output-critical section:
- **Low** (standards, deploy): exact commands, no deviation
- **Medium** (preferred approach): templates, required structure
- **High** (many valid approaches): heuristics, guidelines

Calibration: "If Claude deviates, worst case?" → "Different style"=High | "Wrong format"=Medium | "Broken standard"=Low
**BLOCK** if no freedom level for output-critical sections.
Details: references/degrees-of-freedom.md
- [ ] Checkpoint: sizing OK, directories planned, freedom defined

## Gate 7: Description Engineering (CRITICAL)

### Directive Pattern (MUST USE)
```yaml
description: ALWAYS invoke this skill when [triggers]. Do NOT [alternative] directly -- use this skill first.
```

### 10-Point Checklist
- [ ] Directive pattern (ALWAYS invoke... Do NOT...)
- [ ] Single-line YAML (CRITICAL: multi-line = invisible)
- [ ] Under 250 chars (max 1024)
- [ ] First 50 chars = primary trigger keyword
- [ ] Third person voice
- [ ] WHAT + WHEN
- [ ] Anti-definition (Do NOT use for...)
- [ ] 5+ trigger keywords with synonyms
- [ ] Conceptual triggers (problem descriptions)
- [ ] No implementation details

IF user-invocable only → add `disable-model-invocation: true` (saves budget).
Details: references/description-patterns.md
- [ ] Checkpoint: all 10 checks pass

## Gate 8: Content Generation

Write SKILL.md with:
- **Frontmatter:** name (kebab-case) + directive description + minimal allowed-tools
- **Style:** imperative voice, ## headers, IF/ELSE trees, `- [ ] Checkpoint:` after steps
- **Required sections:** When to Use, When NOT to Use, Workflow, Decision Points, Validation, References
- **Rule:** link to references, don't embed content

Templates: references/templates/{minimal,workflow,expertise,mcp-enhancement}.md

## Gate 9: Validation

**9a. Structural:** Run `scripts/validate_skill.py <dir>` — frontmatter, name, description, size, no XML.
**9b. Scoring:** Apply references/scoring-rubric.md. Target: ≥85/100.
**9c. Triggers:** 10 positive + 5 negative prompts. Target: ≥90% trigger, <10% FP.
**9d. Baseline:** Compare with Gate 2 metrics → confirm improvement.

IF <85 score or <90% trigger → iterate before delivery.
- [ ] Checkpoint: all validation passes

## Output Protocol

After ALL gates pass, output: skill name, location, score, triggers, scope, freedom levels, 3 test queries, reminder to `scan-all --check-overlap`.

## References

- [evaluate-refine.md](references/evaluate-refine.md) — Mode B: evaluate & refine workflow
- [import-assessment.md](references/import-assessment.md) — Gate 0i: security scan
- [eval-driven-development.md](references/eval-driven-development.md) — Gate 2: Anthropic 5-step cycle
- [description-patterns.md](references/description-patterns.md) — Gate 7: trigger engineering
- [sizing-rules.md](references/sizing-rules.md) — Gate 6: spec constraints
- [activation-hooks.md](references/activation-hooks.md) — Hook effectiveness data
- [degrees-of-freedom.md](references/degrees-of-freedom.md) — Gate 6: freedom calibration
- [scoring-rubric.md](references/scoring-rubric.md) — Gate 9: 100-point rubric
- [anti-patterns.md](references/anti-patterns.md) — 20 anti-patterns with severity
- [quick-reference.md](references/quick-reference.md) — 4 checklists
- [claude-code-extensions.md](references/claude-code-extensions.md) — Frontmatter extensions
- [tools-ecosystem.md](references/tools-ecosystem.md) — skill-scanner, cc-plugin-eval, SkillCheck
