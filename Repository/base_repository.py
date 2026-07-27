# Generic CRUD operations for all database models
from sqlalchemy.orm import Session


class BaseRepository:
    def __init__(self, db: Session, model):
        self.db = db
        self.model = model

    def create(self, data: dict):
        try:
            new_record = self.model(**data)
            self.db.add(new_record)
            self.db.commit()
            self.db.refresh(new_record)
            return new_record
        except Exception:
            self.db.rollback()
            raise
