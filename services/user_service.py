from exceptions import EmailAlreadyExistsException
from repositories import UserRepository
from models import User

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
    def register_user(self, user_data: dict) -> User:
        # Check if the user already exists
        existing_user = self.user_repository.find_by_email(user_data["email"])
        if existing_user:
            raise EmailAlreadyExistsException(
            "User with this email already exists"
             )
        # Create the new user
        return self.user_repository.create(user_data)