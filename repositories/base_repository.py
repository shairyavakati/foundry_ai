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
        except Exception :
            self.db.rollback()
            raise

    def get_by_id(self, id: int):
        query = self.db.query(self.model)
        record = query.filter(self.model.id == id).first()
        return record
    def update(self, id: int, data: dict):
        record = self.get_by_id(id)
        if record is None:
            return None
        try:
            for key, value in data.items():
                setattr(record, key, value)
            self.db.commit()
            self.db.refresh(record)
            return record
        except Exception:
            self.db.rollback()
            raise
    def delete(self, id: int):
        record = self.get_by_id(id)
        if record is None:
            return None
        try:
            self.db.delete(record)
            self.db.commit()
            return record
        except Exception:
            self.db.rollback()
            raise
    def get_all(
    self,
    limit: int = 20,
    offset: int = 0,
):
        query = self.db.query(self.model)
        return query.offset(offset).limit(limit).all()
        

