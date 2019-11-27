from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.database import dal


class Department(dal.Base):
    __tablename__ = "department"

    department_id = Column(
        "department_id", Integer, primary_key=True, autoincrement=True
    )
    name = Column("name", String, nullable=False)
    description = Column("description", String)

    def __repr__(self):
        return (
            f"<department(id={self.department_id}, "
            f"name={self.name}, "
            f"description={self.description}, "
        )
