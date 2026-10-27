import os
from agent.identity import get_device_identity
from agent.transport import SentinelTransport
from agent.telemetry import collect_telemetry

def main() -> None:
    api_url = os.getenv(
        "SENTINEL_SERVER_URL",
        "http://127.0.0.1:8000",
    )

    api_key = os.getenv("SENTINEL_API_KEY", "")

    if not api_key:
        raise RuntimeError(
            "Set SENTINEL_API_KEY before starting the client."
        )

    identity = get_device_identity()

    print("SentinelRAT authorized client")
    print(f"Hostname: {identity['hostname']}")
    print(f"Platform: {identity['platform']}")

    transport = SentinelTransport(api_url, api_key)

    result = transport.enroll(
        hostname=identity["hostname"],
        platform_name=identity["platform"],
    )

    print(f"Enrollment successful: {result['enrolled']}")
    print(f"Device ID: {result['device_id']}")

    telemetry = collect_telemetry()

    print("\nLocal telemetry:")
    for key, value in telemetry.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()