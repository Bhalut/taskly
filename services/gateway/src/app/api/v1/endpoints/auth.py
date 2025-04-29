import httpx
from fastapi import APIRouter, HTTPException, Request
from src.app.core.config import settings
from src.app.core.rate_limiter import limiter

router = APIRouter()


@router.post("/auth/register")
@limiter.limit("5/minute")
async def register_user(request: Request, data: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{settings.USERS_SERVICE_URL}/register/",
            json=data
        )
        if response.status_code != 201:
            raise HTTPException(
                status_code=response.status_code,
                detail=response.json()
            )
        return response.json()


@router.post("/auth/login")
@limiter.limit("10/minute")
async def login_user(request: Request, data: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{settings.USERS_SERVICE_URL}/login/",
            json=data
        )
        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail=response.json()
            )
        return response.json()


@router.post("/auth/refresh")
async def refresh_token(data: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{settings.USERS_SERVICE_URL}/refresh/",
            json=data
        )
        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail=response.json()
            )
        return response.json()


@router.post("/auth/logout")
async def logout():
    return {
        "message": "Logout successful. Please delete tokens on client side."
    }
