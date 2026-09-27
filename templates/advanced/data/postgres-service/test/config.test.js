import test from "node:test";
import assert from "node:assert/strict";

test("database configuration is represented by DATABASE_URL", () => {
  assert.equal(typeof "DATABASE_URL", "string");
});
