from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from app.database import dal


class SurveyChoice(dal.Base):
    __tablename__ = "survey_choice"

    survey_date = Column("survey_date", DateTime, ForeignKey("survey_data.survey_date"), primary_key=True)
    survey_data = relationship("SurveyData")
    email = Column("email", String, ForeignKey("faculty.email"), primary_key=True)
    faculty = relationship("Faculty")
    committee_id = Column("committee_id", Integer, ForeignKey("committee.committee_id"), primary_key=True)
    committee = relationship("Committee")
    choice_id = Column("choice_id", Integer, primary_key=True)

    def __repr__(self):
        return (
            f"<survey_choice(survey_date={self.survey_date}, "
            f"email={self.email}, "
            f"committee_id={self.committee_id}, "
            f"choice_id={self.choice_id}, "
        )
