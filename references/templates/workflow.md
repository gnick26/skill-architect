# Workflow Automation Template

Use for multi-step processes with validation gates.

```yaml
---
name: {workflow-name}
description: ALWAYS invoke for {workflow type} when {trigger1}, {trigger2}, or {trigger3}. Do NOT execute {alternative} directly -- use this skill first.
allowed-tools: {minimal required set}
---

# {Workflow Name}

## When to Use
- {Scenario 1}
- {Scenario 2}
- {Scenario 3}

## When NOT to Use
- {Out of scope 1}
- {Out of scope 2}

## Workflow Phases

### Phase 1: {Name} (Preparation)
**Objective:** {What this phase accomplishes}

Steps:
1. {Action}
2. {Action}

Checkpoint:
- [ ] {Verification criterion}
- [ ] {Verification criterion}

IF checkpoint fails → {Recovery action}

### Phase 2: {Name} (Execution)
**Objective:** {What this phase accomplishes}

Steps:
1. {Action}
2. {Action}

Checkpoint:
- [ ] {Verification criterion}

### Phase 3: {Name} (Validation)
**Objective:** {What this phase accomplishes}

Steps:
1. {Action}
2. {Action}

Final validation:
- [ ] {Success criterion 1}
- [ ] {Success criterion 2}
- [ ] {Success criterion 3}

## Decision Points

IF {condition A} → Execute {path A}
ELSE IF {condition B} → Execute {path B}
ELSE → {Default path}

## Error Handling

| Error | Cause | Resolution |
|-------|-------|------------|
| {Error 1} | {Why} | {Fix} |
| {Error 2} | {Why} | {Fix} |

## References

See references/{detail}.md for {expanded guidance}
```

## When to Use This Template

- Multi-phase processes
- Requires validation between steps
- 3-7 distinct phases
- 150-300 lines typical
