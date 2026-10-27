import secrets

from fastapi import Header, HTTPException

from server.config import API_KEY


def require_api_key(
    x_api_key: str = Header(default="", alias="X-API-Key"),
) -> None:
    if not secrets.compare_digest(x_api_key, API_KEY):
        raise HTTPException(
            status_code=401,
            detail="Invalid or missing API key",
        )