# Skill Sizing Rules

## Hard Limits (Spec-Verified)

| Component | Limit | Source |
|-----------|-------|--------|
| SKILL.md body | <500 lines (target ≤250) | Agent Skills spec |
| SKILL.md body | <5,000 tokens | Agent Skills spec |
| Description | max 1024 chars (target 130-250) | Agent Skills spec (NOT 500 — that's `compatibility`) |
| Name | ≤64 chars, lowercase + hyphens | Agent Skills spec |
| Compatibility field | ≤500 chars | Agent Skills spec |
| Metadata | ~100 tokens | Agent Skills spec (progressive disclosure Level 1) |
| Single reference file | ≤10k words | Best practice |
| Total skill loaded | ≤15k tokens | Best practice |

## Progressive Disclosure (Spec)

| Level | Content | Budget |
|-------|---------|--------|
| Level 1 (always loaded) | name + description from frontmatter | ~100 tokens |
| Level 2 (on trigger) | SKILL.md body | <5,000 tokens |
| Level 3 (on demand) | references/, scripts/, examples/ | Unlimited |

## Skills Budget

- **Budget:** 2% of context window, fallback 16,000 chars
- **Per-skill overhead:** ~109 chars XML wrapper + description length
- **Degradation threshold:** ~42 skills at avg 263 chars

| Avg Description | Skills Capacity |
|-----------------|----------------|
| 130 chars | ~67 skills |
| 200 chars | ~52 skills |
| 250 chars | ~42 skills |
| 300 chars | ~36 skills |

## Decomposition Triggers

Split skill when ANY threshold exceeded:

| Metric | Single OK | Split Required |
|--------|-----------|----------------|
| Decision branches | ≤5 | >5 |
| Files touched | ≤50 | >100 |
| Token volume | ≤20k | >50k |
| Tool types | ≤2 | >3 |
| Workflow steps | ≤7 | >10 |

## Optimal Ranges by Skill Type

| Skill Type | SKILL.md Lines | References | Scripts |
|------------|----------------|------------|---------|
| Minimal | 50-100 | 0 | 0 |
| Standard | 150-250 | 1-2 | 0-1 |
| Complex | 250-400 | 3-5 | 1-2 |
| Orchestrator | 200-300 | 2-3 | 1 |

## When to Use What

```
Simple procedure (<50 lines)      → Slash command, not skill
Repeatable workflow (50-250 lines) → Standard skill
Domain expertise (250-400 lines)   → Skill + references/
Multi-phase complex (>400 lines)   → Decompose into skill swarm
External integration               → MCP server, not skill
Autonomous execution               → Agent (Task tool), not skill
```

## Cognitive Load Thresholds [unverified]

Performance may degrade at:
- ~3,000 tokens: reasoning quality starts declining
- ~500 lines SKILL.md: attention decay observed
- Middle of long documents: lost-in-middle effect

These are observed patterns, not spec-confirmed thresholds.

## Optional Directories (Spec-Defined)

| Directory | Purpose | Loading |
|-----------|---------|---------|
| `references/` | Detailed documentation | On-demand by agent |
| `scripts/` | Executable code, self-contained | On-demand |
| `assets/` | Static resources (templates, images, data) | Not loaded into context |
