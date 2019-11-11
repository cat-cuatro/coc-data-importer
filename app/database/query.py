from app.database import dal
from app.database.entities import Faculty


def faculty_count():
    return dal.DBSession.query(Faculty).count()


def faculty_names():
    return [faculty.name for faculty in dal.DBSession.query(Faculty).all()]
