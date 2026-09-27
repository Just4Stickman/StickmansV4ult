export function loadConfig(env = process.env) {
  return {
    port: Number(env.PORT || 3000),
    environment: env.NODE_ENV || "development",
    logLevel: env.LOG_LEVEL || "info"
  };
}
