# Architecture Patterns for Skills

Use at Gate 5 after confirming SKILL (not Agent/MCP/Script).
Select ONE primary pattern. Hybrid valid only with explicit rationale.

## Selection Matrix

| Pattern | Choose when | Avoid when |
|---------|------------|------------|
| Sequential Workflow | Fixed order, each step depends on previous | Steps can reorder or be skipped |
| Iterative Refinement | Output improves in cycles toward quality threshold | No measurable stopping criterion |
| Context-Aware Selection | Multiple valid paths, input determines route | All inputs follow the same path |
| Domain Intelligence | Encode non-obvious expertise Claude lacks | Knowledge already in Claude's training |
| Multi-MCP Coordination | Requires 2+ external services in sequence | One MCP or zero MCPs needed |

## Pattern Validation (run after selection)

For each pattern, 2 disqualifying criteria. If EITHER fails → choose different pattern.

### Pattern 1: Sequential Workflow

**Use for:** deploy checklists, code review, structured reporting, onboarding flows.

**Disqualifiers:**
- Gate 1 examples show step order varies by context → Context-Aware instead
- Any step is optional or conditional on >1 input variable → Iterative or Context-Aware

**Structure:**
```
Phase 1: [name] (Objective: ...)
  Steps 1-N with checkpoint
  BLOCK if checkpoint fails

Phase 2: [name]
  Steps with checkpoint

Phase N: Validation
  Final checklist before delivery
```

**Key rules:** Each phase has exactly one checkpoint. BLOCK on failure = no skipping phases.
Freedom level: Medium for steps, Low for checkpoints.

---

### Pattern 2: Iterative Refinement

**Use for:** draft → feedback → rewrite loops, score-based improvement, quality tuning.

**Disqualifiers:**
- No measurable quality threshold ("done when it looks right" is not a threshold) → Sequential instead
- Fixed steps with no loop → Sequential

**Structure:**
```
Iteration 0: Initial output
Loop (max N iterations):
  Assess: [quality metric] vs threshold [X]
  IF threshold met → EXIT loop, deliver
  IF not → identify delta, apply targeted improvement
  IF iteration N reached → deliver best result, flag to user
```

**Key rules:** Stopping criterion must be defined before writing skill. Max iterations = explicit number.
Freedom level: High for improvement heuristics, Low for stopping criterion.

---

### Pattern 3: Context-Aware Selection

**Use for:** language-specific handling, role-based workflows, format-dependent processing.

**Disqualifiers:**
- Fewer than 3 distinct input contexts in Gate 1 examples → Sequential with IF branches
- All contexts share >70% of steps → Sequential with optional steps

**Structure:**
```
Step 1: Context Detection
  Identify: [context signals from input]
  Classify into: [context A | context B | context C | default]

Step 2: Route
  IF context A → [workflow A]
  IF context B → [workflow B]
  ELSE → [default workflow]

Each workflow: self-contained with own checkpoint
```

**Key rules:** Default path mandatory. Context detection must be deterministic (not LLM judgement).
Freedom level: Low for detection logic, High for workflow content.

---

### Pattern 4: Domain Intelligence

**Use for:** legal review, financial modeling, domain-specific QA, company-specific knowledge.

**Disqualifiers:**
- Claude's base knowledge covers the domain at required depth → no skill needed (Gate 2 RED will show this)
- Knowledge is factual lookup only → use references/ file, not a full pattern

**Structure:**
```
Domain Model:
  Core concepts: [list]
  Decision rules: [IF/THEN trees]
  Quality rubrics: [criteria with thresholds]
  Edge case catalog: [known exceptions]

Workflow:
  Apply domain model to input
  Flag where model is uncertain → escalate to user
  Output in domain-standard format
```

**Key rules:** Decision trees must be explicit (not "use best judgement"). Rubrics must have measurable criteria.
Freedom level: Low for rules and rubrics, High for prose explanations.

---

### Pattern 5: Multi-MCP Coordination

**Use for:** Slack + Linear + GitHub workflows, cross-service data pipelines, multi-API orchestration.

**Disqualifiers:**
- Task achievable with one MCP → use Domain Intelligence or Sequential instead
- MCPs don't share state → they're parallel tasks, not a coordination pattern

**Structure:**
```
Service Map:
  MCP A: [what it provides] → [output consumed by B]
  MCP B: [what it provides] → [output consumed by C]
  MCP C: [final output]

Coordination:
  Step 1: Call MCP A → capture [specific fields]
  Step 2: Transform A output for MCP B input
  Step 3: Call MCP B → capture [specific fields]
  ...

Error isolation:
  IF MCP X fails → [fallback or halt]
  Do NOT cascade failure silently
```

**Key rules:** Each MCP call isolated. Explicit error handling per service. State transformation between services documented.
Freedom level: Low for MCP call signatures, Medium for transformation logic.

---

## Hybrid Patterns

Valid hybrid combinations:
- Sequential + Domain Intelligence: steps follow fixed order, each step applies domain rules
- Context-Aware + Sequential: routing selects which sequential workflow to run
- Iterative + Domain Intelligence: domain rubric defines the quality threshold

Document hybrid choice in SKILL.md Gate 6 (Structure Design):
```
Pattern: Sequential + Domain Intelligence hybrid
Rationale: [why neither alone suffices]
```

Invalid hybrids: avoid combining >2 patterns — complexity exceeds Gate 3 thresholds.