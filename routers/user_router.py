from fastapi import APIRouter, Depends

from schemas.user_schema import UserCreateRequest
from services.user_service import UserService
from dependencies.user_dependencies import get_user_service

router = APIRouter()


@router.post("/register")
def register_user(
    user: UserCreateRequest,
    user_service: UserService = Depends(get_user_service)
):

    return user_service.register_user(user)
