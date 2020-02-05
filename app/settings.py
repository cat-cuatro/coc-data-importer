import os

from dotenv import load_dotenv

load_dotenv()


def map_logging_level(level):
    """ Maps the textual representation of a logging level to the number that
    matches the internal requirements of the logger

    :param level: Logging level to map
    :return:      Mapped logging level
    """
    return {"critical": 50, "error": 40, "warning": 30, "info": 20, "debug": 10}.get(
        level, 10
    )


DATABASE_DATABASE = os.environ.get("DATABASE_DATABASE", "coc")
DATABASE_DRIVER = os.environ.get("DATABASE_DRIVER", "postgresql+pg8000")
DATABASE_HOST = os.environ.get("DATABASE_HOST", "localhost")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD", "pwd123")
DATABASE_PATH = os.environ.get("DATABASE_PATH", ":memory:")
DATABASE_PORT = os.environ.get("DATABASE_PORT", "54320")
DATABASE_USER = os.environ.get("DATABASE_USER", "coc")
DATA_XLSX = os.environ.get("DATA_CSV", "data/survey.xlsx")
LOGGING_LEVEL = map_logging_level(os.environ.get("LOGGING_LEVEL", "debug"))
PROJECT_DIR = os.path.abspath(os.curdir)
