def test_get_logs_with_filters(client):
    payload = [
        {
            "timestamp": "2026-03-29T10:00:00Z",
            "service": "query-svc-a",
            "level": "ERROR",
            "message": "match me",
            "trace_id": "q-1",
        },
        {
            "timestamp": "2026-03-29T10:00:05Z",
            "service": "query-svc-a",
            "level": "INFO",
            "message": "ignore by level",
            "trace_id": "q-2",
        },
        {
            "timestamp": "2026-03-29T10:00:10Z",
            "service": "query-svc-b",
            "level": "ERROR",
            "message": "ignore by service",
            "trace_id": "q-3",
        },
    ]
    client.post("/ingest-logs", json=payload)

    response = client.get(
        "/logs",
        params={
            "start_time": "2026-03-29T09:59:00Z",
            "end_time": "2026-03-29T10:00:02Z",
            "service": "query-svc-a",
            "level": "ERROR",
            "limit": 10,
            "offset": 0,
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["total"] == 1
    assert body["limit"] == 10
    assert body["offset"] == 0
    assert len(body["items"]) == 1
    assert body["items"][0]["message"] == "match me"


def test_get_logs_pagination(client):
    payload = [
        {
            "timestamp": "2026-03-29T10:00:00Z",
            "service": "page-svc",
            "level": "ERROR",
            "message": "m1",
            "trace_id": "p-1",
        },
        {
            "timestamp": "2026-03-29T10:00:01Z",
            "service": "page-svc",
            "level": "ERROR",
            "message": "m2",
            "trace_id": "p-2",
        },
        {
            "timestamp": "2026-03-29T10:00:02Z",
            "service": "page-svc",
            "level": "ERROR",
            "message": "m3",
            "trace_id": "p-3",
        },
    ]
    client.post("/ingest-logs", json=payload)

    response = client.get(
        "/logs",
        params={"service": "page-svc", "limit": 2, "offset": 1},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["total"] == 3
    assert len(body["items"]) == 2
    # Ordered by timestamp desc, then paginated with offset 1.
    assert body["items"][0]["message"] == "m2"
    assert body["items"][1]["message"] == "m1"
