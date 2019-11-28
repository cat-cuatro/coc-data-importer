import logging

from app import settings

logging.basicConfig(level=settings.LOGGING_LEVEL, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)
