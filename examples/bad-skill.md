# Example: Poorly-Designed Skills

Real anti-patterns found in production skills (from Phase 0.5 audit + synthetic examples).

---

## Anti-Pattern 1: Multi-Line YAML (CRITICAL — invisible skill)

```yaml
---
name: team-manager
description: |
  Analyze and optimize multi-agent architecture. ALWAYS activate when
  discussing roles, agents, skills for project vault. Triggers: "role",
  "agent", etc. Keeps roles-registry.md updated after any role discussion.
---
```

**Problem:** The `|` makes description multi-line. Skill is **completely invisible** to Claude's auto-selection.
**Fix:** Single line, no `|`:
```yaml
description: ALWAYS invoke for multi-agent architecture when discussing roles, agents, or skills for project vault. Do NOT add roles or modify agent structure directly -- use this skill first.
```

---

## Anti-Pattern 2: Generic First 50 Characters

```yaml
description: Proactive skill creation framework enforcing evidence-based architecture. Use when user requests "create skill"...
```

**Problem:** First 50 chars = "Proactive skill creation framework enforcing evid" — no trigger keyword. Budget truncation reads left-to-right.
**Fix:** Front-load trigger keyword:
```yaml
description: ALWAYS invoke for skill creation when user requests "create skill", "build skill", or "design skill"...
```

---

## Anti-Pattern 3: Implementation Details in Description

```yaml
description: Execute MCP server tools via mcp-cli without loading tool definitions into context. Use when user mentions "todoist"...
```

**Problem:** "via mcp-cli without loading tool definitions into context" wastes 55 chars of description budget on implementation details irrelevant to routing.
**Fix:** Remove implementation details:
```yaml
description: ALWAYS invoke for MCP tool execution when user mentions "todoist", "tasks", "perplexity", "search the web". Do NOT call MCP tools directly -- use this skill first.
```

---

## Anti-Pattern 4: Provenance in Description

```yaml
description: Build knowledge graph for project vault. Route daily → decisions/hypotheses... Fork of community graph-builder adapted for project architecture.
```

**Problem:** "Fork of community graph-builder adapted for project architecture" wastes 60 chars on history.
**Fix:** Remove provenance, add anti-definition:
```yaml
description: ALWAYS invoke for vault knowledge graph operations when routing daily content, classifying decisions, or linking MOCs. Do NOT route or classify vault content directly -- use this skill first.
```

---

## Anti-Pattern 5: Imperative Voice

```yaml
description: Execute MCP server tools...
description: Load previous session context...
description: Conduct structured interview...
```

**Problem:** "Execute", "Load", "Conduct" are imperatives. Spec recommends third person.
**Fix:** Use third person or directive pattern:
```yaml
description: ALWAYS invoke for MCP tool execution when...
description: Loads previous session context. ALWAYS invoke when user types /resume...
description: Conducts structured interview. ALWAYS invoke when user mentions @teammate-a or @teammate-b...
```

---

## Anti-Pattern 6: The Vague Helper (synthetic)

```yaml
---
name: helper
description: Helps with various tasks.
---

# Helper Skill

You should use this skill when you need help with things...
```

**Problems (8 total):**
1. Vague description — no trigger precision
2. Kitchen sink scope — combines unrelated tasks
3. Second person voice — "You should use..."
4. Redundant instructions — "Be thorough and careful"
5. No checkpoints or validation
6. No decision logic
7. No "When NOT to Use"
8. Would exceed 500 lines

**Result:** ~20% trigger rate. Effectively the same as having no skill at all.

---

## Summary: What Each Anti-Pattern Costs

| Anti-Pattern | Trigger Rate Impact | Budget Impact |
|-------------|-------------------|---------------|
| Multi-line YAML | **0%** (invisible) | N/A |
| Generic first 50 chars | -20-40% | Keywords hidden |
| Implementation details | None | -55 chars wasted |
| Provenance | None | -60 chars wasted |
| Imperative voice | -5-10% | None |
| Vague helper | **~20%** baseline | None |
| Hooks + weak description | **37%** (worse than no hooks) | +200-500 tokens/msg |
