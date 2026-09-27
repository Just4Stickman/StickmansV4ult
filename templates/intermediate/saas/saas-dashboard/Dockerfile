FROM node:20-alpine
WORKDIR /app
COPY package.json .
RUN npm install --omit=dev
COPY server ./server
COPY web ./web
EXPOSE 3000
CMD ["node","server/index.js"]
