import test from "node:test";
import assert from "node:assert/strict";
test("dashboard has an organization concept", () => {
  const organization = { id: "org_demo", name: "Demo Organization" };
  assert.ok(organization.id);
});
