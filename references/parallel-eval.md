# Parallel Evaluation System (Gate 9e)

Three-agent evaluation for complex skills. Provides measurable evidence that skill improves on baseline.

## When to Activate Gate 9e

Gate 9e is **opt-in**, NOT automatic. Activate when:
- User explicitly requests: "запусти полный eval", "проверь параллельно", "deep evaluation"
- Gate 9d shows: delta between with/without skill is <10% → need to diagnose why
- Skill has multi-MCP or orchestrator architecture (Pattern 5) where failure modes are non-obvious

Do NOT activate automatically based on skill size or reference count.

## Three Agents: Contracts

Run all three as parallel subagents (Agent tool). Each has isolated context.

---

### Agent 1: Grader

**Purpose:** assertion checking — does the output contain what it should?

**Context to provide:**
- Skill's SKILL.md
- 3 test scenarios from Gate 2 eval-driven-development.md (Scenarios 1-3)
- Expected outputs documented in Gate 2

**Task instruction:**
```
For each scenario:
1. Simulate running the skill on the scenario input
2. Extract 3-5 specific assertions from the expected output
3. Check each assertion: PASS if present and correct, FAIL if absent or wrong
4. Provide evidence for each verdict (quote the relevant output section)
```

**Output format (JSON):**
```json
{
  "scenario_1": {
    "assertions": [
      {"claim": "output contains section X", "result": "PASS", "evidence": "..."},
      {"claim": "format follows template Y", "result": "FAIL", "evidence": "..."}
    ],
    "pass_rate": 0.8
  },
  "scenario_2": { ... },
  "scenario_3": { ... },
  "overall_pass_rate": 0.87
}
```

**Tools allowed:** Read (skill files only)
**Target:** overall_pass_rate ≥ 0.90

---

### Agent 2: Comparator

**Purpose:** blind A/B — is the with-skill output objectively better than baseline?

**Context to provide:**
- RED baseline output from Gate 2 (without skill)
- Same 3 scenarios (but NOT the skill itself — comparator is blind to instructions)
- Scoring axes definition

**Task instruction:**
```
For each scenario, you have two outputs: Baseline (without skill) and Test (with skill).
Do NOT know which is which until you score them.
Rate each pair on 3 axes (1-5 each):
  - Completeness: does it fully address the scenario?
  - Format adherence: does it follow expected structure?
  - Domain specificity: does it use correct domain knowledge/terms?
After scoring both, reveal which was baseline and which was test.
```

**Output format (JSON):**
```json
{
  "scenario_1": {
    "output_A": {"completeness": 3, "format": 2, "domain": 3, "total": 8},
    "output_B": {"completeness": 4, "format": 5, "domain": 4, "total": 13},
    "skill_is": "B",
    "verdict": "skill_better"
  },
  "overall": "skill_better_in_3_of_3"
}
```

**Tools allowed:** none (text comparison only)
**Target:** skill_better in ≥2 of 3 scenarios on ≥2 of 3 axes

---

### Agent 3: Analyzer

**Purpose:** root cause of Grader failures. Activated only when Grader pass_rate < 0.90.

**Context to provide:**
- Grader output (FAIL items only)
- Skill's SKILL.md and relevant references/

**Task instruction:**
```
For each FAIL assertion from Grader:
1. Identify which section of SKILL.md should have produced this output
2. Classify failure type:
   - missing_instruction: the step doesn't exist in the skill
   - wrong_freedom_level: instruction too vague (High when should be Low) or too rigid
   - ambiguous_wording: instruction can be interpreted multiple ways
   - token_budget: instruction buried in long section (lost-in-middle)
   - wrong_pattern: architectural pattern doesn't fit the workflow
3. Point to specific location (file:section)
4. Suggest minimal fix
```

**Output format (JSON):**
```json
{
  "failures": [
    {
      "assertion": "output contains section X",
      "root_cause": "missing_instruction",
      "location": "SKILL.md:Workflow/Phase2",
      "fix": "Add explicit step: 'Generate section X with fields A, B, C'"
    }
  ]
}
```

**Tools allowed:** Read (skill files only)

---

## Synthesizing Results

After all three agents complete:

| Grader | Comparator | Analyzer | Decision |
|--------|------------|----------|---------|
| ≥90% | skill_better | N/A | SHIP — deliver skill |
| ≥90% | same/worse | N/A | REVIEW — skill may be redundant, check Gate 2 scope |
| <90% | skill_better | root causes found | FIX — apply Analyzer recommendations, re-run Gate 9 |
| <90% | skill_better | no clear root cause | RETHINK — return to Gate 5 (architecture) |
| <90% | skill_worse | root causes found | BLOCK — skill hurts performance, rebuild from Gate 2 |

"REVIEW — skill may be redundant": confirm with user whether the skill is worth maintaining.

## Cost and Time Estimates

| Scope | Agents | Approx tokens | Approx time |
|-------|--------|---------------|-------------|
| Grader only | 1 | ~2k | 1-2 min |
| Grader + Comparator | 2 | ~4k | 2-3 min |
| Full 9e (all 3) | 3 | ~6-8k | 3-5 min |

Run Grader first. Only add Comparator if Grader passes. Only add Analyzer if Grader fails.
This staged approach avoids full 9e cost when not needed.