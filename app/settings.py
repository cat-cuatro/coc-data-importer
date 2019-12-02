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


DATABASE_DRIVER = os.environ.get("DATABASE_DRIVER", "sqlite")
DATABASE_PATH = os.environ.get("DATABASE_PATH", ":memory:")
DATA_XLSX = os.environ.get("DATA_CSV", "data/survey.xlsx")
LOGGING_LEVEL = map_logging_level(os.environ.get("LOGGING_LEVEL", "debug"))
PROJECT_DIR = os.path.abspath(os.curdir)
