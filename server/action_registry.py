from fastapi import APIRouter, Depends, HTTPException

from server.auth import require_api_key
from server.audit import record_event
from shared.schemas import ActionRequest, ActionResult

router = APIRouter(
    prefix="/actions",
    tags=["Actions"],
    dependencies=[Depends(require_api_key)],
)


ALLOWED_ACTIONS = {
    "health_check": "The server is operational.",
    "collect_status": "Status collection is available.",
}


@router.post("/", response_model=ActionResult)
def execute_action(
    request: ActionRequest,
) -> ActionResult:
    message = ALLOWED_ACTIONS.get(request.action)

    if message is None:
        raise HTTPException(
            status_code=400,
            detail="Action is not allowlisted",
        )

    record_event(
        "action_requested",
        details=request.action,
    )

    return ActionResult(
        action=request.action,
        success=True,
        message=message,
    )