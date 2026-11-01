import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import task_autopilot as ap


def guide(root: Path, files: list[str]) -> None:
    for name in files:
        path = root / "guide" / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("x", encoding="utf-8")


def gfi(title: str, body: str = "", assignee: bool = False) -> dict:
    return {
        "title": title,
        "body": body,
        "assignees": [{"login": "someone"}] if assignee else [],
        "labels": [{"name": "good first issue"}],
    }


class TaskAutopilotTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        guide(
            self.root,
            [
                "01-why-contribute.md",
                "02-setup.md",
                "glossary.md",
                "bn/02-setup.md",
                "es/01-why-contribute.md",
                "es/02-setup.md",
                "es/glossary.md",
            ],
        )

    def tearDown(self):
        self.tmp.cleanup()

    def test_titles(self):
        self.assertEqual(
            ap.title_for("05-first-pull-request.md", "Bengali"), "Translate chapter 5 (first pull request) to Bengali"
        )
        self.assertEqual(ap.title_for("glossary.md", "Hindi"), "Translate the glossary to Hindi")

    def test_missing_translations_take_turns_between_languages(self):
        self.assertEqual(
            ap.missing_translations(self.root),
            [("bn", "01-why-contribute.md"), ("bn", "glossary.md")],
        )
        guide(self.root, ["uk/README.md"])
        self.assertEqual(
            ap.missing_translations(self.root)[:3],
            [("bn", "01-why-contribute.md"), ("uk", "01-why-contribute.md"), ("bn", "glossary.md")],
        )

    def test_languages_without_a_folder_get_nothing(self):
        self.assertNotIn("vi", {folder for folder, _ in ap.missing_translations(self.root)})

    def test_opens_only_enough_to_reach_the_minimum(self):
        guide(self.root, ["uk/README.md"])
        issues = [gfi(f"free {n}") for n in range(ap.MIN_FREE - 1)]
        self.assertEqual(ap.plan(issues, self.root), [("bn", "01-why-contribute.md")])
        issues.append(gfi("one more"))
        self.assertEqual(ap.plan(issues, self.root), [])

    def test_claimed_issues_do_not_count_as_free(self):
        issues = [gfi(f"taken {n}", assignee=True) for n in range(10)]
        self.assertEqual(len(ap.plan(issues, self.root)), 2)

    def test_existing_issue_by_title_or_path_is_not_duplicated(self):
        issues = [
            gfi("Translate chapter 1 (why contribute) to Bengali", assignee=True),
            gfi("Bengali glossary", body="Create `guide/bn/glossary.md` translated from ..."),
        ]
        self.assertEqual(ap.plan(issues, self.root), [])

    def test_body_points_at_the_target_file_and_claim_bot(self):
        body = ap.body_for("bn", "glossary.md", "Bengali")
        self.assertIn("`guide/bn/glossary.md`", body)
        self.assertIn("/claim", body)


if __name__ == "__main__":
    unittest.main()
