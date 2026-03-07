# Example: Mode D Edit Session

Demonstrates surgical fix workflow. Shows correct routing, localization, hypothesis, fix, and regression check.

---

## Session 1: Missing Trigger Language

**User says:** "Мой скилл для коммитов не реагирует когда я говорю 'зафиксируй изменения' — только на английские команды работает"

### Gate 0 Routing

Symptom: specific ("не реагирует на 'зафиксируй изменения'")
Localization: known ("только английские команды") → description keywords
Decision: Mode D ✓

### Step 1: Symptom → Signal

| Symptom | Maps to |
|---------|---------|
| Not triggering on Russian phrase | description frontmatter — trigger keywords |

### Step 2: Read Only Frontmatter

```yaml
---
name: commit-helper
description: ALWAYS invoke when user says "commit", "git commit", "make a commit", or wants to create a commit message. Do NOT write commit messages directly -- use this skill first.
---
```

No systemic issues found. Problem is isolated: keywords English-only.

### Step 3: Root Cause Hypothesis

```
Root cause: description trigger keywords contain only English phrases.
Russian-language queries ("зафиксируй", "сохрани изменения") not covered.
Prediction: adding Russian synonyms to description will fix the trigger gap.
Regression risk: description length may exceed 250 chars — check after edit.
```

### Step 4: Minimal Fix

Before: 164 chars
```yaml
description: ALWAYS invoke when user says "commit", "git commit", "make a commit", or wants to create a commit message. Do NOT write commit messages directly -- use this skill first.
```

After: 218 chars (within 130-250 target ✓)
```yaml
description: ALWAYS invoke when user says "commit", "git commit", "зафиксируй", "сохрани изменения", or wants to create a commit message. Do NOT write commit messages directly -- use this skill first.
```

Changed: SKILL.md:3 — added 2 Russian keyword phrases to description.

### Step 5: Regression Check

Test 1 (unaffected path — English trigger):
Query: "make a commit for my changes" → skill activates ✓

Test 2 (unaffected path — slash command):
Query: /commit → skill activates ✓

No regression found.

### Step 6: Output

```
Fixed: скилл не реагировал на русские фразы
Root cause: description содержала только английские ключевые слова
Changed: SKILL.md:3 — добавлены "зафиксируй", "сохрани изменения"
Verified: English trigger + slash command не затронуты
```

---

## Session 2: Mode D Escalates to Mode B

**User says:** "Скилл иногда пропускает второй шаг в воркфлоу"

### Gate 0 Routing

Symptom: specific ("пропускает второй шаг")
Localization: workflow Step 2
Decision: Mode D tentative — need to localize

### Step 2: Read Workflow Section

```markdown
## Workflow

### Step 1: Analyze input
Parse user request and extract key parameters.

### Step 2: Validate parameters
[no checkpoint here]

### Step 3: Execute
Run with validated parameters.
```

During reading: Step 2 has no checkpoint → Claude skips it when confident about parameters.
BUT also notices: Step 1 has no example of what "key parameters" means → ambiguous.
AND: Step 3 references "validated parameters" without defining validation criteria.

**Systemic issue detected**: the problem isn't "missing checkpoint in Step 2" alone. Steps 1, 2, 3 are semantically coupled and all have gaps. Touching Step 2 checkpoint without fixing Steps 1 and 3 would create inconsistency.

### Escalation

STOP Mode D.

"Обнаружена системная проблема: шаги 1-3 семантически связаны и все имеют пробелы — недостаточно примеров, неопределённые критерии, отсутствующие checkpoint'ы. Хирургический fix Step 2 не решит проблему. Нужен полный аудит (Mode B). Запускаю evaluate-refine.md?"

---

## Why These Two Sessions Differ

Session 1: symptom → one section → one field → one line change. True Mode D.
Session 2: symptom → section → reveals 3 coupled gaps → must be Mode B.

The escape in Session 2 is not a failure — it's Mode D working correctly. The goal is surgical precision, and that requires knowing when surgery is not the right procedure.