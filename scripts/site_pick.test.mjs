import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import test from "node:test";
import vm from "node:vm";

const source = readFileSync(new URL("../site/assets/pick.js", import.meta.url), "utf8");
const context = { window: {} };
vm.runInNewContext(source, context);
const { signals, score, bestBets, mergeHealth, demoteStalled } = context.window.RadarPick;

const NOW = Date.parse("2026-11-22T12:00:00Z");
const fast = { merged_in_window: 5, created_in_window: 6, median_time_to_merge_hours: 10, capped: false };
const stalled = { merged_in_window: 0, created_in_window: 9, median_time_to_merge_hours: null, capped: false };

function issue(overrides = {}) {
  return {
    repo: "a/one", number: 1, title: "Fix typo", url: "https://github.com/a/one/issues/1",
    level: "beginner", created: "2026-11-20", updated: "2026-11-21", comments: 0,
    maintainer_replied: false, closed_pr: false, labels: [], ...overrides,
  };
}
const repo = (overrides = {}) => ({ language: "Python", external_prs: fast, contributing: "CONTRIBUTING.md", policy: {}, ...overrides });
const keys = (list) => [...list].map((signal) => signal.key);

test("a fresh, quiet issue in a project that merges fast gets the good signals", () => {
  assert.deepEqual(keys(signals(issue(), repo(), NOW)), ["pick.mergeDay", "pick.quiet", "pick.fresh"]);
});

test("busy threads and stalled projects are flagged as warnings", () => {
  const out = signals(issue({ comments: 12, created: "2026-06-01" }), repo({ external_prs: stalled }), NOW);
  assert.deepEqual(keys(out), ["pick.busy", "pick.stalls"]);
  assert.ok(out.every((signal) => signal.tone === "warn"));
});

test("capped or thin merge stats say nothing rather than guess", () => {
  assert.equal(mergeHealth(repo({ external_prs: { ...stalled, capped: true } })), null);
  assert.equal(mergeHealth(repo({ external_prs: { merged_in_window: 1, created_in_window: 1, median_time_to_merge_hours: 3 } })), null);
  assert.equal(mergeHealth(repo({ external_prs: undefined })), null);
});

test("a stalled project scores below a responsive one", () => {
  assert.ok(score(issue(), repo(), NOW) > score(issue(), repo({ external_prs: stalled }), NOW));
  assert.ok(score(issue({ comments: 0 }), repo(), NOW) > score(issue({ comments: 10 }), repo(), NOW));
});

test("best bets honour language and comfort, and take one issue per project", () => {
  const issues = [
    issue({ repo: "a/one", number: 1 }),
    issue({ repo: "a/one", number: 2 }),
    issue({ repo: "b/two", number: 3, level: "help-wanted" }),
    issue({ repo: "c/three", number: 4 }),
    issue({ repo: "d/four", number: 5 }),
  ];
  const repositories = {
    "a/one": repo(), "b/two": repo(), "c/three": repo({ language: "Rust" }),
    "d/four": repo({ external_prs: stalled }),
  };
  const picks = (options) => [...bestBets(issues, repositories, { now: NOW, ...options })].map((i) => i.number);
  assert.deepEqual(picks({ language: "Python", comfort: "new" }), [1, 5]);
  assert.deepEqual(picks({ language: "Python", comfort: "some" }), [1, 3, 5]);
  assert.deepEqual(picks({ language: "Rust" }), [4]);
  assert.deepEqual(picks({ limit: 2 }), [1, 4]);
});

test("issues that score zero or less are never suggested", () => {
  const bad = issue({ comments: 20, created: "2026-01-01", closed_pr: true });
  const picks = bestBets([bad], { "a/one": repo({ external_prs: stalled, contributing: null }) }, { now: NOW });
  assert.equal(picks.length, 0);
});

test("stalled projects sink to the end of the list, everything else keeps its order", () => {
  const repos = { "a/one": repo(), "b/stuck": repo({ external_prs: stalled }), "c/new": repo({ external_prs: undefined }) };
  const list = [issue({ repo: "b/stuck", number: 1 }), issue({ repo: "a/one", number: 2 }), issue({ repo: "c/new", number: 3 }), issue({ repo: "b/stuck", number: 4 })];
  assert.deepEqual([...demoteStalled(list, repos)].map((item) => item.number), [2, 3, 1, 4]);
});
