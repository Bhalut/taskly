from fastapi import FastAPI
from slowapi.errors import RateLimitExceeded
from src.app.api.v1.router import router as api_router
from src.app.core.rate_limiter import limiter, rate_limit_exceeded_handler

app = FastAPI(title="Taskly Gateway", openapi_url="/openapi.json")

app.state.limiter = limiter

app.add_exception_handler(RateLimitExceeded, rate_limit_exceeded_handler)

app.include_router(api_router, prefix="/api/v1")
