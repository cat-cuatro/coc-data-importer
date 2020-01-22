from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.database import dal


class Committee(dal.Base):
    __tablename__ = "committee"

    committee_id = Column("committee_id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String, nullable=False)
    description = Column("description", String)
    total_slots = Column("total_slots", Integer)

    def __repr__(self):
        return (
            f"<committee(id={self.committee_id}, "
            f"name={self.name}, "
            f"description={self.description}, "
            f"total_slots={self.total_slots}"
        )
