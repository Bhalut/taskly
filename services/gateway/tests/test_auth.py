import pytest
from httpx import AsyncClient
from app.main import app


@pytest.mark.asyncio
async def test_register_and_login():
    async with AsyncClient(app=app, base_url="http://testserver") as ac:
        register_data = {
            "username": "gatewayuser",
            "email": "gatewayuser@example.com",
            "password": "strongpass123",
        }
        reg_resp = await ac.post("/api/v1/auth/register", json=register_data)
        assert reg_resp.status_code == 201
        assert reg_resp.json()["email"] == register_data["email"]

        login_data = {
            "email": "gatewayuser@example.com",
            "password": "strongpass123",
        }
        login_resp = await ac.post("/api/v1/auth/login", json=login_data)
        assert login_resp.status_code == 200
        assert "access" in login_resp.json()
        assert "refresh" in login_resp.json()
