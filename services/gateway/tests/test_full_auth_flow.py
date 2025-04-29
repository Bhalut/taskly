import pytest
from httpx import AsyncClient
from app.main import app


@pytest.mark.asyncio
async def test_full_auth_flow():
    async with AsyncClient(app=app, base_url="http://testserver") as ac:
        # Register user
        reg_data = {
            "username": "flowuser",
            "email": "flowuser@example.com",
            "password": "verysecure123",
        }
        reg_resp = await ac.post("/api/v1/auth/register", json=reg_data)
        assert reg_resp.status_code == 201

        # Login
        login_data = {
            "email": "flowuser@example.com",
            "password": "verysecure123",
        }
        login_resp = await ac.post("/api/v1/auth/login", json=login_data)
        assert login_resp.status_code == 200
        tokens = login_resp.json()
        access_token = tokens["access"]
        refresh_token = tokens["refresh"]

        # Access tasks with token
        headers = {"Authorization": f"Bearer {access_token}"}
        tasks_resp = await ac.get("/api/v1/tasks", headers=headers)
        assert tasks_resp.status_code == 200

        # Simulate expiration (or use refresh)
        refresh_resp = await ac.post(
            "/api/v1/auth/refresh", json={"refresh": refresh_token}
        )
        assert refresh_resp.status_code == 200
        new_access_token = refresh_resp.json()["access"]

        # Access tasks with new token
        new_headers = {"Authorization": f"Bearer {new_access_token}"}
        tasks_resp2 = await ac.get("/api/v1/tasks", headers=new_headers)
        assert tasks_resp2.status_code == 200
