import test from "node:test";
import assert from "node:assert/strict";
import { health } from "../src/modules/health/health.js";

test("health returns an operational status", () => {
  assert.equal(health().status, "ok");
});
