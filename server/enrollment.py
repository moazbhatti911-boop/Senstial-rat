import sqlite3
import uuid
from datetime import datetime, timezone

from fastapi import APIRouter, Depends

from server.auth import require_api_key
from server.config import DATABASE_PATH
from server.audit import record_event
from shared.schemas import (
    EnrollmentRequest,
    EnrollmentResponse,
)

router = APIRouter(
    prefix="/enrollment",
    tags=["Enrollment"],
    dependencies=[Depends(require_api_key)],
)


def initialize_database() -> None:
    with sqlite3.connect(DATABASE_PATH) as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS devices (
                device_id TEXT PRIMARY KEY,
                hostname TEXT NOT NULL,
                platform TEXT NOT NULL,
                enrolled_at TEXT NOT NULL,
                last_seen TEXT
            )
            """
        )

        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS telemetry (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                device_id TEXT NOT NULL,
                cpu_percent REAL NOT NULL,
                memory_percent REAL NOT NULL,
                reported_at TEXT NOT NULL,
                FOREIGN KEY(device_id)
                    REFERENCES devices(device_id)
            )
            """
        )

        connection.commit()


@router.post(
    "/",
    response_model=EnrollmentResponse,
)
def enroll_device(
    request: EnrollmentRequest,
) -> EnrollmentResponse:
    initialize_database()

    device_id = str(uuid.uuid4())

    enrolled_at = datetime.now(
        timezone.utc
    ).isoformat()

    with sqlite3.connect(DATABASE_PATH) as connection:
        connection.execute(
            """
            INSERT INTO devices (
                device_id,
                hostname,
                platform,
                enrolled_at
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                device_id,
                request.hostname,
                request.platform,
                enrolled_at,
            ),
        )

        connection.commit()

    record_event(
        "device_enrolled",
        device_id,
        request.hostname,
    )

    return EnrollmentResponse(
        device_id=device_id,
        enrolled=True,
    )