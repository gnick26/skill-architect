# Skills Tools Ecosystem

External tools for validating, testing, and scanning skills.

## 1. Cisco AI Defense skill-scanner

**Purpose:** Security scanning of Agent Skills packages.
**License:** Apache 2.0
**Version:** 1.0.2 (CVE-2026-26057 fixed)
**Install:** `pip install cisco-ai-skill-scanner`

### CLI Quick Reference

```bash
# Scan single skill (recommended flags for Gate 0i):
skill-scanner scan <path> --use-behavioral --use-trigger --yara-mode strict --fail-on-findings --format json

# Scan all skills with overlap detection:
skill-scanner scan-all <path> --recursive --check-overlap --format markdown -o report.md

# List available analyzers:
skill-scanner list-analyzers

# Validate custom YARA rules:
skill-scanner validate-rules
```

### Key Flags

| Flag | Purpose |
|------|---------|
| `--use-behavioral` | AST dataflow + taint tracking (Python) |
| `--use-trigger` | Description specificity analysis |
| `--use-llm` | LLM semantic analysis (needs API key) |
| `--use-virustotal` | Hash-based malware scan (needs VT key) |
| `--enable-meta` | 2nd-pass FP filtering (needs 2+ analyzers + LLM) |
| `--yara-mode {strict,balanced,permissive}` | YARA sensitivity |
| `--fail-on-findings` | Non-zero exit on HIGH/CRITICAL |
| `--format {summary,json,markdown,table,sarif}` | Output format |
| `--check-overlap` | (scan-all only) Description overlap detection |

### Cost

~$0.01-0.05 per scan with LLM analyzer enabled.

## 2. cc-plugin-eval

**Purpose:** Automated triggering accuracy measurement.
**Source:** github.com/sjnims/cc-plugin-eval
**Note:** Measures triggering, NOT task completion quality.

### 4-Stage Pipeline

| Stage | Purpose | Model |
|-------|---------|-------|
| 1. Analysis | Parse SKILL.md, extract triggers | Deterministic |
| 2. Generation | Create test scenarios (5/component) | Sonnet 4.5 |
| 3. Execution | Run against Claude Agent SDK | Sonnet 4.5 |
| 4. Evaluation | Calculate triggering metrics | Haiku 4.5 |

### Output Metrics

```json
{
  "metrics": {
    "total_scenarios": 25,
    "accuracy": 0.92,
    "trigger_rate": 0.88,
    "avg_quality": 8.7,
    "conflict_count": 1
  }
}
```

### Scenario Types

Direct, Paraphrased, Edge case, Negative, Semantic

### Limitations

- Budget: max $10 USD per eval
- Disallowed tools during eval: Write, Edit, Bash (safety)
- Measures triggering accuracy only, NOT whether skill produces correct output

## 3. SkillCheck

**Purpose:** Structural validator and quality linter.
**Source:** getskillcheck.com
**Tiers:** Free + Pro

### What It Checks

- Structure validation (file naming, directory layout)
- Naming conventions (kebab-case, length)
- Semantics validation (description quality)
- Anti-slop patterns (filler detection)
- Security checks (hardcoded secrets, injection)
- WCAG compliance
- Token budget estimation

### Output

Quality score (e.g., "92/100 Anti-slop").
This is a structural linter — NOT an eval framework.

## 4. init_skill.py

**Purpose:** Scaffold new skill directory with SKILL.md template and example directories.
**Location:** scripts/init_skill.py (in this skill)
**Usage:**
```bash
python scripts/init_skill.py <skill-name> --path <output-directory>
```
**Creates:** skill directory, SKILL.md template with frontmatter placeholders, empty scripts/, references/, assets/
**Use at:** Gate 8 (content generation) — run before writing SKILL.md manually.

## 5. package_skill.py

**Purpose:** Package skill into distributable .skill zip file with pre-validation.
**Location:** scripts/package_skill.py (in this skill)
**Usage:**
```bash
python scripts/package_skill.py <path/to/skill-folder> [output-directory]
```
**Validates:** YAML frontmatter, naming conventions, directory structure, description completeness.
**Excludes:** `__pycache__`, `*.pyc`, `.DS_Store`, `evals/` directory.
**Use at:** After Gate 9 — when skill passes all validation and is delivery-ready.

## Integration in skill-architect

| Tool | Gate | Use |
|------|------|-----|
| skill-scanner | Gate 0i (Import) | Security scan of external skills |
| skill-scanner scan-all | Gate 9 / Post-deploy | Overlap detection in collection |
| cc-plugin-eval | Gate 9c | Automated trigger rate measurement |
| SkillCheck | Gate 9a | Structural quality validation |
| init_skill.py | Gate 8 | Scaffold new skill directory |
| package_skill.py | Post Gate 9 | Package for distribution |