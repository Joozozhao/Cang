#!/usr/bin/env python3
"""Small, dependency-free consistency check for the cang-skill package."""
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
required = [
    ROOT / "SKILL.md",
    ROOT / "README.md",
    ROOT / "agents/openai.yaml",
    *(ROOT / "references").glob("*.md"),
]
errors = []
for path in required:
    if not path.exists():
        errors.append(f"missing: {path.relative_to(ROOT)}")

skill = (ROOT / "SKILL.md").read_text(encoding="utf-8") if (ROOT / "SKILL.md").exists() else ""
if not skill.startswith("---\n") or "name: cang-skill" not in skill.split("---", 2)[1]:
    errors.append("SKILL.md has invalid or missing frontmatter")

for ref in re.findall(r"`(references/[^`]+\.md)`", skill):
    if not (ROOT / ref).exists():
        errors.append(f"broken reference: {ref}")

readme = (ROOT / "README.md").read_text(encoding="utf-8") if (ROOT / "README.md").exists() else ""
if "assets/<article-slug>/00-cover.png" not in skill or "assets/<article-slug>/00-cover.png" not in readme:
    errors.append("cover output path is not synchronized")
if "必须提供 `assets/avatar-reference.jpg`" in skill or "必须提供 `assets/avatar-reference.jpg`" in readme:
    errors.append("cover flow still requires a non-existent avatar reference")

if errors:
    print("cang-skill validation failed")
    print("\n".join(f"- {e}" for e in errors))
    sys.exit(1)
print("cang-skill package is valid")
