# Modular SaaS Backend

A professional-level architecture reference for a modular backend.

## Modules

- configuration
- HTTP transport
- health
- logging
- domain services
- infrastructure boundaries

The template intentionally does not pretend to solve every production concern.
Authentication, authorization, tenant isolation, billing, migrations,
observability, rate limiting, queues, deployment policy, backups, and incident
response must be designed for the actual product.

## Run

```bash
npm install
npm test
npm start
```
