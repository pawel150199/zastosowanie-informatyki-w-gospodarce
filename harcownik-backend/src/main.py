from pydoc import describe
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .db import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.CreateUser, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)
    
@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
       raise HTTPException(status_code=404, detail="User not found")
    return db_user 

@app.post("/badges", response_model=schemas.Badge)
def create_badge(badge: schemas.CreateBadge, db:Session = Depends(get_db)):
    return crud.create_badge(db=db, badge=badge)

@app.get("/badges/{badge_id}", response_model=schemas.Badge)
def read_badge(badge_id: int, db: Session = Depends(get_db)):
    db_badge = crud.get_badge(db, badge_id=badge_id)
    if db_badge is None:
        raise HTTPException(status_code=404, detail="Badge not found")
    return db_badge