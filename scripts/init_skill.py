#!/usr/bin/env python3
"""
Skill Initializer - Creates a new skill directory with SKILL.md template and structure.

Usage:
    python scripts/init_skill.py <skill-name> [--path <output-directory>]

Examples:
    python scripts/init_skill.py my-skill
    python scripts/init_skill.py my-skill --path ~/.claude/skills/
"""

import sys
import re
import argparse
from pathlib import Path

SKILL_MD_TEMPLATE = """---
name: {name}
description: ALWAYS invoke for [TODO: what this skill does] when [TODO: trigger condition 1], [TODO: trigger condition 2]. Do NOT [TODO: alternative action] directly -- use this skill first.
---

# [TODO: Skill Title]

## When to Use
- [TODO: scenario 1]
- [TODO: scenario 2]

## When NOT to Use
- [TODO: out of scope 1]
- [TODO: out of scope 2]

## Workflow

### Phase 1: [TODO: Phase Name]
[TODO: what this phase accomplishes]

Steps:
1. [TODO: action]
2. [TODO: action]

Checkpoint:
- [ ] [TODO: verification criterion]
- [ ] [TODO: verification criterion]

IF checkpoint fails → [TODO: recovery action]

### Phase 2: [TODO: Phase Name]
[TODO: what this phase accomplishes]

Steps:
1. [TODO: action]
2. [TODO: action]

Checkpoint:
- [ ] [TODO: verification criterion]

## Decision Points

IF [TODO: condition A] → [TODO: path A]
ELSE IF [TODO: condition B] → [TODO: path B]
ELSE → [TODO: default path]

## References

[TODO: link to reference files if needed]
See references/[TODO].md for [TODO: what it contains]
"""

REFERENCES_PLACEHOLDER = """# [TODO: Reference Title]

Detailed documentation for [TODO: topic].

## Section 1

[TODO: content]

## Section 2

[TODO: content]
"""

ASSETS_PLACEHOLDER = """# assets/

Place static files here (templates, images, fonts, boilerplate code).
These files are NOT loaded into context — they are used in skill output.

Examples:
- report-template.md
- logo.png
- boilerplate/

Delete this README when you add real assets.
"""


def validate_name(name: str) -> bool:
    """Validate skill name: lowercase, hyphens only, no start/end hyphens."""
    pattern = r'^[a-z]([a-z0-9-]*[a-z0-9])?$'
    return bool(re.match(pattern, name)) and '--' not in name


def init_skill(skill_name: str, output_dir: str = None) -> Path:
    """
    Initialize a new skill directory with template files.

    Args:
        skill_name: Name of the skill (kebab-case)
        output_dir: Directory to create skill in (defaults to current directory)

    Returns:
        Path to created skill directory, or None on error
    """
    if not validate_name(skill_name):
        print(f"Error: '{skill_name}' is not a valid skill name.")
        print("  Requirements: lowercase, hyphens only, no start/end hyphens, no double hyphens")
        print("  Example: my-skill, code-review, odoo-dev")
        return None

    if len(skill_name) > 64:
        print(f"Error: skill name must be ≤64 chars (got {len(skill_name)})")
        return None

    base_dir = Path(output_dir).resolve() if output_dir else Path.cwd()
    skill_dir = base_dir / skill_name

    if skill_dir.exists():
        print(f"Error: '{skill_dir}' already exists. Choose a different name or path.")
        return None

    # Create directory structure
    (skill_dir / "references").mkdir(parents=True)
    (skill_dir / "scripts").mkdir()
    (skill_dir / "examples").mkdir()
    (skill_dir / "assets").mkdir()

    # Write SKILL.md
    skill_md = skill_dir / "SKILL.md"
    skill_md.write_text(SKILL_MD_TEMPLATE.format(name=skill_name))
    print(f"  Created: {skill_md.relative_to(base_dir)}")

    # Write placeholder files
    ref_placeholder = skill_dir / "references" / "README.md"
    ref_placeholder.write_text(REFERENCES_PLACEHOLDER)
    print(f"  Created: {ref_placeholder.relative_to(base_dir)}")

    assets_readme = skill_dir / "assets" / "README.md"
    assets_readme.write_text(ASSETS_PLACEHOLDER)
    print(f"  Created: {assets_readme.relative_to(base_dir)}")

    print(f"\nSkill '{skill_name}' initialized at: {skill_dir}")
    print("\nNext steps:")
    print("  1. Edit SKILL.md — fill in all [TODO] sections")
    print("  2. Add reference files to references/ as needed")
    print("  3. Add scripts to scripts/ if deterministic code is needed")
    print("  4. Delete placeholder files in assets/ and references/ if unused")
    print("  5. Run: python scripts/validate_skill.py " + str(skill_dir))

    return skill_dir


def main():
    parser = argparse.ArgumentParser(
        description="Initialize a new Agent Skill directory with template files."
    )
    parser.add_argument("skill_name", help="Skill name (kebab-case, e.g. my-skill)")
    parser.add_argument(
        "--path",
        default=None,
        help="Output directory (default: current directory)"
    )
    args = parser.parse_args()

    result = init_skill(args.skill_name, args.path)
    sys.exit(0 if result else 1)


if __name__ == "__main__":
    main()