# Claude Code Extensions to Agent Skills Spec

Claude Code supports the base Agent Skills specification plus additional frontmatter fields not in the spec.

## Base Spec Fields (agentskills.io)

| Field | Required | Constraint |
|-------|----------|-----------|
| `name` | Yes (spec) / Optional (Claude Code fallback: dirname) | 1-64 chars, lowercase + hyphens, no start/end hyphens, must match dirname |
| `description` | Yes (spec) / Optional (Claude Code fallback: first paragraph) | Max 1024 chars |
| `license` | No | License identifier |
| `compatibility` | No | Max 500 chars (often confused with description limit) |
| `metadata` | No | Key-value pairs |
| `allowed-tools` | No (experimental) | Tool access restrictions |

## Claude Code Extension Fields

| Field | Type | Purpose | Example |
|-------|------|---------|---------|
| `disable-model-invocation` | boolean | Removes description from auto-selection budget | `disable-model-invocation: true` |
| `user-invocable` | boolean | Visibility in `/` slash command menu | `user-invocable: true` |
| `argument-hint` | string | Placeholder text shown in `/` menu | `argument-hint: [topic]` |
| `context` | string | Execution isolation | `context: fork` |
| `agent` | string | Subagent type for forked context | `agent: Bash` |
| `model` | string | Execution model override | `model: haiku` |
| `hooks` | object | Lifecycle hooks | See hooks section |

## When to Use Each Extension

### `disable-model-invocation: true`
- Skill is only useful via explicit `/command`
- Saves description budget (2% context / 16K chars)
- Example: `/resume`, `/preflight` — user always invokes explicitly

### `context: fork`
- Skill needs isolated execution (no main context pollution)
- Skill has >3 reference files (heavy context load)
- Skill runs risky operations (sandboxing)
- Combined with `agent` field for subagent type

### `argument-hint`
- Skill accepts arguments from `/` menu
- Shows user what to type after slash command
- Example: `argument-hint: [server] [tool] [json-args]`

### `model`
- Skill needs specific model capabilities
- Cost optimization (haiku for simple tasks)
- Example: `model: opus` for complex reasoning

## Spec vs Implementation Differences

| Aspect | Agent Skills Spec | Claude Code |
|--------|------------------|-------------|
| `name` required | Yes | No (fallback: dirname) |
| `description` required | Yes | No (fallback: first paragraph) |
| Discovery | Explicit registration | Auto-scan `.claude/skills/` |
| Legacy support | N/A | `.claude/commands/*.md` also works |
| Progressive disclosure | Spec-defined pattern | Supported via references/ |

## Compatibility Note

27+ agents support Agent Skills spec. Extension fields are Claude Code-specific and will be ignored by other agents (Cursor, Codex, Gemini CLI, etc.). Keep base spec fields for cross-agent compatibility.
