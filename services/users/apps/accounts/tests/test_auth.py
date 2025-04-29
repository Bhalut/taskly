import pytest
from rest_framework.test import APIClient

pytestmark = pytest.mark.django_db

client = APIClient()


def test_register_user():
    payload = {
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "strongpassword123",
    }
    response = client.post("/api/v1/auth/register/", payload)
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == payload["email"]


def test_login_user():
    # Register first
    client.post(
        "/api/v1/auth/register/",
        {
            "username": "testuser2",
            "email": "testuser2@example.com",
            "password": "strongpassword123",
        },
    )

    # Then login
    response = client.post(
        "/api/v1/auth/login/",
        {
            "email": "testuser2@example.com",
            "password": "strongpassword123",
        },
    )
    assert response.status_code == 200
    assert "access" in response.json()
    assert "refresh" in response.json()
