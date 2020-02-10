from sqlalchemy import Date
from sqlalchemy import Column, PrimaryKeyConstraint, ForeignKeyConstraint
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from app.database import dal


class SurveyChoice(dal.Base):
    __tablename__ = "survey_choice"
    __table_args__ = (
        PrimaryKeyConstraint(
            "choice_id",
            "email",
            "survey_date",
            "committee_id",
            name="survey_choice_pkey",
        ),
        ForeignKeyConstraint(
            ["email"], ["faculty.email"], name="survey_choice_email_foreign"
        ),
        ForeignKeyConstraint(
            ["committee_id"],
            ["committee.committee_id"],
            name="survey_choice_committee_id_foreign",
        ),
    )

    choice_id = Column("choice_id", Integer)
    survey_date = Column("survey_date", Date)
    email = Column("email", String(255))
    committee_id = Column("committee_id", Integer)

    def __repr__(self):
        return (
            f"<survey_choice(survey_date={self.survey_date}, "
            f"email={self.email}, "
            f"committee_id={self.committee_id}, "
            f"choice_id={self.choice_id}, "
        )
