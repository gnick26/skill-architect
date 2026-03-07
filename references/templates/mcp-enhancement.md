# MCP Enhancement Template

Use for adding domain expertise on top of MCP tool access.

```yaml
---
name: {service}-{capability}
description: ALWAYS invoke for intelligent {MCP service} usage when {trigger1}, {trigger2}, or {trigger3}. Do NOT call {service} tools directly for {complex scenario} -- use this skill first.
allowed-tools: Read, Write, Bash
---

# {Service} {Capability} Guide

## When to Use
- {User wants intelligent use of service}
- {User needs guidance on best approach}
- {User asks about {domain} with {service}}

## When NOT to Use
- Simple {service} queries (use MCP directly)
- {Out of scope scenario}

## Service Context

**MCP Server:** {server-name}
**Key Tools:**
- `{tool_1}`: {what it does}
- `{tool_2}`: {what it does}
- `{tool_3}`: {what it does}

## Decision Logic

### When to Use Which Tool

User intent: {intent type 1}
→ Tool: {tool_1}
→ Parameters: {key params}
→ Post-processing: {what to do with result}

User intent: {intent type 2}
→ Tool: {tool_2}
→ Parameters: {key params}
→ Post-processing: {what to do with result}

## Workflow Patterns

### Pattern 1: {Common workflow}
1. Call `{tool_1}` to {purpose}
2. Analyze result for {criteria}
3. Call `{tool_2}` with {derived params}
4. Format output as {format}

## Error Handling

| Error | Cause | Resolution |
|-------|-------|------------|
| `{error_code}` | {Why it happens} | {What to do} |

## Validation

Before completing:
- [ ] Correct tool selected for intent
- [ ] Parameters properly formatted
- [ ] Error handling applied
- [ ] Output matches expected format
```

## When to Use This Template

- GitHub workflows with expertise
- Database queries with domain knowledge
- API integrations with business logic
- Any MCP server + decision expertise

## Key Principle

Skills teach WHAT to do with tools.
MCP servers provide HOW to access tools.
Combine for intelligent automation.
