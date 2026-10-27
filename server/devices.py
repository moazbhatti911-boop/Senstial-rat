import sqlite3

from fastapi import APIRouter, Depends
from fastapi import APIRouter, Depends, HTTPException

from server.auth import require_api_key
from server.config import DATABASE_PATH

router = APIRouter(
    prefix="/devices",
    tags=["Devices"],
    dependencies=[Depends(require_api_key)],
)


@router.get("/")
def list_devices() -> list[dict]:
    with sqlite3.connect(DATABASE_PATH) as connection:
        connection.row_factory = sqlite3.Row

        rows = connection.execute(
            """
            SELECT
                device_id,
                hostname,
                platform,
                enrolled_at,
                last_seen
            FROM devices
            ORDER BY enrolled_at DESC
            """
        ).fetchall()

    return [dict(row) for row in rows]


@router.get("/{device_id}")
def get_device(device_id: str) -> dict:
    with sqlite3.connect(DATABASE_PATH) as connection:
        connection.row_factory = sqlite3.Row

        row = connection.execute(
            """
            SELECT
                device_id,
                hostname,
                platform,
                enrolled_at,
                last_seen
            FROM devices
            WHERE device_id = ?
            """,
            (device_id,),
        ).fetchone()

    if row is None:
        raise HTTPException(
            status_code=404,
            detail="Device not found",
        )

    return dict(row)