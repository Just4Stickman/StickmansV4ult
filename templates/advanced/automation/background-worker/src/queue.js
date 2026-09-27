const jobs = [];

export function enqueue(job) {
  jobs.push({...job, attempts:0});
}

export function nextJob() {
  return jobs.shift() ?? null;
}

export function size() {
  return jobs.length;
}
