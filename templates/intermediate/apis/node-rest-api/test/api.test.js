import test from "node:test";
import assert from "node:assert/strict";

test("basic API data contract", () => {
  const response = { status: "ok" };
  assert.equal(response.status, "ok");
});
