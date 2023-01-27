from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.attributes import flag_modified

from app.src.db.database import SessionLocal


def get_db():
    db: sessionmaker = SessionLocal()
    try:
        yield db
    finally:
        db.close_all()

def update_jsonb(model: object, key: str, db) -> None:
    if isinstance(model, list):
        [(flag_modified(_object, key), db.merge(_object)) for _object in model]
    else:
        flag_modified(model, key)
        db.merge(model)
    db.flush()
    db.commit()