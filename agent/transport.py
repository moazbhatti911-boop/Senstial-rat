import httpx


class SentinelTransport:
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url.rstrip("/")

        self.headers = {
            "X-API-Key": api_key,
        }

    def enroll(
        self,
        hostname: str,
        platform_name: str,
    ) -> dict:
        with httpx.Client(
            base_url=self.base_url,
            headers=self.headers,
            timeout=10.0,
        ) as client:
            response = client.post(
                "/enrollment/",
                json={
                    "hostname": hostname,
                    "platform": platform_name,
                },
            )

            response.raise_for_status()
            return response.json()