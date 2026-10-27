import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_PATH = Path(
    os.getenv(
        "SENTINEL_DB",
        str(BASE_DIR / "sentinelrat.db"),
    )
)

API_KEY = os.getenv("SENTINEL_API_KEY", "")

if not API_KEY:
    raise RuntimeError(
        "SENTINEL_API_KEY is not configured. "
        "Set it in your environment before starting the server."
    )