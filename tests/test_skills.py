from __future__ import annotations

import re
import unittest
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]


class SkillPackagingTest(unittest.TestCase):
    def test_pr_capabilities_are_discoverable(self) -> None:
        for name in ("prepare-pr", "address-review", "fix-ci", "watch-pr"):
            with self.subTest(skill=name):
                self.assertTrue((ROOT / "skills" / name / "SKILL.md").is_file())

    def test_catalog_matches_packaged_skills(self) -> None:
        catalog = (ROOT / "docs" / "DESIGN.md").read_text()
        listed = re.findall(r"^\| [^|]+ \| `([^`]+)` \|", catalog, re.MULTILINE)
        packaged = {path.parent.name for path in (ROOT / "skills").glob("*/SKILL.md")}
        self.assertEqual(len(listed), len(set(listed)))
        self.assertEqual(set(listed), packaged)

    def test_relative_skill_resources_resolve_inside_package(self) -> None:
        for document in (ROOT / "skills").rglob("*.md"):
            for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", document.read_text()):
                link = urlsplit(target)
                if link.scheme or link.netloc or not link.path:
                    continue
                with self.subTest(document=document.relative_to(ROOT), target=target):
                    resolved = (document.parent / unquote(link.path)).resolve()
                    self.assertTrue(resolved.is_relative_to(ROOT))
                    self.assertTrue(resolved.is_file(), f"Missing resource: {target}")


if __name__ == "__main__":
    unittest.main()
