import logging
from tenacity import after_log, before_log, retry, stop_after_attempt, wait_fixed
from src.db.db import SessionLocal

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)

max_tries = 60 * 5
wait_seconds = 1

@retry(
    stop=stop_after_attempt(max_tries),
    wait=wait_fixed(wait_seconds),
    before=before_log(logger, logging.INFO),
    after=after_log(logger, logging.WARN),
)
def init() -> None:
    try:
        db = SessionLocal()
        db.execute("SELECT 1")
    except Exception as e:
        logger.error(e)
        raise e
    
def main() -> None:
    logger.info("Initializating service")
    init()
    logger.info("Service finished initialization")

if __name__ == '__main__':
    main()            