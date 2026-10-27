# SentinelRAT API

## Public endpoints

GET /health

Returns the server health status.

## Authenticated endpoints

GET /admin/status

Returns administrative service status.

POST /enrollment/

Enrolls a device.

GET /devices/

Lists enrolled devices.

GET /devices/{device_id}

Returns a registered device.

POST /actions/

Validates and handles an allowlisted action.

## Authentication

Supply the X-API-Key header to access protected endpoints.