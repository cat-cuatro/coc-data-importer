from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import relationship

from app.database import dal


class SurveyChoice(dal.Base):
    __tablename__ = "survey_choice"

    survey_choice_id = Column(
        "survey_choice_id", Integer, primary_key=True, autoincrement=True
    )
    survey_date = Column("survey_date", DateTime)
    faculty_id = Column("faculty_id", Integer, ForeignKey("faculty.faculty_id"))
    faculty = relationship("Faculty")
    committee_id = Column("committee_id", Integer, ForeignKey("committee.committee_id"))
    committee = relationship("Committee")
    choice_priority = Column("choice_priority", Integer)

    def __repr__(self):
        return (
            f"<survey_choice(id={self.survey_choice_id}, "
            f"survey_date={self.survey_date}, "
            f"faculty_id={self.faculty_id}, "
            f"committee_id={self.committee_id}, "
            f"choice_priority={self.choices_id}, "
        )
