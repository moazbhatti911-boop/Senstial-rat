import json
import logging
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
AUDIT_FILE = BASE_DIR / "sentinelrat-audit.log"

logger = logging.getLogger("sentinelrat.audit")
logger.setLevel(logging.INFO)

if not logger.handlers:
    handler = logging.FileHandler(
        AUDIT_FILE,
        encoding="utf-8",
    )
    handler.setFormatter(logging.Formatter("%(message)s"))
    logger.addHandler(handler)


def record_event(
    event: str,
    device_id: str | None = None,
    details: str = "",
) -> None:
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "event": event,
        "device_id": device_id,
        "details": details,
    }

    logger.info(
        json.dumps(entry, ensure_ascii=False)
    )