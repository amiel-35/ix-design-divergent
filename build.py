#!/usr/bin/env python3
"""
build.py: sync the skill into the dist/ plugin layout.

The repo root is the skill itself (SKILL.md, docs/, local.example.md), so that
`git clone` into ~/.claude/skills/design-divergent works as is. The plugin
needs it one level down, in dist/skills/design-divergent/. This script wipes
that folder and copies it fresh, so a file removed at the root does not
linger in dist/.

Usage:
    python3 build.py           # rebuild dist/, then check it
    python3 build.py --check   # check only: fails if dist/ is stale
"""

import filecmp
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DIST = ROOT / "dist"
DIST_SKILL = DIST / "skills" / "design-divergent"
# Ce qui part dans le plugin installé. local.md n'y va jamais (réglages perso).
SKILL_FILES = ("SKILL.md", "local.example.md")
SKILL_DIRS = ("docs",)  # sans docs/assets : la bannière ne sert qu'au README
LEGAL_FILES = ("LICENSE",)

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def build() -> None:
    if DIST_SKILL.exists():
        shutil.rmtree(DIST_SKILL)
    DIST_SKILL.mkdir(parents=True)
    for name in SKILL_FILES:
        shutil.copy2(ROOT / name, DIST_SKILL / name)
    for name in SKILL_DIRS:
        shutil.copytree(ROOT / name, DIST_SKILL / name, ignore=shutil.ignore_patterns(".DS_Store", "assets"))
    for name in LEGAL_FILES:
        shutil.copy2(ROOT / name, DIST / name)


def same_tree(a: Path, b: Path) -> bool:
    cmp = filecmp.dircmp(a, b, ignore=[".DS_Store", "assets"])
    if cmp.left_only or cmp.right_only or cmp.diff_files or cmp.funny_files:
        return False
    return all(same_tree(a / d, b / d) for d in cmp.common_dirs)


def check() -> list[str]:
    errors = []
    text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(text)
    if not m or not re.search(r"^name:\s*design-divergent\s*$", m.group(1), re.M):
        errors.append("SKILL.md: frontmatter missing or name is not design-divergent")
    for name in SKILL_FILES:
        if not (DIST_SKILL / name).exists() or not filecmp.cmp(ROOT / name, DIST_SKILL / name, shallow=False):
            errors.append(f"dist is stale: {name}")
    for name in SKILL_DIRS:
        if not (DIST_SKILL / name).exists() or not same_tree(ROOT / name, DIST_SKILL / name):
            errors.append(f"dist is stale: {name}/")
    for name in LEGAL_FILES:
        if not (DIST / name).exists() or not filecmp.cmp(ROOT / name, DIST / name, shallow=False):
            errors.append(f"dist is stale: {name}")
    if (DIST_SKILL / "local.md").exists():
        errors.append("dist contains local.md (personal settings)")
    return errors


if __name__ == "__main__":
    if "--check" not in sys.argv:
        build()
    problems = check()
    for p in problems:
        print(f"ERROR {p}")
    print("dist/ OK" if not problems else f"{len(problems)} problem(s)")
    sys.exit(1 if problems else 0)
