from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import relationship

from app.database import dal


class DepartmentAssociations(dal.Base):
    __tablename__ = "department_associations"

    email = Column(
        "email", String, ForeignKey("faculty.email"), primary_key=True, nullable=False,
    )
    faculty = relationship("Faculty")
    department_id = Column(
        "department_id",
        Integer,
        ForeignKey("department.department_id"),
        primary_key=True,
        nullable=False,
    )
    department = relationship("Department")

    def __repr__(self):
        return (
            f"<department_associations(email={self.email},"
            f"department_id={self.department_id}, "
        )
