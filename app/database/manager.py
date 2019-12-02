from datetime import datetime

from app.database import dal
from app.database.entities import Committee
from app.database.entities import Department
from app.database.entities import Faculty
from app.database.entities import SurveyChoice
from app.database.entities import SurveyData


class CommitteeManager:
    @staticmethod
    def add_committee(name, description=None):
        committee_record = (
            dal.DBSession.query(Committee).filter(Committee.name == name).first()
        )

        if committee_record is None:
            committee_record = Committee(name=name, description=description)
            dal.DBSession.add(committee_record)

        dal.DBSession.commit()

        return committee_record


class DepartmentManager:
    @staticmethod
    def add_department(name, description=None):
        department_record = (
            dal.DBSession.query(Department).filter(Department.name == name).first()
        )

        if department_record is None:
            department_record = Department(name=name, description=description)
            dal.DBSession.add(department_record)

        dal.DBSession.commit()

        return department_record


class FacultyManager:
    @staticmethod
    def add_faculty(full_name, email, job_title, senate_division, department_id):
        faculty_record = (
            dal.DBSession.query(Faculty).filter(Faculty.full_name == full_name).first()
        )

        if faculty_record is None:
            faculty_record = FacultyManager.create_faculty(
                full_name, email, job_title, senate_division, department_id
            )
            dal.DBSession.add(faculty_record)

        dal.DBSession.commit()

        return faculty_record

    @staticmethod
    def create_faculty(full_name, email, job_title, senate_division, department_id):
        return Faculty(
            full_name=full_name,
            email=email,
            job_title=job_title,
            senate_division=senate_division,
            department_id=department_id,
        )


class SurveyChoiceManager:
    @staticmethod
    def add_survey_choice(faculty_id, committee_id, choice_priority=None):
        survey_choice_record = (
            dal.DBSession.query(SurveyChoice)
            .filter(
                SurveyChoice.faculty_id == faculty_id,
                SurveyChoice.committee_id == committee_id,
                SurveyChoice.choice_priority == choice_priority,
            )
            .first()
        )

        if survey_choice_record is None:
            survey_choice_record = SurveyChoice(
                survey_date=datetime.now(),
                faculty_id=faculty_id,
                committee_id=committee_id,
                choice_priority=choice_priority,
            )

            dal.DBSession.add(survey_choice_record)

        return survey_choice_record

    @staticmethod
    def create_survey_choice(faculty_id, committee_id, choice_priority):
        return SurveyChoice(
            survey_date=datetime.now(),
            faculty_id=faculty_id,
            committee_id=committee_id,
            choice_priority=choice_priority,
        )


class SurveyDataManager:
    @staticmethod
    def add_survey_data(faculty_id, is_interested, expertise=None):
        survey_data_record = (
            dal.DBSession.query(SurveyData)
            .filter(SurveyData.faculty_id == faculty_id)
            .first()
        )

        if survey_data_record is None:
            survey_data_record = SurveyDataManager.create_survey_data(
                faculty_id, is_interested, expertise
            )
            dal.DBSession.add(survey_data_record)

        dal.DBSession.commit()

        return survey_data_record

    @staticmethod
    def create_survey_data(faculty_id, is_interested, expertise):
        return SurveyData(
            survey_date=datetime.now(),
            faculty_id=faculty_id,
            is_interested=is_interested,
            expertise=expertise,
        )
