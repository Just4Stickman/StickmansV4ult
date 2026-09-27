import http from "node:http";
import { readFile } from "node:fs/promises";
import { join } from "node:path";
import { fileURLToPath } from "node:url";
import { state } from "./store.js";

const root=join(fileURLToPath(import.meta.url),"..","..");
const port=Number(process.env.PORT||3000);

function send(res,status,data,type="application/json"){
  res.writeHead(status,{"content-type":type});
  res.end(type.includes("json")?JSON.stringify(data):data);
}

const server=http.createServer(async(req,res)=>{
  const url=new URL(req.url,"http://localhost");
  if(req.method==="GET"&&url.pathname==="/"){
    send(res,200,await readFile(join(root,"web","index.html"),"utf8"),"text/html; charset=utf-8"); return;
  }
  if(req.method==="GET"&&url.pathname==="/api/dashboard")
    return send(res,200,state);
  if(req.method==="GET"&&url.pathname==="/api/health")
    return send(res,200,{status:"ok"});
  send(res,404,{error:"not found"});
});
server.listen(port,()=>console.log(`Dashboard on :${port}`));
