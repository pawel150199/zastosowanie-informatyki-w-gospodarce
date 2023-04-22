import logging

from src.db.db_init import init_db
from src.db.db import SessionLocal

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def init() -> None:
    db = SessionLocal()
    init_db(db)

def main() -> None:
    logger.info("Creating initial data...")
    init()
    logger.info("Initial data successfully created")

if __name__ == '__main__':
    main()
