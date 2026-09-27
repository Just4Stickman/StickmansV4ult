import http from "node:http";
import { health } from "../modules/health/health.js";

export function createServer() {
  return http.createServer((req,res)=>{
    if(req.url === "/health"){
      res.writeHead(200,{"content-type":"application/json"});
      res.end(JSON.stringify(health()));
      return;
    }
    res.writeHead(404,{"content-type":"application/json"});
    res.end(JSON.stringify({error:"not found"}));
  });
}
