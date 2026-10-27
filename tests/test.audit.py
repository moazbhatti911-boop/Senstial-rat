from server.audit import record_event


def test_audit_event():
    record_event(
        "test_event",
        device_id="test-device",
        details="pytest",
    )