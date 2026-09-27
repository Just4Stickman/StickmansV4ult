import http from "node:http";
import { readFile } from "node:fs/promises";
import { join } from "node:path";
import { fileURLToPath } from "node:url";
import { generateReply } from "./provider.js";

const root = join(fileURLToPath(import.meta.url), "..", "..");
const port = Number(process.env.PORT || 3000);

function send(res, status, data) {
  res.writeHead(status, {"content-type":"application/json"});
  res.end(JSON.stringify(data));
}

const server = http.createServer(async (req,res) => {
  const url = new URL(req.url, "http://localhost");

  if (req.method === "GET" && url.pathname === "/") {
    const html = await readFile(join(root,"public","index.html"),"utf8");
    res.writeHead(200,{"content-type":"text/html; charset=utf-8"});
    res.end(html);
    return;
  }

  if (req.method === "GET" && url.pathname === "/api/health")
    return send(res,200,{status:"ok"});

  if (req.method === "POST" && url.pathname === "/api/chat") {
    let body="";
    req.on("data",c => body += c);
    req.on("end",async()=>{
      try {
        const data=JSON.parse(body||"{}");
        const message=typeof data.message==="string" ? data.message.trim() : "";
        if (!message) return send(res,400,{error:"message is required"});
        send(res,200,{reply:await generateReply(message)});
      } catch {
        send(res,400,{error:"invalid request"});
      }
    });
    return;
  }

  send(res,404,{error:"not found"});
});

server.listen(port,()=>console.log(`AI chatbot on :${port}`));
