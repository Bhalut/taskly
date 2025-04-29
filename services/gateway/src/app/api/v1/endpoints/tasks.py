from fastapi import APIRouter, Depends
from src.app.core.security import verify_token

router = APIRouter()


@router.get("/tasks")
async def list_tasks(payload: dict = Depends(verify_token)):
    return {"message": f"Here are your tasks, user_id={payload.get('sub')}"}
