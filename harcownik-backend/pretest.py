import logging

from src.db.init_db import init_badges, init_users
from src.db.init_test_db import init_test_groups, init_test_users
from src.db.db import SessionLocal

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)

def init() -> None:
    db = SessionLocal()
    try:
        init_badges(db)
        logger.info("Badges data has been successfully injected")

        init_users(db)
        logger.info("Users data has been successfully injected")

        init_test_groups(db)
        logger.info("Test groups data has been successfully injected")

        init_test_users(db)
        logger.info("Test users data has been successfully injected")
    except Exception as e:
        logger.error("A error occured during data injection", e)

def main() -> None:
    logger.info("Creating initial data...")
    try:
        init()
        logger.info("Initial data successfully created")
    except:
        logger.error("Initial data has not successfully created")

if __name__ == '__main__':
    main()