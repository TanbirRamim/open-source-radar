// Open Source Radar: "is this a good pick?" signals and the start-here best bets.
// Pure functions over one issue and its repository, so scripts/site_pick.test.mjs can run them in Node.
(() => {
  "use strict";

  const DAY = 86400000;

  function ageDays(isoDate, now) {
    return Math.max(0, Math.floor((now - new Date(isoDate + "T00:00:00Z").getTime()) / DAY));
  }

  // How the project treats pull requests from people outside the team. null when we can't tell:
  // too few PRs to judge, or the search hit its cap and the numbers are partial.
  function mergeHealth(repo) {
    const stats = repo.external_prs;
    if (!stats || stats.capped) return null;
    const merged = stats.merged_in_window || 0;
    const created = stats.created_in_window || 0;
    if (merged >= 2 && typeof stats.median_time_to_merge_hours === "number") {
      return { kind: "merges", hours: stats.median_time_to_merge_hours };
    }
    if (merged === 0 && created >= 3) return { kind: "stalls" };
    return null;
  }

  // Signals, best first. Each is { key, tone: "good" | "warn", values }.
  function signals(issue, repo, now = Date.now()) {
    const out = [];
    const age = ageDays(issue.created, now);
    const health = mergeHealth(repo);
    if (health?.kind === "merges" && health.hours <= 72) {
      out.push({ key: health.hours <= 24 ? "pick.mergeDay" : "pick.mergeDays", tone: "good", values: {} });
    }
    if (issue.comments === 0) out.push({ key: "pick.quiet", tone: "good", values: {} });
    if (age <= 14) out.push({ key: "pick.fresh", tone: "good", values: {} });
    if (issue.comments >= 8) out.push({ key: "pick.busy", tone: "warn", values: {} });
    if (health?.kind === "stalls") out.push({ key: "pick.stalls", tone: "warn", values: {} });
    return out;
  }

  // Higher is a better first issue. comfort "new" only takes beginner-labelled issues.
  function score(issue, repo, now = Date.now()) {
    let total = issue.level === "beginner" ? 3 : 0;
    const age = ageDays(issue.created, now);
    if (age <= 14) total += 2;
    else if (age > 120) total -= 1;
    if (issue.comments === 0) total += 2;
    else if (issue.comments <= 3) total += 1;
    else if (issue.comments >= 8) total -= 3;
    if (issue.maintainer_replied === true) total += 2;
    if (issue.closed_pr) total -= 2;
    const health = mergeHealth(repo);
    if (health?.kind === "merges") total += health.hours <= 72 ? 3 : 1;
    if (health?.kind === "stalls") total -= 4;
    if (repo.contributing) total += 1;
    if (repo.policy?.ai === "restricted") total -= 1;
    return total;
  }

  function bestBets(issues, repositories, { language = "", comfort = "new", limit = 5, now = Date.now() } = {}) {
    const scored = [];
    for (const issue of issues) {
      const repo = repositories[issue.repo];
      if (!repo) continue;
      if (language && repo.language !== language) continue;
      if (comfort === "new" && issue.level !== "beginner") continue;
      scored.push({ issue, value: score(issue, repo, now) });
    }
    scored.sort((a, b) => b.value - a.value || b.issue.created.localeCompare(a.issue.created));
    // One per project, so five picks are five different places to try.
    const seen = new Set();
    const picks = [];
    for (const { issue, value } of scored) {
      if (value <= 0 || seen.has(issue.repo)) continue;
      seen.add(issue.repo);
      picks.push(issue);
      if (picks.length === limit) break;
    }
    return picks;
  }

  const api = { signals, score, bestBets, mergeHealth };
  if (typeof window !== "undefined") window.RadarPick = api;
  if (typeof globalThis !== "undefined") globalThis.RadarPick = api;
})();
