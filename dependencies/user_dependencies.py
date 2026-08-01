from repositories.user_repository import UserRepository
from services.user_service import UserService


def get_user_service():

    user_repository = UserRepository()

    user_service = UserService(user_repository)

    return user_service