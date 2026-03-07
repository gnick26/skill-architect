# Activation Hooks

Hooks can boost trigger rates — but ONLY when combined with strong descriptions.

## Key Finding

**Hooks HURT with weak descriptions.** Logistic regression: hooks coefficient -2.35, p<0.0001 (Seleznov, 650 trials).
Directive description alone (97-100%) outperforms hooks + weak description (37%).

**Rule: Fix description FIRST, add hooks ONLY if still needed.**

## Baseline Trigger Rates by Model (Without Hooks)

| Model | Passive Description | Directive Description | Source |
|-------|--------------------|-----------------------|--------|
| Haiku 4.5 | ~20% | Not tested | Spence |
| Sonnet 4.5 | 50-55% | Not tested | Spence |
| Opus 4.5 | ~77% | 97-100% | Seleznov |

## Hook Types and Effectiveness

| Method | Rate (Haiku) | Rate (Sonnet) | Rate (Opus) | Notes |
|--------|-------------|---------------|-------------|-------|
| No hook, passive desc | ~20% | 50-55% | ~77% | Baseline |
| No hook, directive desc | — | — | 97-100% | Best without hooks |
| Forced-eval hook | 84% | 100% | — | Adds ~200-500 tokens/message |
| LLM-eval hook | 80% | 100% | — | Risk: hallucinated skill names |
| **Hooks + weak desc** | — | — | **37%** | **WORSE than no hooks** |

## Forced-Eval Hook Pattern

The most effective hook forces Claude to evaluate ALL skills before responding.

```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "type": "command",
        "command": "echo 'SKILL EVALUATION REQUIRED: Before responding, check all available skills against this query. List each skill with YES/NO and reason. Use matching skill if YES.'"
      }
    ]
  }
}
```

### Trade-offs

| Pro | Con |
|-----|-----|
| Near-100% trigger accuracy | +200-500 tokens per message |
| Catches skills user forgot about | Slight latency increase |
| Works on weaker models (Haiku) | Overhead on trivial queries |

## When to Use Hooks

```
IF directive description achieves ≥90% trigger rate → Skip hooks
IF skill is critical (security, compliance) AND rate <90% → Add forced-eval hook
IF skill targets Haiku/Sonnet AND rate <80% → Add forced-eval hook
IF skill is nice-to-have → Skip hook, rely on description
```

## Zero-Effect Approaches

- `keywords` frontmatter field: **0 effect** on trigger rate (Seleznov)
- CLAUDE.md reference alone: only +15pp (50%→65%) — insufficient (Seleznov)
- Adding more hooks without fixing description: counterproductive

## Diagnostic: Why Skills Get Ignored

| Cause | Signal | Fix |
|-------|--------|-----|
| Weak description | <50% trigger rate | Rewrite with directive pattern |
| Multi-line YAML | 0% trigger rate | Convert to single-line |
| Too many skills loaded | Declining rates over time | Consolidate or `disable-model-invocation` |
| Conflicting descriptions | Wrong skill triggers | Sharpen anti-definitions, `scan-all --check-overlap` |
| Claude prefers base knowledge | Correct answer but no skill structure | Add hook or strengthen description |
