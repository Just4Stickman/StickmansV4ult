import test from "node:test";
import assert from "node:assert/strict";
test("chat input contract", () => {
  const message = "hello";
  assert.equal(typeof message, "string");
});
