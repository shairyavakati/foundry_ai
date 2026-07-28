from base_repository import BaseRepository
from sqlalchemy.orm import Session
from models import User

class UserRepository(BaseRepository):
    def __init__(self, db: Session):
        super().__init__(db, User)