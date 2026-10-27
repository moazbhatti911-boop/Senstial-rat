# SentinelRAT Architecture

## Components

- Agent: collects basic local system telemetry.
- Server: provides authenticated API endpoints.
- Enrollment: registers authorized devices.
- Device registry: stores device metadata in SQLite.
- Action registry: validates predefined actions.
- Audit logger: records security-relevant events.
- Dashboard: displays registered devices.
- CLI: provides terminal-based administration.

## Communication

The client communicates with the server over HTTP.

Local development uses loopback networking.

Production deployment requires HTTPS, secure credential
management, device-specific authorization, and access controls.

## Database

SQLite stores device records and telemetry.

Database migrations and retention policies should be added
before production use.