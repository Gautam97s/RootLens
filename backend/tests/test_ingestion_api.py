def test_ingest_log_single(client):
    payload = {
        "timestamp": "2026-03-29T10:00:00Z",
        "service": "auth-service",
        "level": "ERROR",
        "message": "DB timeout",
        "trace_id": "trace-001",
    }

    response = client.post("/ingest-log", json=payload)

    assert response.status_code == 201
    body = response.json()
    assert body["id"] > 0
    assert body["service"] == "auth-service"
    assert body["level"] == "ERROR"


def test_ingest_logs_bulk(client):
    payload = [
        {
            "timestamp": "2026-03-29T10:00:01Z",
            "service": "api-gateway",
            "level": "WARNING",
            "message": "Upstream slow",
            "trace_id": "trace-001",
        },
        {
            "timestamp": "2026-03-29T10:00:02Z",
            "service": "billing-service",
            "level": "ERROR",
            "message": "Payment provider failure",
            "trace_id": "trace-002",
        },
    ]

    response = client.post("/ingest-logs", json=payload)

    assert response.status_code == 201
    body = response.json()
    assert len(body) == 2
    assert body[0]["id"] > 0
    assert body[1]["id"] > body[0]["id"]


def test_ingest_log_validation_error(client):
    # Missing required fields should fail schema validation.
    payload = {
        "service": "auth-service",
        "level": "ERROR",
    }

    response = client.post("/ingest-log", json=payload)

    assert response.status_code == 422
