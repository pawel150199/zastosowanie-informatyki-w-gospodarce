from sqlalchemy.orm import Session

from src import crud, schemas
from src.core.settings import settings


def init_badges(db: Session) -> None:

    badges = [
        schemas.CreateBadge(name="Sprinter", description="Szybki musisz być", group="Sportowe"),
        schemas.CreateBadge(name="Powolniak", description="Wolny musisz być", group="Sportowe"),
        schemas.CreateBadge(name="Buszmen", description="Musisz spędzić tydzień w krzakach", group="Leśne"),
        schemas.CreateBadge(name="Tarzan", description="Musisz spędzić dzień w krzakach", group="Leśne"),
    ]

    for badge in badges:
        crud.create_badge(db, badge=badge)


def init_groups(db: Session) -> None:
    groups = [
        schemas.CreateGroup(name="Forward", number="7", szczep="Zielona Siódemka", city="Bydgoszcz")
    ]

    for group in groups:
        crud.create_group(db, group=group)
        

def init_users(db: Session) -> None:
    users = [
        schemas.CreateUser(
            first_name="admin",
            last_name="admin",
            email="admin@harcownik.com",
            level="admin", function="admin",
            password="admin",
            group_id=1,
            badge_id=3
        )
    ]

    for user in users:
        crud.create_user(db, user=user)