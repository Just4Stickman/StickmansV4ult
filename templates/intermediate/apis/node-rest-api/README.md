# Node REST API

A structured REST API starter using Node.js without a mandatory web framework.

## Features

- REST-style routing
- JSON responses
- Request validation
- Health endpoint
- In-memory example repository
- Unit tests
- Docker
- GitHub Actions

## Run

```bash
npm install
npm test
npm start
```

API endpoints:

- `GET /api/health`
- `GET /api/items`
- `POST /api/items`
- `GET /api/items/:id`

This is a starting point; replace the in-memory repository with a real database
and add authentication/rate limiting before production deployment.
