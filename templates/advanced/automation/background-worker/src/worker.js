import { enqueue, nextJob, size } from "./queue.js";

let running = true;
enqueue({type:"example", payload:{message:"hello"}});

async function processJob(job) {
  job.attempts += 1;
  console.log("processing", job.type, "attempt", job.attempts);
}

async function loop() {
  while (running) {
    const job = nextJob();
    if (!job) {
      await new Promise(resolve => setTimeout(resolve, 250));
      continue;
    }
    try {
      await processJob(job);
    } catch (error) {
      console.error("job failed", error);
      if (job.attempts < 3) enqueue(job);
    }
  }
}

process.on("SIGTERM", () => {
  running = false;
  console.log("shutdown requested");
});

console.log(`worker starting with ${size()} queued job(s)`);
loop();
