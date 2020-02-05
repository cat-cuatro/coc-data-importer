from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship

from app.database import dal


class Faculty(dal.Base):
    __tablename__ = "faculty"

    full_name = Column("full_name", String, nullable=False)
    email = Column("email", String, primary_key=True)
    job_title = Column("job_title", String, nullable=False)
    senate_division_short_name = Column(
        "senate_division_short_name",
        String,
        ForeignKey("senate_division.senate_division_short_name"),
    )
    senate_division = relationship("SenateDivision")
    phone_num = Column("phone_num", String)

    def __repr__(self):
        return (
            f"<faculty(email={self.full_name}, "
            f"full_name={self.full_name}, "
            f"job_title={self.job_title}, "
            f"senate_division_short_name={self.senate_division_short_name}, "
            f"phone_num={self.phone_num}, "
        )
