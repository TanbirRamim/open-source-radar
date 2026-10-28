import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import test from "node:test";
import vm from "node:vm";

const i18nSource = readFileSync(new URL("../site/assets/i18n.js", import.meta.url), "utf8");
const indexSource = readFileSync(new URL("../site/index.html", import.meta.url), "utf8");

function loadI18n(requestedLocale, navigator = { language: "en" }) {
  const select = { value: "", addEventListener() { } };
  const context = {
    window: {},
    navigator,
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

function localeSelectValues() {
  const select = indexSource.match(/<select id="locale-select"[\s\S]*?<\/select>/)?.[0];
  assert.ok(select, "locale selector is present");
  return [...select.matchAll(/<option\s+value="([^"]+)"\s+lang="([^"]+)"/g)]
    .map((match) => ({ value: match[1], lang: match[2] }));
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

test("every locale defines every site message", () => {
  const keys = [...new Set([...staticKeys(), ...dynamicKeys])];
  // Every locale in messages, so a new locale PR does not need to edit this test.
  for (const locale of Object.keys(loadI18n("en").messages)) {
    const i18n = loadI18n(locale);
    assert.equal(i18n.locale, locale);
    for (const key of keys) assert.notEqual(i18n.t(key), key, `${locale} is missing ${key}`);
  }
});

test("unsupported locales fall back to English", () => {
  const i18n = loadI18n("sw");
  assert.equal(i18n.locale, "en");
  assert.equal(i18n.t("query.copy"), "Copy");
});

test("messages interpolate values", () => {
  assert.equal(loadI18n("es").t("repo.stars", { count: "25" }), "25 estrellas");
  assert.equal(loadI18n("hi").t("repo.stars", { count: "25" }), "25 स्टार्स");
  assert.equal(loadI18n("pt").t("repo.stars", { count: "25" }), "25 estrelas");
  assert.equal(loadI18n("fr").t("repo.stars", { count: "25" }), "25 étoiles");
});

test("every locale has the same keys as English", () => {
  // Loops over every locale in messages, so a new locale is checked without touching this test.
  const { messages } = loadI18n("en");
  const en = Object.keys(messages.en).sort();
  for (const [locale, table] of Object.entries(messages)) {
    const keys = Object.keys(table);
    assert.deepEqual(keys.filter((key) => !en.includes(key)), [], `keys only in ${locale}`);
    assert.deepEqual(en.filter((key) => !keys.includes(key)), [], `keys missing in ${locale}`);
  }
});

test("every translation keeps the English placeholders", () => {
  // A dropped or translated {count} renders as a literal "{count}" on the page, so compare the sets.
  const { messages } = loadI18n("en");
  // Plural messages are objects of forms; every form has to keep the placeholders.
  const placeholders = (text) =>
    [...new Set(Object.values(typeof text === "object" ? text : { text }).join(" ").match(/\{\w+\}/g) ?? [])].sort();
  for (const [locale, table] of Object.entries(messages)) {
    for (const [key, text] of Object.entries(messages.en)) {
      if (!(key in table)) continue;
      assert.deepEqual(placeholders(table[key]), placeholders(text), `${locale} ${key}`);
    }
  }
});

test("the locale menu matches the available message locales", () => {
  const { messages } = loadI18n("en");
  // Compare as sorted lists: the menu order is a display choice (e.g. English first),
  // the test only cares that no locale is missing from either side.
  const options = localeSelectValues();
  assert.deepEqual(options.map((option) => option.value).sort(), Object.keys(messages).sort());
  // A lang can be more specific than the locale code, like zh-Hans for the Simplified Chinese option.
  for (const option of options) {
    assert.ok(
      option.lang === option.value || option.lang.startsWith(`${option.value}-`),
      `${option.value} option has matching lang (got ${option.lang})`,
    );
  }
});

test("the first supported browser language wins", () => {
  assert.equal(loadI18n(null, { language: "pa-IN", languages: ["pa-IN", "hi-IN", "es"] }).locale, "hi");
  assert.equal(loadI18n(null, { language: "pt-BR", languages: ["pt-BR"] }).locale, "pt");
});

test("browser languages fall back to navigator.language, then English", () => {
  assert.equal(loadI18n(null, { language: "fr-CA" }).locale, "fr");
  assert.equal(loadI18n(null, { language: "pa", languages: ["pa", "ta"] }).locale, "en");
});

test("a saved choice beats the browser languages", () => {
  assert.equal(loadI18n("de", { language: "es", languages: ["es"] }).locale, "de");
});

test("plural messages pick the right form", () => {
  const pl = loadI18n("pl");
  assert.equal(pl.t("time.months", { count: "3", n: 3 }), "zaktualizowano 3 miesiące temu");
  assert.equal(pl.t("time.months", { count: "7", n: 7 }), "zaktualizowano 7 miesięcy temu");
  assert.equal(pl.t("issue.comments", { count: "22", n: 22 }), "22 komentarze");
  assert.equal(pl.t("issue.comments", { count: "0", n: 0 }), "0 komentarzy");
  assert.equal(pl.t("time.years", { count: "5", n: 5 }), "zaktualizowano 5 lat temu");
  // Plain string messages ignore n.
  assert.equal(loadI18n("en").t("time.months", { count: "3", n: 3 }), "updated 3 months ago");
});

test("every plural message has an other form", () => {
  for (const [locale, table] of Object.entries(loadI18n("en").messages)) {
    for (const [key, text] of Object.entries(table)) {
      if (typeof text === "object") assert.equal(typeof text.other, "string", `${locale} ${key}`);
    }
  }
});
