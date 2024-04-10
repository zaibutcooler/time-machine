from fastapi import APIRouter, HTTPException
from models.user import User

router = APIRouter()

@router.get("/users/{user_id}/", response_model=User)
async def read_user(user_id: int):
    
    
    user = User(username="example", email="example@example.com", password="*********")
    return user
