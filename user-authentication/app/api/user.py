from fastapi import APIRouter, HTTPException
from app.models.user import User

router = APIRouter()


@router.get("/users/{user_id}/", response_model=User)
async def read_user(user_id: int):
    # Placeholder logic to retrieve user by ID
    # Replace this with actual user retrieval logic (e.g., database operation)
    user = User(username="example", email="example@example.com", password="*********")
    return user
