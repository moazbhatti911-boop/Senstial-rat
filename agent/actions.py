def run_local_action(action: str) -> dict:
    allowed_actions = {
        "health_check": "Client is operational.",
        "collect_status": "Status collection is available.",
    }

    message = allowed_actions.get(action)

    if message is None:
        return {
            "success": False,
            "message": "Action not permitted.",
        }

    return {
        "success": True,
        "message": message,
    }