export function health() {
  return {
    status: "ok",
    timestamp: new Date().toISOString()
  };
}
