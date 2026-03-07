# Mode D: Targeted Edit

Surgical fix for a known symptom. Gates 1-9 are NOT run — they were completed during original Mode A.
Scope: one localized change. If systemic issues found → escalate to Mode B.

## When to Use Mode D (not Mode B)

Mode D requires TWO conditions simultaneously:
1. User names a **specific symptom** ("не триггерится на X", "пропускает шаг 3", "выдаёт формат Y вместо Z")
2. Symptom can be **localized to a section** (not "работает плохо", not "нужно улучшить")

IF either condition absent → ask: "Что именно сломано — конкретный пример?"
- Answer is specific → Mode D
- Answer is general → Mode B (references/evaluate-refine.md)

## Step 1: Symptom → Signal Mapping

Map symptom to likely root cause location BEFORE reading any file:

| Symptom | Signal location |
|---------|----------------|
| Not triggering at all (0%) | description frontmatter — multi-line YAML or vague pattern |
| Triggering too rarely (<90%) | description — keywords, directive pattern, first 50 chars |
| Over-triggering (wrong contexts) | description — missing anti-definition (Do NOT) |
| Wrong output format | examples/ section or workflow output spec |
| Skips step N | workflow checkpoint N |
| Inconsistent output across runs | freedom level mismatch or missing examples |
| Too verbose / token-heavy | instruction density — redundant instructions |
| Wrong skill triggers instead | description overlap → scan-all --check-overlap |
| Errors in script | scripts/ file |

IF symptom doesn't map cleanly → STOP Mode D. Declare: "This symptom requires full audit (Mode B)."

## Step 2: Localize — Read Only the Signal Section

Read ONLY the file/section containing the signal. Do NOT read the entire skill.

IF during reading you discover:
- Problem spans >1 unrelated sections
- Root cause is a Critical anti-pattern (anti-patterns.md #1-5)
- Fix would require changing >3 lines across multiple files

→ STOP Mode D. State: "Обнаружена системная проблема: [что именно]. Требуется Mode B."
→ Switch to references/evaluate-refine.md

## Step 3: Root Cause Hypothesis

State explicitly BEFORE touching anything:

```
Root cause: [one sentence hypothesis]
Prediction: changing [specific element] at [file:section] will fix [symptom]
Regression risk: [what could break if wrong]
```

Do not proceed without this statement.

## Step 4: Minimal Fix

Change the minimum required to fix the signal.

Hard rule: if the fix touches >3 lines or >1 file — you are doing Mode B, not Mode D.
If this happens: stop, state the scope, offer to switch to Mode B.

Freedom level check before writing:
- Trigger description → Low (exact directive pattern, no deviation)
- Workflow steps → Medium (structure required, wording flexible)
- Domain heuristics → High (guidelines only)

## Step 5: Regression Check

Run 2+ queries that test paths NOT affected by the fix:

```
IF fixed: description keywords
  Test: workflow execution still produces correct output format
  Test: a different trigger phrase still activates the skill

IF fixed: workflow step N
  Test: step N-1 and step N+1 still execute correctly
  Test: skill still triggers on primary keyword

IF fixed: freedom level in section X
  Test: section X output is now consistent
  Test: sections Y and Z (untouched) still behave as before
```

BLOCK delivery if any regression found. State regression, propose additional fix.

## Step 6: Output

Always close Mode D with this format:

```
Fixed: [symptom described by user]
Root cause: [one sentence]
Changed: [file:section or file:line]
Verified: [which paths were tested and passed]
```

## Mode D Anti-Patterns

- Reading the whole skill directory before localizing → just do Mode B
- Fixing multiple issues in one edit → separate fixes, separate verifications
- Skipping regression check → always verify 2+ unaffected paths
- Hypothesis stated after the fix → always state before
- Fix touches >3 lines → switch to Mode B