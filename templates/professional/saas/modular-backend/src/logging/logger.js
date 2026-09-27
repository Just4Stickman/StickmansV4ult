export function createLogger(context = {}) {
  return {
    info(message, data = {}) {
      console.log(JSON.stringify({level:"info", message, ...context, ...data}));
    },
    error(message, data = {}) {
      console.error(JSON.stringify({level:"error", message, ...context, ...data}));
    }
  };
}
