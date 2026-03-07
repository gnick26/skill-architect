#!/usr/bin/env python3
"""
Skill Structure Validator v2
Validates SKILL.md against Agent Skills spec and best practices.

Updates from L2 research:
- description max: 1024 chars (L2-1: spec limit, 500 was compatibility field)
- name ≤64 chars (L2-1: spec limit)
- single-line YAML check (L2-3: multi-line breaks recognition entirely)
- XML tags in frontmatter (injection risk)
- forward slashes in name (path traversal)
- compatibility ≤500 chars (spec limit for that field)
"""

import sys
import re
from pathlib import Path


class SkillValidator:
    def __init__(self, skill_path: str):
        self.skill_path = Path(skill_path)
        self.errors = []
        self.warnings = []
        self.frontmatter_raw = ""
        self.body = ""

    def validate(self) -> bool:
        """Run all validations. Returns True if no errors."""
        self._load_content()
        self._validate_structure()
        self._validate_frontmatter()
        self._validate_name()
        self._validate_description()
        self._validate_compatibility()
        self._validate_body()
        self._validate_sections()
        return len(self.errors) == 0

    def _load_content(self):
        """Load and split SKILL.md into frontmatter and body."""
        skill_md = self.skill_path / "SKILL.md"
        if not skill_md.exists():
            return

        content = skill_md.read_text()
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                self.frontmatter_raw = parts[1]
                self.body = parts[2]

    def _validate_structure(self):
        """Check directory structure and SKILL.md existence."""
        skill_md = self.skill_path / "SKILL.md"
        if not skill_md.exists():
            self.errors.append("SKILL.md not found")
            return

        name = self.skill_path.name
        # Kebab-case check
        if not re.match(r'^[a-z][a-z0-9-]*$', name):
            self.errors.append(f"Directory name '{name}' must be kebab-case (lowercase, hyphens only)")

        # Forward slashes in name (path traversal risk)
        if '/' in name or '\\' in name:
            self.errors.append(f"Directory name '{name}' contains path separators")

    def _validate_frontmatter(self):
        """Validate YAML frontmatter format and security."""
        skill_md = self.skill_path / "SKILL.md"
        if not skill_md.exists():
            return

        content = skill_md.read_text()

        if not content.startswith('---'):
            self.errors.append("Missing YAML frontmatter (must start with ---)")
            return

        parts = content.split('---', 2)
        if len(parts) < 3:
            self.errors.append("Invalid frontmatter format (missing closing ---)")
            return

        fm = parts[1]

        # Required fields
        if 'name:' not in fm:
            self.warnings.append("Missing 'name' in frontmatter")
        if 'description:' not in fm:
            self.errors.append("Missing 'description' in frontmatter (REQUIRED)")

        # XML tags check — injection risk (L2-3)
        if re.search(r'<[a-zA-Z/][^>]*>', fm):
            self.errors.append("XML/HTML tags found in frontmatter (injection risk). Remove all <> tags.")

        # Single-line YAML check for description (L2-3, CRITICAL)
        desc_match = re.search(r'description:\s*([|>])', fm)
        if desc_match:
            self.errors.append(
                f"CRITICAL: Description uses multi-line YAML operator '{desc_match.group(1)}'. "
                "Multi-line descriptions break skill recognition entirely. Use single-line format."
            )

    def _validate_name(self):
        """Validate name field (L2-1: ≤64 chars, lowercase+hyphens)."""
        if not self.frontmatter_raw:
            return

        match = re.search(r'name:\s*(.+)', self.frontmatter_raw)
        if not match:
            return

        name = match.group(1).strip().strip('"\'')

        # Length check (L2-1: spec limit 64 chars)
        if len(name) > 64:
            self.errors.append(f"Name too long ({len(name)} chars). Spec max: 64")

        # Format check
        if not re.match(r'^[a-z][a-z0-9-]*$', name):
            self.errors.append(f"Name '{name}' must be lowercase with hyphens only (kebab-case)")

    def _validate_description(self):
        """Validate description field against spec and best practices."""
        if not self.frontmatter_raw:
            return

        # Extract single-line description value
        match = re.search(r'description:\s*(.+)', self.frontmatter_raw)
        if not match:
            return

        desc = match.group(1).strip().strip('"\'')

        # Length checks (L2-1: spec max 1024, target 130-250)
        if len(desc) < 50:
            self.errors.append(f"Description too short ({len(desc)} chars). Minimum: 50")
        if len(desc) > 1024:
            self.errors.append(f"Description exceeds spec limit ({len(desc)} chars). Max: 1024")
        elif len(desc) > 250:
            self.warnings.append(f"Description long ({len(desc)} chars). Target: 130-250 for optimal budget")

        # Trigger phrases
        if 'use when' not in desc.lower() and 'invoke' not in desc.lower():
            self.warnings.append("Description missing trigger phrases ('Use when...' or 'invoke...when')")

        # Negative triggers
        if 'not use' not in desc.lower() and "don't use" not in desc.lower() and 'do not' not in desc.lower():
            self.warnings.append("Description missing negative triggers (Do NOT use for...)")

        # Voice check — first word capitalized
        first_word = desc.split()[0] if desc else ""
        if first_word and first_word[0].islower():
            self.warnings.append("Description should start with capital letter")

        # Directive pattern check
        if not re.match(r'^ALWAYS\b', desc):
            self.warnings.append("Description does not use directive pattern (should start with 'ALWAYS')")

        # First 50 chars should contain trigger keyword
        first_50 = desc[:50].lower()
        generic_starts = ['this skill', 'a skill', 'the skill', 'proactive framework']
        for generic in generic_starts:
            if generic in first_50:
                self.warnings.append(
                    f"First 50 chars contain generic phrase '{generic}'. "
                    "Front-load with primary trigger keyword."
                )

    def _validate_compatibility(self):
        """Validate compatibility field if present (spec: ≤500 chars)."""
        if not self.frontmatter_raw:
            return

        match = re.search(r'compatibility:\s*(.+)', self.frontmatter_raw)
        if not match:
            return

        compat = match.group(1).strip().strip('"\'')
        if len(compat) > 500:
            self.errors.append(f"Compatibility field too long ({len(compat)} chars). Spec max: 500")

    def _validate_body(self):
        """Validate body size."""
        if not self.body:
            return

        lines = self.body.strip().split('\n')

        # Line count (spec: <500, target ≤250)
        if len(lines) > 500:
            self.errors.append(f"SKILL.md body too long ({len(lines)} lines). Spec max: 500")
        elif len(lines) > 250:
            self.warnings.append(f"SKILL.md body above target ({len(lines)} lines). Target: ≤250")

        # Word/token estimate (spec: <5000 tokens ≈ 3750 words)
        words = len(self.body.split())
        if words > 5000:
            self.errors.append(f"SKILL.md body too long ({words} words). Spec max: ~5000")
        elif words > 4000:
            self.warnings.append(f"SKILL.md body approaching limit ({words}/5000 words)")

    def _validate_sections(self):
        """Check for recommended sections."""
        if not self.body:
            return

        content_lower = self.body.lower()

        if '## when to use' not in content_lower and '# when to use' not in content_lower:
            self.warnings.append("Missing 'When to Use' section")
        if 'not to use' not in content_lower and 'when not' not in content_lower:
            self.warnings.append("Missing 'When NOT to Use' section")

    def report(self) -> str:
        """Generate validation report."""
        lines = []
        lines.append(f"Skill Validation: {self.skill_path.name}")
        lines.append("=" * 50)

        if self.errors:
            lines.append(f"\n  ERRORS ({len(self.errors)}):")
            for e in self.errors:
                lines.append(f"  - {e}")

        if self.warnings:
            lines.append(f"\n  WARNINGS ({len(self.warnings)}):")
            for w in self.warnings:
                lines.append(f"  - {w}")

        if not self.errors and not self.warnings:
            lines.append("\n  All validations passed!")

        lines.append("\n" + "=" * 50)
        status = "FAIL" if self.errors else "PASS"
        e_count = len(self.errors)
        w_count = len(self.warnings)
        lines.append(f"Status: {status} ({e_count} errors, {w_count} warnings)")

        return "\n".join(lines)


def main():
    if len(sys.argv) < 2:
        print("Usage: validate_skill.py <skill-directory>")
        print("  Validates SKILL.md in the given directory against Agent Skills spec.")
        sys.exit(1)

    skill_path = sys.argv[1]

    validator = SkillValidator(skill_path)
    is_valid = validator.validate()

    print(validator.report())

    sys.exit(0 if is_valid else 1)


if __name__ == "__main__":
    main()
