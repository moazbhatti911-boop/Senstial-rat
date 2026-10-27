import platform
import socket
import uuid


def get_device_identity() -> dict:
    return {
        "hostname": socket.gethostname(),
        "platform": platform.system(),
    }


def get_local_instance_id() -> str:
    return str(uuid.uuid4())