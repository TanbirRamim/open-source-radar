import assert from "node:assert/strict";
import test from "node:test";

const findCommand = (text) =>
  text
    .split("\n")
    .map((line) => line.trim())
    .find((line) => line.startsWith("/claim") || line.startsWith("/unclaim"));

test("findCommand recognizes claim commands on unquoted lines", () => {
  assert.equal(findCommand("/claim"), "/claim");
  assert.equal(findCommand("hi\n/claim"), "/claim");
  assert.equal(findCommand("/unclaim thanks"), "/unclaim thanks");
});

test("findCommand ignores quoted lines and comments without a command", () => {
  assert.equal(findCommand("> /claim"), undefined);
  assert.equal(findCommand("I would like to help"), undefined);
});
