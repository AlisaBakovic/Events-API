import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import create_app


def test_health_endpoint_returns_healthy_status():
    app = create_app()

    client = app.test_client()

    response = client.get("/api/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "healthy"

def test_register_user_successfully():
    app = create_app()

    client = app.test_client()

    response = client.post(
        "/api/auth/register",
        json={
            "username": "testuser999",
            "password": "mypassword123"
        }
    )

    assert response.status_code == 201

    data = response.get_json()

    assert data["message"] == "User created successfully"
    assert data["user"]["username"] == "testuser999"

def test_register_fails_when_username_missing():
    app = create_app()

    client = app.test_client()

    response = client.post(
        "/api/auth/register",
        json={
            "password": "mypassword123"
        }
    )

    assert response.status_code == 400

    data = response.get_json()

    assert data["error"] == "Username and password are required"
