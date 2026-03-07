# Example: Well-Designed Skill

Demonstrates all v2 best practices including directive description pattern.

```yaml
---
name: code-review-security
description: ALWAYS invoke for security-focused code review when reviewing PRs for vulnerabilities, auditing OWASP compliance, or preparing for penetration tests. Do NOT perform ad-hoc security checks directly -- use this skill first.
allowed-tools: Read, Grep, Glob
---

# Security Code Review

## When to Use
- Reviewing pull requests with security implications
- Auditing code for vulnerabilities
- Preparing for penetration tests
- Post-incident code analysis

## When NOT to Use
- General code style review (use code-review skill)
- Performance optimization (use perf-analysis skill)
- Simple typo fixes

## Workflow

### Phase 1: Reconnaissance
Identify attack surface:
1. List all user input points (forms, APIs, file uploads)
2. Map data flow from input to storage/output
3. Identify authentication/authorization checkpoints

Checkpoint:
- [ ] Input vectors documented
- [ ] Data flow mapped

### Phase 2: OWASP Top 10 Scan
Check each category:

| Category | Check | Tools |
|----------|-------|-------|
| Injection | SQL, Command, LDAP | Grep for string concat in queries |
| Broken Auth | Session handling | Review auth middleware |
| XSS | Output encoding | Check template escaping |
| IDOR | Access controls | Review permission checks |
| Security Misconfig | Defaults, headers | Check config files |

For each finding:
IF vulnerability found →
  Severity: Critical/High/Medium/Low
  Location: file:line
  Recommendation: specific fix

### Phase 3: Report Generation
Output format:

## Security Review Summary

**Files Reviewed:** {count}
**Vulnerabilities Found:** {count}

### Critical
- [{file}:{line}] {description} - {recommendation}

### High
- [{file}:{line}] {description} - {recommendation}

### Medium/Low
- [{file}:{line}] {description} - {recommendation}

## Validation

Before completing:
- [ ] All OWASP categories checked
- [ ] Each finding has severity + recommendation
- [ ] No false positives (verified exploitable)
- [ ] Report follows standard format

## References

See references/owasp-checklist.md for detailed category guidance
```

## Why This Skill Works (v2 Checklist)

1. **Directive description:** "ALWAYS invoke... Do NOT... directly -- use this skill first."
2. **Single-line YAML:** no `|` or `>` — skill is visible
3. **Length:** 207 chars — within 130-250 target
4. **First 50 chars:** "ALWAYS invoke for security-focused code review whe" — trigger keyword present
5. **Third person:** implied by directive pattern
6. **WHAT + WHEN:** security review + when reviewing PRs/auditing/preparing
7. **Anti-definition:** "Do NOT perform ad-hoc security checks directly"
8. **Scope:** Single job-to-be-done (security review)
9. **Structure:** Clear phases with checkpoints
10. **Size:** ~90 lines body — well within limits
