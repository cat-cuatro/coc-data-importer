from app.database import dal
from app.database import store


def load(transformed):
    dal.db_init()

    for row in transformed:
        store.save_to_database(row)
