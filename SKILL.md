---
name: skill-architect
description: "ALWAYS invoke for Agent Skills lifecycle: create, evaluate, import, or fix skills. Handles создай скилл, оцени скилл, build skill, review skill. Do NOT create/modify/evaluate skills directly -- use this protocol first."
---

# Skill Architect Protocol v3

Gatekeeper for Agent Skills lifecycle. No creation proceeds until ALL gates pass.
Four modes: Create (A), Evaluate (B), Import (C), Edit (D).

## Gate 0: Intent Classification

```
IF specific symptom named ("не триггерится на X", "пропускает шаг N", "выдаёт формат Y") → SPECIFICITY TEST below
IF "create skill", "build skill", "new skill", "design skill" → Mode A: Gate 1
IF "import skill", "check downloaded skill" → Mode C: Gate 0i
IF "evaluate skill", "review skill", "улучши скилл", "improve skill" → Mode B: references/evaluate-refine.md
IF general question about skills → Answer directly. Do NOT start protocol.
```

Note: Specificity Test runs FIRST. Compound requests like "улучши скилл — он не триггерится на X" route to Mode D (not Mode B) because symptom is specific and localizable.

### Specificity Test (for ambiguous "fix" / "broke" / "починить" queries)

Ask: "Does user name a SPECIFIC symptom AND can it be localized to a section?"
- BOTH yes → Mode D: references/edit-mode.md
  Note: Mode D bypasses Gates 1-9. Gates were completed during original Mode A.
- Either NO → ask ONE clarifying question: "Что именно сломано — конкретный пример?"
  - Answer specific → Mode D
  - Answer general → Mode B

## Gate 0.6: Body-edit invariants

Skill body = executable instrument. Every skill Write/Edit:
- **Minimal, unambiguous** — only directives the model executes; model-read test each line; cut the rest.
- **No volatile content** — no history, rationale, logs, time-bound or variable data.
- **Consistency sweep** — editing an item that overlaps existing instructions ⇒ re-read all directives in the skill's context window; keep them consistent, ordered, non-duplicated.
- **English only.**

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

**RED Phase (MANDATORY):** Run target task WITHOUT skill before writing anything.
- Type 1 (can run now): execute one Gate 1 example → capture output
- Type 2 (domain/MCP dependency): write "Claude would [X], gap: [Y]"
- Simple skill exception (≤1 workflow + domain gap + clear from Gate 1) → Type 2 sufficient
- BLOCK if neither done. Stop if Type 1 ≥90% complete → skill not needed.

**GREEN Phase (Anthropic 5-step):** gaps → evaluations → baseline → minimal instructions → iterate.
Details and exception criteria: references/eval-driven-development.md
- [ ] Checkpoint: RED completed (Type 1 or 2), gaps documented, 3+ scenarios, baseline recorded

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

IF → SKILL: select pattern from references/architecture-patterns.md
  (Sequential | Iterative | Context-Aware | Domain Intelligence | Multi-MCP)
  Then validate: check 2 disqualifying criteria for chosen pattern.
  BLOCK if pattern disqualified → choose different pattern.

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
├── scripts/        # Validation + scaffolding
├── examples/       # Few-shot
└── assets/         # Static (not loaded into context)
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

Scaffold: run `scripts/init_skill.py <name> --path <dir>` to create directory structure.

Write SKILL.md with:
- **Frontmatter:** name (kebab-case) + directive description + minimal allowed-tools
- **Style:** imperative voice, ## headers, IF/ELSE trees, `- [ ] Checkpoint:` after steps
- **Required sections:** When to Use, When NOT to Use, Workflow, Decision Points, Validation, References
- **Rule:** link to references, don't embed content

Templates: references/templates/{minimal,workflow,expertise,mcp-enhancement}.md

## Gate 9: Validation

**9a. Structural:** Run `scripts/validate_skill.py <dir>` — frontmatter, name, description, size, no XML.
**9b. Scoring:** Quick 5-axis screen (references/quick-reference.md Section 0). If ≥35/50 → full scoring-rubric.md. Target: ≥85/100.
**9c. Triggers:** 10 positive + 5 negative prompts. Target: ≥90% trigger, <10% FP.
**9d. Baseline delta:** Compare with Gate 2 RED metrics. BLOCK if improvement <10% over baseline.
**9e. Parallel eval [opt-in]:** Run when user requests deep eval OR Gate 9d delta <10% but sign of real improvement.
  See references/parallel-eval.md — Grader → Comparator → Analyzer (staged, not all at once).

IF <85 score or <90% trigger → iterate before delivery.
- [ ] Checkpoint: all validation passes

## Output Protocol

**Mode A/C:** skill name, location, score, triggers, scope, freedom levels, 3 test queries, reminder to `scan-all --check-overlap`. Package with `scripts/package_skill.py <dir>` for distribution.

**Mode B:** evaluation report per references/evaluate-refine.md Step 8.

**Mode D:** `Fixed: [symptom] | Root cause: [one sentence] | Changed: [file:section] | Verified: [paths tested]`

## References

- [evaluate-refine.md](references/evaluate-refine.md) — Mode B: evaluate & refine workflow
- [edit-mode.md](references/edit-mode.md) — Mode D: targeted fix without regression
- [import-assessment.md](references/import-assessment.md) — Gate 0i: security scan
- [eval-driven-development.md](references/eval-driven-development.md) — Gate 2: RED phase + Anthropic 5-step cycle
- [architecture-patterns.md](references/architecture-patterns.md) — Gate 5: 5 named patterns with validation
- [description-patterns.md](references/description-patterns.md) — Gate 7: trigger engineering
- [sizing-rules.md](references/sizing-rules.md) — Gate 6: spec constraints
- [activation-hooks.md](references/activation-hooks.md) — Hook effectiveness data
- [degrees-of-freedom.md](references/degrees-of-freedom.md) — Gate 6: freedom calibration
- [scoring-rubric.md](references/scoring-rubric.md) — Gate 9: 100-point rubric
- [parallel-eval.md](references/parallel-eval.md) — Gate 9e: 3-agent evaluation system
- [anti-patterns.md](references/anti-patterns.md) — 20 anti-patterns with severity
- [quick-reference.md](references/quick-reference.md) — 5 checklists + 5-axis pre-screening
- [claude-code-extensions.md](references/claude-code-extensions.md) — Frontmatter extensions
- [tools-ecosystem.md](references/tools-ecosystem.md) — skill-scanner, cc-plugin-eval, init_skill.py, package_skill.py