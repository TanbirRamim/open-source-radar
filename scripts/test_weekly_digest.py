import datetime as dt
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import weekly_digest as wd

TODAY = dt.date(2026, 11, 2)


def issue(repo, number, created="2026-10-30", level="beginner", comments=0, closed_pr=False):
    return {
        "repo": repo,
        "number": number,
        "title": f"Fix the parser bug {number}",
        "url": f"https://github.com/{repo}/issues/{number}",
        "created": created,
        "level": level,
        "comments": comments,
        "closed_pr": closed_pr,
    }


def repo(stars, merge_rate=0.5):
    return {"stars": stars, "language": "Python", "external_prs": {"merge_rate": merge_rate}}


class WeeklyDigestTests(unittest.TestCase):
    def payload(self, issues, repos):
        return {"issues": issues, "repositories": repos}

    def test_picks_fresh_quiet_beginner_issues_one_per_project_by_stars(self):
        payload = self.payload(
            [
                issue("a/small", 1),
                issue("b/big", 2),
                issue("b/big", 3),
                issue("c/old", 4, created="2026-10-01"),
                issue("d/busy", 5, comments=5),
                issue("e/help", 6, level="help-wanted"),
                issue("f/retried", 7, closed_pr=True),
            ],
            {
                "a/small": repo(10),
                "b/big": repo(1000),
                "c/old": repo(500),
                "d/busy": repo(500),
                "e/help": repo(500),
                "f/retried": repo(500),
            },
        )
        self.assertEqual([i["number"] for i in wd.pick(payload, TODAY)], [2, 1])

    def test_skips_projects_that_rarely_merge_outside_prs(self):
        payload = self.payload(
            [issue("a/closed", 1), issue("b/unknown", 2)],
            {"a/closed": repo(10, merge_rate=0.05), "b/unknown": {"stars": 5, "language": None, "external_prs": None}},
        )
        self.assertEqual([i["number"] for i in wd.pick(payload, TODAY)], [2])

    def test_caps_the_number_of_picks(self):
        repos = {f"o/r{n}": repo(n) for n in range(20)}
        payload = self.payload([issue(f"o/r{n}", n) for n in range(20)], repos)
        self.assertEqual(len(wd.pick(payload, TODAY)), wd.PICKS)

    def test_skips_template_and_bot_titles(self):
        self.assertFalse(wd.readable_title("[ACTION]"))
        self.assertFalse(wd.readable_title("Link Checker Report"))
        self.assertTrue(wd.readable_title("[docs] Fix the install command on Windows"))

    def test_brackets_in_titles_are_escaped(self):
        self.assertEqual(wd.escape("[bug] x"), "\\[bug\\] x")

    def test_render(self):
        payload = self.payload([issue("b/big", 2)], {"b/big": repo(1234)})
        title, body = wd.render(wd.pick(payload, TODAY), payload, TODAY)
        self.assertEqual(title, "Fresh beginner issues, week of 2026-11-02")
        line = "- [Fix the parser bug 2](https://github.com/b/big/issues/2) in **b/big** (Python, 1,234 stars)"
        self.assertIn(line, body)


if __name__ == "__main__":
    unittest.main()
