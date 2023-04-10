from sqlalchemy.orm import Session

from src import crud, schemas
from src.core.settings import settings
from src.db.db import Base, engine

def init_db(db: Session) -> None:
    Base.metadata.create_all(bind=engine)