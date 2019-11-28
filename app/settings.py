import os

from dotenv import load_dotenv

load_dotenv()

DATABASE_DRIVER = os.environ.get("DATABASE_DRIVER", "sqlite")
DATABASE_PATH = os.environ.get("DATABASE_PATH", ":memory:")
DATA_CSV = os.environ.get("DATA_CSV", "data/faculty.csv")
DATA_XLSX = os.environ.get("DATA_CSV", "data/survey.xlsx")
PROJECT_DIR = os.path.abspath(os.curdir)
