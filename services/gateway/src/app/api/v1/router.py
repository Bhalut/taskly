from fastapi import APIRouter, Request
from src.app.api.v1.endpoints import auth
from src.app.core.rate_limiter import limiter

api_router = APIRouter()

api_router.include_router(auth.router, tags=["auth"])

router = APIRouter()


@router.get("/ping")
@limiter.limit("5/minute")
async def ping(request: Request):
    return {"message": "pong"}


api_router.include_router(router)
