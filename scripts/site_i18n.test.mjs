import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import test from "node:test";
import vm from "node:vm";

const i18nSource = readFileSync(new URL("../site/assets/i18n.js", import.meta.url), "utf8");
const indexSource = readFileSync(new URL("../site/index.html", import.meta.url), "utf8");

function loadI18n(requestedLocale) {
  const select = { value: "", addEventListener() { } };
  const context = {
    window: {},
    navigator: { language: "en" },
    localStorage: { getItem: () => requestedLocale, setItem() { } },
    location: { reload() { } },
    document: {
      documentElement: {},
      getElementById: () => select,
      querySelectorAll: () => [],
    },
  };
  vm.runInNewContext(i18nSource, context);
  return context.window.RadarI18n;
}

function staticKeys() {
  const pattern = /data-i18n(?:-html|-content|-aria-label|-title|-placeholder)?="([^"]+)"/g;
  return [...indexSource.matchAll(pattern)].map((match) => match[1]);
}

const dynamicKeys = [
  "badge.aiDisclose", "badge.aiPolicy", "badge.aiRestricted", "badge.closedPr", "badge.dco",
  "badge.guide", "feed.language", "feed.topic", "footer.updated", "issue.beginner", "issue.comments",
  "issue.helpWanted", "issue.maintainerReplied", "issue.maintainerRepliedTitle", "issue.moreLabels",
  "issue.oneComment", "issue.onlyAria", "issue.searchLabel", "load.error", "more", "query.copied",
  "repo.forks", "repo.guide", "repo.openMany", "repo.openOne", "repo.showAll", "repo.stars",
  "summary.match", "time.days", "time.months", "time.openedPrefix", "time.pushedPrefix", "time.today",
  "time.updatedPrefix", "time.year", "time.years", "time.yesterday", "title.issue", "title.issues",
];

test("English, Spanish and Hindi define every site message", () => {
  const keys = [...new Set([...staticKeys(), ...dynamicKeys])];
  for (const locale of ["en", "es", "hi"]) {
    const i18n = loadI18n(locale);
    assert.equal(i18n.locale, locale);
    for (const key of keys) assert.notEqual(i18n.t(key), key, `${locale} is missing ${key}`);
  }
});

test("unsupported locales fall back to English", () => {
  const i18n = loadI18n("fr");
  assert.equal(i18n.locale, "en");
  assert.equal(i18n.t("query.copy"), "Copy");
});

test("messages interpolate values", () => {
  assert.equal(loadI18n("es").t("repo.stars", { count: "25" }), "25 estrellas");
  assert.equal(loadI18n("hi").t("repo.stars", { count: "25" }), "25 स्टार्स");
});

test("English and Spanish have the same keys", () => {
  const { messages } = loadI18n("en");
  const en = Object.keys(messages.en).sort();
  const es = Object.keys(messages.es).sort();
  const hi = Object.keys(messages.hi).sort();
  assert.deepEqual(es.filter((key) => !en.includes(key)), [], "keys only in es");
  assert.deepEqual(en.filter((key) => !es.includes(key)), [], "keys only in en");
  assert.deepEqual(hi.filter((key) => !en.includes(key)), [], "keys only in hi");
  assert.deepEqual(en.filter((key) => !hi.includes(key)), [], "keys only in en");
});
