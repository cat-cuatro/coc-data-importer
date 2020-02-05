from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import CreateTable

from app.settings import *


class DataAccessLayer:
    # https://www.oreilly.com/library/view/essential-sqlalchemy-2nd/9781491916544/ch04.html
    Base = declarative_base()
    conn_string = (
        f"{DATABASE_DRIVER}://"
        f"{DATABASE_USER}:{DATABASE_PASSWORD}@"
        f"{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_DATABASE}"
    )
    connection = None
    engine = None
    Session = None
    DBSession = None

    def db_init(self, conn_string=None):
        self.engine = create_engine(conn_string or self.conn_string, echo=False)
        self.Base.metadata.drop_all(self.engine)
        self.Base.metadata.create_all(self.engine)

        self.Session = sessionmaker(bind=self.engine)
        self.DBSession = self.Session()

    def table_exists(self, name):
        return self.engine.dialect.has_table(self.engine, name)

    def close(self):
        if not self.Base or not self.engine:
            return

        self.Base.metadata.drop_all(self.engine)


dal = DataAccessLayer()
