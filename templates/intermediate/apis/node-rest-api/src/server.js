import http from "node:http";
import { listItems, createItem, findItem } from "./repository.js";

function send(res, status, data) {
  res.writeHead(status, {"content-type":"application/json; charset=utf-8"});
  res.end(JSON.stringify(data));
}

const server = http.createServer(async (req, res) => {
  const url = new URL(req.url, "http://localhost");

  if (req.method === "GET" && url.pathname === "/api/health")
    return send(res, 200, {status:"ok"});

  if (req.method === "GET" && url.pathname === "/api/items")
    return send(res, 200, listItems());

  if (req.method === "GET" && url.pathname.startsWith("/api/items/")) {
    const item = findItem(url.pathname.split("/").pop());
    return item ? send(res, 200, item) : send(res, 404, {error:"not found"});
  }

  if (req.method === "POST" && url.pathname === "/api/items") {
    let body = "";
    req.on("data", c => body += c);
    req.on("end", () => {
      try {
        const payload = JSON.parse(body || "{}");
        if (typeof payload.name !== "string" || !payload.name.trim())
          return send(res, 400, {error:"name is required"});
        send(res, 201, createItem(payload.name.trim()));
      } catch {
        send(res, 400, {error:"invalid JSON"});
      }
    });
    return;
  }

  send(res, 404, {error:"not found"});
});

const port = Number(process.env.PORT || 3000);
server.listen(port, () => console.log(`API listening on :${port}`));
