from sqlalchemy import Column
from sqlalchemy import String

from app.database import dal


class SenateDivision(dal.base):
    __tablename__ = "senate_division"

    senate_division_short_name = Column(
        "senate_division_short_name", String, primary_key=True, nullable=False
    )
    name = Column("name", String)

    def __repr__(self):
        return (
            f"<senate_division(senate_division_short_name={self.senate_division_short_name}, "
            f"name={self.name}, "
        )
