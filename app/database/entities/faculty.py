from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.database import dal


class Faculty(dal.Base):
    __tablename__ = "Faculty"

    faculty_id = Column("FacultyId", Integer, primary_key=True, autoincrement=True)
    name = Column("Name", String, nullable=False)
    email = Column("Email", String, nullable=False)
    phone = Column("Phone", String, nullable=False)
    department = Column("Department", String, nullable=False)

    def __repr__(self):
        return (
            f"<Faculty(id={self.faculty_id}, "
            f"name={self.name}, "
            f"email={self.email}, "
            f"phone={self.phone}, "
            f"department={self.department}, "
        )
