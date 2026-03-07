# Skill Anti-Patterns (20)

Numbered catalog with severity. Check during Mode B evaluation (Step 3).

## Critical (breaks skill functionality)

### 1. Multi-Line YAML Description
**Symptom:** `description: |` or `description: >` in frontmatter.
**Result:** Skill is completely invisible to Claude's auto-selection.
**Fix:** Convert to single-line. No `|`, no `>`, no line breaks.
**Source:** L2-3 — Spence confirmed "Prettier breaking skills."

### 2. Vague Description
**Symptom:** "Helps with various tasks", "Assists users", "Manages things."
**Result:** ~20% trigger rate — effectively invisible.
**Fix:** Directive pattern: "ALWAYS invoke when [specific triggers]."
**Source:** L2-3 — Seleznov, 650 trials, OR=20.6 for directive vs passive.

### 3. Missing WHEN Clause
**Symptom:** Description says WHAT but not WHEN to use.
**Result:** Undertriggering — Claude doesn't know when to activate.
**Fix:** "Use when [trigger1], [trigger2], or [trigger3]."

### 4. Wrong File Naming
**Symptom:** README.md instead of SKILL.md, or wrong casing.
**Result:** Skill not discovered at all.
**Fix:** Must be exactly `SKILL.md`, directory in kebab-case matching `name`.

### 5. XML Tags in Frontmatter
**Symptom:** Angle brackets `<>` in description or other frontmatter fields.
**Result:** Prompt injection vulnerability; parsing errors.
**Fix:** Remove all angle brackets from frontmatter.

## Major (degrades quality significantly)

### 6. Hooks Without Directive Description
**Symptom:** Forced-eval hook added to compensate for weak description.
**Result:** Trigger rate DROPS to 37% (coefficient -2.35, p<0.0001).
**Fix:** Fix description first, add hooks only if still needed.
**Source:** L2-3 — Seleznov experiment, condition C3.

### 7. Oversized SKILL.md
**Symptom:** >500 lines with embedded documentation.
**Result:** Lost-in-middle effect, instruction dilution.
**Fix:** Extract to references/, keep SKILL.md ≤250 lines.

### 8. Kitchen Sink Scope
**Symptom:** Single skill handles unrelated tasks ("bugs AND marketing").
**Result:** Unpredictable triggering, confused execution.
**Fix:** Split by Single Job-to-be-Done principle.

### 9. Missing Anti-Definition
**Symptom:** No "Do NOT use for..." boundaries.
**Result:** Overtriggering on adjacent domains.
**Fix:** Add 2+ explicit negative triggers.

### 10. No Examples
**Symptom:** Zero input/output examples in skill.
**Result:** Inconsistent output format across runs.
**Fix:** Add 3-5 concrete input/output pairs.

### 11. Redundant Instructions
**Symptom:** "Be thorough", "Check your work", "Handle edge cases."
**Result:** Token waste — Claude already knows these.
**Fix:** Only add procedural knowledge Claude lacks.

### 12. Deep Nested References
**Symptom:** `references/sub/sub/file.md` — 2+ levels deep.
**Result:** Claude may read incompletely or miss files.
**Fix:** Keep references 1 level deep.

### 13. Generic First 50 Characters
**Symptom:** "Proactive framework for evidence-based..." before any trigger keyword.
**Result:** Budget truncation hides trigger keywords.
**Fix:** Front-load: trigger keyword in first 50 chars.
**Source:** L2-3 — alexey-pelykh gist, budget truncation left-to-right.

## Minor (reduces effectiveness)

### 14. AI Slop
**Symptom:** "It's important to note that...", "This comprehensive solution..."
**Result:** Token waste on filler.
**Fix:** Remove all hedging language.

### 15. Inconsistent Terminology
**Symptom:** "requirements", "specs", "acceptance criteria" for same concept.
**Result:** Claude confused about meaning.
**Fix:** One term per concept throughout.

### 16. Wrong Point of View
**Symptom:** "I will analyze" or "You should use when."
**Result:** Semantic matching confusion.
**Fix:** Third person: "Analyzes...", "Processes..."

### 17. Hardcoded Credentials
**Symptom:** API keys, passwords in scripts or SKILL.md.
**Result:** Credential exposure.
**Fix:** Use environment variables or MCP.

### 18. Description Over 250 Chars
**Symptom:** Description length 300-500+ chars.
**Result:** Budget waste, diluted attention, fewer skills fit.
**Fix:** Trim to 130-250 chars (max 1024 by spec).

### 19. Implementation Details in Description
**Symptom:** "via mcp-cli without loading tool definitions into context."
**Result:** Wasted description budget on non-routing info.
**Fix:** Description is for routing only. Details go in SKILL.md body.

### 20. Provenance in Description
**Symptom:** "Fork of X adapted for Y architecture."
**Result:** Wasted description budget on history.
**Fix:** Remove provenance. Document in SKILL.md body or references.

## Recovery Pattern

When anti-pattern detected during evaluation:

1. STOP current work
2. Identify specific anti-pattern by number and severity
3. State required fix
4. Apply fix (if user requests)
5. Re-score affected dimensions
