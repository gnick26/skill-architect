# Gate 0i: Import Security Assessment

Security scan workflow for externally-sourced skills using Cisco AI Defense skill-scanner.

## Prerequisites

- skill-scanner v1.0.2+ installed (CVE-2026-26057 fixed in v1.0.2)
- Server: `export PYTHONPATH=$HOME/.local/lib/python3.10/site-packages`

## Step 1: Run Security Scan

```bash
skill-scanner scan <path> \
  --use-behavioral \
  --use-trigger \
  --yara-mode strict \
  --fail-on-findings \
  --format json
```

## Step 2: Interpret Results

### Exit Code Decision Matrix

| Exit Code | Max Severity | Decision | Action |
|-----------|-------------|----------|--------|
| 0 (clean) | SAFE | **PASS** | Proceed to quality eval (Mode B) |
| 0 (findings) | LOW | **PASS with note** | Log findings, proceed to Mode B |
| ≠0 | MEDIUM | **WARNING** | Show findings to user, user decides |
| ≠0 | HIGH | **BLOCK** | Reject import. Manual audit required |
| ≠0 | CRITICAL | **BLOCK** | Reject import. Do not deploy |

### Threat Category Overrides

These categories trigger BLOCK regardless of severity level:

| AITech Category | Code | Rationale |
|----------------|------|-----------|
| Prompt Injection | AITech-1.1, 1.2 | Direct threat to agent integrity |
| Code Injection | AITech-9.1.4 | Arbitrary code execution |
| Data Exfiltration | AITech-8.2 | Data leakage |
| Hardcoded Secrets | AITech-8.2 | Credential compromise |
| Tool Chaining | AITech-8.2.3 | Multi-step exfiltration |
| Obfuscation | — | Intentional concealment = zero trust |

These categories trigger WARNING (escalate to BLOCK on HIGH+):

| AITech Category | Code | Rationale |
|----------------|------|-----------|
| Tool/Permission Abuse | AITech-12.1 | Config review needed |
| Autonomy Abuse | AITech-13.1 | Excessive autonomy |
| Capability Inflation | AITech-4.3 | Trigger hijacking risk |
| Resource Abuse | AITech-13.1 | Monitor on deploy |

## 7 Analyzers Reference

| # | Analyzer | Method | Scope | Requirements |
|---|----------|--------|-------|-------------|
| 1 | **static** | YAML + YARA (80+ patterns) | All files | None (default) |
| 2 | **behavioral** | AST dataflow + taint tracking | Python files | `--use-behavioral` |
| 3 | **trigger** | Description specificity analysis | SKILL.md | `--use-trigger` |
| 4 | **llm** | LLM-as-judge semantic analysis | SKILL.md + scripts | `--use-llm` + API key |
| 5 | **virustotal** | Hash-based malware detection | Binary files | `--use-virustotal` + VT key |
| 6 | **aidefense** | Cisco AI Defense cloud API | Prompts, code, markdown | `--use-aidefense` + key |
| 7 | **meta** | 2nd-pass LLM: FP filtering | All findings | `--enable-meta` + 2 analyzers + LLM |

## Step 3: Output

```
IF BLOCK:
  "⛔ Import BLOCKED: {severity} findings detected.
   Category: {threat_category}
   Details: {finding_summary}
   Action: Do not deploy. Manual security audit required."

IF WARNING:
  "⚠️ Import WARNING: {count} MEDIUM findings detected.
   {finding_list}
   Decision: Deploy with monitoring? [Y/N]"

IF PASS:
  "✅ Security scan clean. Proceeding to quality evaluation (Mode B)."
  → Run Mode B (references/evaluate-refine.md)
```

## Ecosystem Overlap Check (Post-Import)

After importing, check for description conflicts with existing skills:

```bash
skill-scanner scan-all ~/.claude/skills/ --recursive --check-overlap --format markdown -o scan-report.md
```
