from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from app.database import dal


class Faculty(dal.Base):
    __tablename__ = "faculty"

    faculty_id = Column("faculty_id", Integer, primary_key=True, autoincrement=True)
    full_name = Column("full_name", String, nullable=False)
    job_title = Column("job_title", String, nullable=False)
    senate_division = Column("senate_division", String, nullable=False)
    department_id = Column(
        "department_id", Integer, ForeignKey("department.department_id"), nullable=False
    )
    department = relationship("Department")

    def __repr__(self):
        return (
            f"<faculty(id={self.faculty_id}, "
            f"full_name={self.full_name}, "
            f"job_title={self.job_title}, "
            f"senate_division={self.senate_division}, "
            f"department_id={self.department_id}, "
        )
