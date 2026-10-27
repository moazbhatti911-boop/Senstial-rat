import platform
from datetime import datetime, timezone

import psutil


def collect_telemetry() -> dict:
    return {
        "hostname": platform.node(),
        "platform": platform.system(),
        "cpu_percent": psutil.cpu_percent(interval=0.2),
        "memory_percent": psutil.virtual_memory().percent,
        "reported_at": datetime.now(
            timezone.utc
        ).isoformat(),
    }