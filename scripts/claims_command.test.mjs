import assert from "node:assert/strict";
import test from "node:test";

import { findCommand } from "./claims_command.mjs";

test("findCommand recognizes claim commands on unquoted lines", () => {
  assert.equal(findCommand("/claim"), "/claim");
  assert.equal(findCommand("hi\n/claim"), "/claim");
  assert.equal(findCommand("/unclaim thanks"), "/unclaim thanks");
});

test("findCommand ignores quoted lines and comments without a command", () => {
  assert.equal(findCommand("> /claim"), undefined);
  assert.equal(findCommand("I would like to help"), undefined);
});
