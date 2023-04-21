from sqlalchemy.orm import Session

from src import crud, schemas
from src.core.settings import settings


def init_db(db: Session) -> None:

    badges = [
        schemas.CreateBadge(name="Sprinter", description="Szybki musisz być", group="Sportowe"),
        schemas.CreateBadge(name="Powolniak", description="Wolny musisz być", group="Sportowe"),
        schemas.CreateBadge(name="Buszmen", description="Musisz spędzić tydzień w krzakach", group="Leśne"),
        schemas.CreateBadge(name="Tarzan", description="Musisz spędzić dzień w krzakach", group="Leśne"),
    ]

    for badge in badges:
        crud.create_badge(db, badge=badge)
