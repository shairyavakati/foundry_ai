from base_repository import BaseRepository
from sqlalchemy.orm import Session
from models import User 

class UserRepository(BaseRepository):
    def __init__(self, db: Session):
        super().__init__(db, User)
    def find_by_email(self, email: str) -> User | None:
        return (
    self.db
        .query(self.model)
        .filter(self.model.email == email)
        .first()
)   
    
    