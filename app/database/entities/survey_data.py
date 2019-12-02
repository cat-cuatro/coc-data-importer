from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from app.database import dal


class SurveyData(dal.Base):
    __tablename__ = "survey_data"

    survey_date = Column("survey_date", DateTime, primary_key=True)
    faculty_id = Column(
        "faculty_id", Integer, ForeignKey("faculty.faculty_id"), primary_key=True
    )
    faculty = relationship("Faculty")
    is_interested = Column("is_interested", Boolean, nullable=False)
    expertise = Column("expertise", String)

    def __repr__(self):
        return (
            f"<survey_data(survey_date={self.survey_date}, "
            f"faculty_id={self.faculty_id}, "
            f"is_interested={self.is_interested}, "
            f"expertise={self.expertise}, "
        )
