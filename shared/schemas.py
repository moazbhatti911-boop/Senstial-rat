from datetime import datetime, timezone
from typing import Literal

from pydantic import BaseModel, Field


class EnrollmentRequest(BaseModel):
    hostname: str = Field(min_length=1, max_length=255)
    platform: str = Field(min_length=1, max_length=100)


class EnrollmentResponse(BaseModel):
    device_id: str
    enrolled: bool


class TelemetryReport(BaseModel):
    hostname: str = Field(min_length=1, max_length=255)
    platform: str = Field(min_length=1, max_length=100)
    cpu_percent: float = Field(ge=0, le=100)
    memory_percent: float = Field(ge=0, le=100)
    reported_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )


class DeviceRecord(BaseModel):
    device_id: str
    hostname: str
    platform: str
    enrolled_at: datetime
    last_seen: datetime | None = None


class ActionRequest(BaseModel):
    action: Literal["health_check", "collect_status"]


class ActionResult(BaseModel):
    action: str
    success: bool
    message: str