# Background Job Worker

A framework-neutral background worker skeleton with job lifecycle handling,
retry policy, graceful shutdown, and a health signal.

The queue is intentionally an in-memory example. Replace it with Redis,
RabbitMQ, SQS, a database queue, or another queue implementation for a real
deployment.
