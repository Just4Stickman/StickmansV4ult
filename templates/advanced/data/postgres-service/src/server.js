import http from "node:http";

const port = Number(process.env.PORT || 3000);

const server = http.createServer((req,res)=>{
  if(req.url === "/health"){
    res.writeHead(200,{"content-type":"application/json"});
    res.end(JSON.stringify({status:"ok",databaseConfigured:Boolean(process.env.DATABASE_URL)}));
    return;
  }
  res.writeHead(404,{"content-type":"application/json"});
  res.end(JSON.stringify({error:"not found"}));
});

server.listen(port,()=>console.log(`service on :${port}`));
