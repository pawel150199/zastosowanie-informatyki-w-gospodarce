from pydoc import describe
import re
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

# User
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.CreateUser, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)
    
@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
       raise HTTPException(status_code=404, detail="User not found")
    return db_user 

# Badge
@app.post("/badges", response_model=schemas.Badge)
def create_badge(badge: schemas.CreateBadge, db:Session = Depends(get_db)):
    return crud.create_badge(db=db, badge=badge)

@app.get("/badges/{badge_id}", response_model=schemas.Badge)
def read_badge(badge_id: int, db: Session = Depends(get_db)):
    db_badge = crud.get_badge(db, badge_id=badge_id)
    if db_badge is None:
        raise HTTPException(status_code=404, detail="Badge not found")
    return db_badge

# Group
@app.post("/groups", response_model=schemas.Group)
def create_group(group: schemas.CreateGroup, db:Session = Depends(get_db)):
    return crud.create_group(db=db, group=group)

@app.get("/groups/{group_id}", response_model=schemas.Group)
def read_group(group_id: int, db: Session = Depends(get_db)):
    db_group = crud.get_group(db, group_id=group_id)
    if db_group is None:
        raise HTTPException(status_code=404, detail="Group not found")
    return db_group

# BadgeReport
@app.post("/badge_reports", response_model=schemas.BadgeReport)
def create_badge_report(badge_report: schemas.CreateBadgeReport, db:Session = Depends(get_db)):
    return crud.create_badge_report(db=db, badge_report=badge_report)

@app.get("/badge_reports/{badge_report_id}", response_model=schemas.BadgeReport)
def read_group(badge_report_id: int, db: Session = Depends(get_db)):
    db_badge_report = crud.get_badge_report(db, badge_report_id=badge_report_id)
    if db_badge_report is None:
        raise HTTPException(status_code=404, detail="Report not found")
    return db_badge_report

# LevelReport
@app.post("/level_reports", response_model=schemas.LevelReport)
def create_badge_report(level_report: schemas.CreateLevelReport, db:Session = Depends(get_db)):
    return crud.create_level_report(db=db, level_report=level_report)

@app.get("/level_reports/{level_report_id}", response_model=schemas.LevelReport)
def read_group(level_report_id: int, db: Session = Depends(get_db)):
    db_level_report = crud.get_level_report(db=db, level_report_id=level_report_id)
    if db_level_report is None:
        raise HTTPException(status_code=404, detail="Report not found")
    return db_level_report
