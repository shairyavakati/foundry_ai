from fastapi import APIRouter, Depends

from app.schemas.user_schema import UserCreateRequest
from app.services.user_service import UserService

router = APIRouter()
@router.post("/register") 
def register_user(user: UserCreateRequest):
    user_service = UserService()
    return user_service.register_user(user.dict())
