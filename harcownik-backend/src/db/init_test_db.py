from sqlalchemy.orm import Session
from src import crud, schemas




def init_test_groups(db: Session) -> None:
    groups = [
        schemas.CreateGroup(
            name="Test", number=10, szczep="Test Group", city="Test"
        )
    ]

    for group in groups:
        crud.create_group(db, group=group)


def init_test_users(db: Session) -> None:
    users = [
        schemas.CreateUser(
            first_name="webadmin_test",
            last_name="test",
            email="webadmin_test@harcownik.com",
            is_webadmin=True,
            level="webadmin",
            function="webadmin",
            password="zaq12wsx",
        ),
        schemas.CreateUser(
            first_name="teamadmin_test",
            last_name="test",
            email="teamadmin_test@harcownik.com",
            is_teamadmin=True,
            level="webadmin",
            function="webadmin",
            password="zaq12wsx",
        ),
        schemas.CreateUser(
            first_name="test",
            last_name="test",
            email="test@harcownik.com",
            level="test",
            function="test",
            password="zaq12wsx",
        )
    ]

    for user in users:
        crud.create_user(db, user=user)
