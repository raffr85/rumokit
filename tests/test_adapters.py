from __future__ import annotations

import json
import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_json(path: Path) -> dict:
    return json.loads(path.read_text())


class AdapterPackagingTest(unittest.TestCase):
    def test_package_identifiers_agree_across_hosts(self) -> None:
        for relative in ("plugin.json", ".codex-plugin/plugin.json", ".claude-plugin/plugin.json"):
            with self.subTest(manifest=relative):
                self.assertEqual(load_json(ROOT / relative)["name"], "rumokit")
        adapter = ROOT / "adapters" / "rumokit-codex" / ".codex-plugin" / "plugin.json"
        self.assertEqual(load_json(adapter)["name"], "rumokit-codex")

    def test_manifests_share_one_version(self) -> None:
        manifests = [
            ROOT / "plugin.json",
            ROOT / ".codex-plugin" / "plugin.json",
            ROOT / ".claude-plugin" / "plugin.json",
            ROOT / "adapters" / "rumokit-codex" / ".codex-plugin" / "plugin.json",
        ]

        versions = {load_json(path)["version"] for path in manifests}

        self.assertEqual(len(versions), 1)

    def test_claude_session_start_emits_the_portable_router(self) -> None:
        completed = subprocess.run(
            [str(ROOT / "hooks" / "session-start")],
            check=False,
            capture_output=True,
            text=True,
            env={**os.environ, "CLAUDE_PLUGIN_ROOT": str(ROOT)},
        )

        self.assertEqual(completed.returncode, 0, completed.stderr)
        output = json.loads(completed.stdout)
        hook_output = output["hookSpecificOutput"]
        self.assertEqual(hook_output["hookEventName"], "SessionStart")
        context = hook_output["additionalContext"]
        self.assertIn("<RUMOKIT_BOOTSTRAP>", context)
        self.assertIn("# Use RumoKit", context)
        self.assertIn("scope-product-increment", context)
        self.assertNotIn(str(ROOT), context)

    def test_claude_session_start_works_from_a_relocated_plugin_root(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            relocated = Path(temporary) / "plugin with spaces"
            shutil.copytree(
                ROOT,
                relocated,
                ignore=shutil.ignore_patterns(".git", "__pycache__", "tests"),
            )
            command = load_json(relocated / "hooks" / "hooks.json")["hooks"][
                "SessionStart"
            ][0]["hooks"][0]["command"]
            completed = subprocess.run(
                ["sh", "-c", command],
                cwd=temporary,
                capture_output=True,
                text=True,
                check=False,
                env={**os.environ, "CLAUDE_PLUGIN_ROOT": str(relocated)},
            )

        self.assertEqual(completed.returncode, 0, completed.stderr)
        hook_output = json.loads(completed.stdout)["hookSpecificOutput"]
        self.assertEqual(hook_output["hookEventName"], "SessionStart")
        self.assertIn("# Use RumoKit", hook_output["additionalContext"])
        self.assertIn("clarify-intent", hook_output["additionalContext"])
        self.assertNotIn(str(ROOT), hook_output["additionalContext"])

    def test_claude_layout_hook_has_no_host_specific_source_filter(self) -> None:
        hooks = load_json(ROOT / "hooks" / "hooks.json")["hooks"]
        session_start = hooks["SessionStart"]

        self.assertEqual(len(session_start), 1)
        # SessionStart sources differ by host. An unfiltered registration
        # also includes resume; real loader checks complement this shape test.
        self.assertEqual(session_start[0]["matcher"], "")
        command = session_start[0]["hooks"][0]
        self.assertEqual(command["type"], "command")
        self.assertIn("${CLAUDE_PLUGIN_ROOT}", command["command"])

    def test_codex_manifest_uses_native_component_discovery(self) -> None:
        manifest = load_json(ROOT / ".codex-plugin" / "plugin.json")

        self.assertNotIn("hooks", manifest)
        self.assertEqual(manifest["skills"], "./skills/")

    def test_codex_hook_emits_its_bundled_bootstrap(self) -> None:
        adapter = ROOT / "adapters" / "rumokit-codex"
        events = load_json(adapter / "hooks" / "hooks.json")["hooks"]["SessionStart"]
        self.assertEqual(len(events), 1)
        self.assertEqual(events[0]["matcher"], "startup|resume|clear|compact")
        hook = events[0]["hooks"][0]
        completed = subprocess.run(
            ["sh", "-c", hook["command"]],
            capture_output=True,
            check=False,
            env={**os.environ, "PLUGIN_ROOT": str(adapter)},
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertEqual(
            completed.stdout,
            (adapter / "hooks" / "session-start-context.md").read_bytes(),
        )
        self.assertIn(b"`use-rumokit`", completed.stdout)
        self.assertTrue((ROOT / "skills" / "use-rumokit" / "SKILL.md").is_file())


if __name__ == "__main__":
    unittest.main()
