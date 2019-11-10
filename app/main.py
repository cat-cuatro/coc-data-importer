import pandas as pd

from app import settings
from app.database import dal
from app.database import query


def run():
    """Entry point for the application.

    Loads CSV faculty data and stores it into a database.

    :return: Count of faculty members and list of faculty names
    """
    dal.db_init()
    df = pd.read_csv(settings.DATA_CSV)
    df.to_sql("Faculty", con=dal.engine, index_label="FacultyId", if_exists="replace")

    faculty_count = query.faculty_count()
    faculty_names = query.faculty_names()

    dal.DBSession.close()
    return faculty_count, faculty_names
