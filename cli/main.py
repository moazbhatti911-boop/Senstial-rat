import argparse
import json
import os
import urllib.request


def main() -> None:
    parser = argparse.ArgumentParser(
        description="SentinelRAT administration CLI"
    )

    parser.add_argument(
        "command",
        choices=["health", "devices"],
    )

    parser.add_argument(
        "--url",
        default=os.getenv(
            "SENTINEL_SERVER_URL",
            "http://127.0.0.1:8000",
        ),
    )

    args = parser.parse_args()

    api_key = os.getenv("SENTINEL_API_KEY", "")

    if not api_key:
        parser.error("SENTINEL_API_KEY is not configured")

    headers = {"X-API-Key": api_key}

    path = {
        "health": "/health",
        "devices": "/devices/",
    }[args.command]

    request = urllib.request.Request(
        f"{args.url.rstrip('/')}{path}",
        headers=headers,
    )

    with urllib.request.urlopen(request, timeout=5.0) as response:
        print(
            json.dumps(
                json.load(response),
                indent=2,
            )
        )


if __name__ == "__main__":
    main()