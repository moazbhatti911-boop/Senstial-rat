# SentinelRAT Threat Model

## Assets

- API credentials
- Device inventory
- Telemetry records
- Audit logs

## Threats

- Unauthorized device enrollment
- API credential disclosure
- Unauthorized access to device information
- Tampering with audit logs
- Malicious or malformed API requests
- Unauthorized remote actions

## Mitigations

- API authentication
- Input validation
- Parameterized SQL queries
- Explicit action allowlisting
- Local development binding
- Secret exclusion from version control
- Security audit logging

## Limitations

The demonstration uses a shared API key and SQLite.
It is not a production-ready endpoint security platform.