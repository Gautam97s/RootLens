import os
from uuid import uuid4

import pytest
from fastapi.testclient import TestClient

# Ensure test database URL is set before importing app modules.
os.environ["DATABASE_URL"] = f"sqlite+aiosqlite:///./test_rootlens_{uuid4().hex}.db"

from app.main import app


@pytest.fixture(scope="function")
def client():
    with TestClient(app) as test_client:
        yield test_client
