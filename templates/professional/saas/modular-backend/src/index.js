import { loadConfig } from "./config/index.js";
import { createLogger } from "./logging/logger.js";
import { createServer } from "./http/server.js";

const config = loadConfig();
const logger = createLogger({service:"modular-backend"});
const server = createServer();

server.listen(config.port, () => {
  logger.info("server started", {port:config.port, environment:config.environment});
});
