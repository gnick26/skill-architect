# Degrees of Freedom Framework

Match instruction specificity to task fragility. The more dangerous a deviation, the more prescriptive the instructions must be.

## Freedom Levels

| Level | Instruction Type | When to Use | Risk Profile |
|-------|-----------------|-------------|--------------|
| **High** | Text-based heuristics, general guidance | Multiple valid approaches, context-dependent. Example: code review style | Low — many paths to success |
| **Medium** | Pseudocode, scripts with parameters | Preferred pattern exists but variation acceptable. Example: report generation | Medium — some paths are better |
| **Low** | Exact commands, no modification allowed | Fragile operations, consistency critical. Example: DB migrations, deployments | High — only one safe path |

## Calibration Test

Ask: "If Claude deviates from these instructions, what's the worst that happens?"

| Answer | Freedom Level | Instruction Style |
|--------|--------------|-------------------|
| "Slightly different style" | High | Heuristics, guidelines |
| "Wrong format but recoverable" | Medium | Pseudocode, templates |
| "Data loss or security breach" | Low | Exact scripts, no deviation |

## Application to Skill Sections

| Skill Section | Typical Freedom | Rationale |
|---------------|----------------|-----------|
| Trigger description | Low | Must match precisely or skill is invisible |
| Workflow overview | Medium | Structure matters, details flexible |
| Domain heuristics | High | Context-dependent decisions |
| Validation scripts | Low | Deterministic checks, exact commands |
| Error recovery | Medium | Known patterns with variation |

## Examples

### High Freedom (code review skill)
```
Review for: readability, maintainability, potential bugs.
Flag patterns that increase complexity unnecessarily.
```

### Medium Freedom (report generation)
```
Generate report with sections: Summary, Findings, Recommendations.
Use markdown tables for data. Include severity ratings (High/Medium/Low).
```

### Low Freedom (database migration)
```bash
# Execute exactly as written. No modifications.
pg_dump -Fc myproject > backup_$(date +%Y%m%d).dump
psql -c "ALTER TABLE users ADD COLUMN email_verified BOOLEAN DEFAULT FALSE;"
```

## Anti-Pattern: Freedom Mismatch

| Mismatch | Symptom | Fix |
|----------|---------|-----|
| Low freedom on flexible task | Claude fights instructions, produces stilted output | Relax to heuristics |
| High freedom on fragile task | Inconsistent results, occasional data issues | Tighten to exact scripts |
