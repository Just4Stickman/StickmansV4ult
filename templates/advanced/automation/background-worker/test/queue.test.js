import test from "node:test";
import assert from "node:assert/strict";
import { enqueue, nextJob, size } from "../src/queue.js";

test("queue stores and returns jobs", () => {
  enqueue({type:"test"});
  assert.equal(size(), 1);
  assert.equal(nextJob().type, "test");
});
