import unittest

from app.database import dal
from app.database import store
from app.database.entities import Committee
from app.database.entities import Department
from app.database.entities import Faculty
from app.database.entities import SurveyChoice
from app.database.entities import SurveyData
from app.database.entities import SenateDivision
from app.database.entities import DepartmentAssociations


class TestDatabaseStore(unittest.TestCase):
    def setUp(self):
        dal.db_init("sqlite:///:memory:")

    def tearDown(self):
        dal.close()

    def test_save_to_database_saves_committee_data_to_database(self):
        data = {
            "committee_preferred": "test-committee-preferred",
            "choice": 1,
            "email": "johndoe@mail.com",
            "name": "John Doe",
            "senate_division": "test-senate-division",
            "department": "test-department",
            "job_title": "test-job-title",
            "is_interested": True,
            "expertise": None,
        }

        store.save_to_database(data)

        committee_query = dal.DBSession.query(Committee).filter(
            Committee.name == "test-committee-preferred"
        )

        committee_record = committee_query.first()
        assert committee_query.count() == 1
        assert committee_record.name == "test-committee-preferred"
        assert committee_record.description is None

    def test_save_to_database_saves_department_data_to_database(self):
        data = {
            "committee_preferred": "test-committee-preferred",
            "choice": 1,
            "email": "johndoe@mail.com",
            "name": "John Doe",
            "senate_division": "test-senate-division",
            "department": "test-department",
            "job_title": "test-job-title",
            "is_interested": True,
            "expertise": None,
        }

        store.save_to_database(data)

        department_query = dal.DBSession.query(Department).filter(
            Department.name == "test-department"
        )

        department_record = department_query.first()
        assert department_query.count() == 1
        assert department_record.name == "test-department"
        assert department_record.description is None

    def test_save_to_database_saves_faculty_data_to_database(self):
        data = {
            "committee_preferred": "test-committee-preferred",
            "choice": 1,
            "email": "johndoe@mail.com",
            "name": "John Doe",
            "senate_division": "test-senate-division",
            "department": "test-department",
            "job_title": "test-job-title",
            "is_interested": True,
            "expertise": None,
        }

        store.save_to_database(data)

        faculty_query = dal.DBSession.query(Faculty).filter(
            Faculty.full_name == "John Doe"
        )

        faculty_record = faculty_query.first()
        assert faculty_query.count() == 1
        assert faculty_record.full_name == "John Doe"
        assert faculty_record.job_title == "test-job-title"
        assert faculty_record.senate_division_short_name == "test-senate-division"

    def test_save_to_database_saves_survey_choice_data_to_database(self):
        data = {
            "committee_preferred": "test-committee-preferred",
            "choice": 1,
            "email": "johndoe@mail.com",
            "name": "John Doe",
            "senate_division": "test-senate-division",
            "department": "test-department",
            "job_title": "test-job-title",
            "is_interested": True,
            "expertise": None,
        }

        store.save_to_database(data)

        committee_query = dal.DBSession.query(Committee).filter(
            Committee.name == "test-committee-preferred"
        )
        committee_record = committee_query.first()
        committee_id = committee_record.committee_id
        faculty_query = dal.DBSession.query(Faculty).filter(
            Faculty.full_name == "John Doe"
        )
        faculty_record = faculty_query.first()
        email = faculty_record.email
        survey_choice_query = dal.DBSession.query(SurveyChoice).filter(
            SurveyChoice.email == email, SurveyChoice.committee_id == committee_id,
        )

        survey_choice_record = survey_choice_query.first()
        assert survey_choice_query.count() == 1
        assert survey_choice_record.email == "johndoe@mail.com"
        assert survey_choice_record.committee_id == 1
        assert survey_choice_record.choice_id is 1

    def test_save_to_database_saves_survey_data_data_to_database(self):
        data = {
            "committee_preferred": "test-committee-preferred",
            "choice": 1,
            "email": "johndoe@mail.com",
            "name": "John Doe",
            "senate_division": "test-senate-division",
            "department": "test-department",
            "job_title": "test-job-title",
            "is_interested": True,
            "expertise": None,
        }

        store.save_to_database(data)

        faculty_query = dal.DBSession.query(Faculty).filter(
            Faculty.full_name == "John Doe"
        )
        faculty_record = faculty_query.first()
        survey_data_query = dal.DBSession.query(SurveyData).filter(
            SurveyData.email == faculty_record.email
        )
        survey_data_record = survey_data_query.first()
        assert faculty_query.count() == 1
        assert survey_data_query.count() == 1
        assert survey_data_record.email == "johndoe@mail.com"
        assert survey_data_record.is_interested is True
        assert survey_data_record.expertise is None

    def test_save_to_database_saves_survey_data_data_to_database_with_expertise(self):
        data = {
            "committee_preferred": "test-committee-preferred",
            "choice": 1,
            "email": "johndoe@mail.com",
            "name": "John Doe",
            "senate_division": "test-senate-division",
            "department": "test-department",
            "job_title": "test-job-title",
            "is_interested": True,
            "expertise": "test-expertise",
        }

        store.save_to_database(data)

        faculty_query = dal.DBSession.query(Faculty).filter(
            Faculty.full_name == "John Doe"
        )
        faculty_record = faculty_query.first()
        survey_data_query = dal.DBSession.query(SurveyData).filter(
            SurveyData.email == faculty_record.email
        )
        survey_data_record = survey_data_query.first()
        assert survey_data_query.count() == 1
        assert survey_data_record.email == "johndoe@mail.com"
        assert survey_data_record.is_interested is True
        assert survey_data_record.expertise == "test-expertise"

    def test_save_to_database_saves_senate_division_with_short_name(self):
        data = {
            "committee_preferred": "test-committee-preferred",
            "choice": 1,
            "email": "johndoe@mail.com",
            "name": "John Doe",
            "senate_division": "test-senate-division",
            "department": "test-department",
            "job_title": "test-job-title",
            "is_interested": True,
            "expertise": "test-expertise",
        }

        store.save_to_database(data)

        senate_division_query = dal.DBSession.query(SenateDivision)
        senate_division_record = senate_division_query.first()

        assert senate_division_query.count() == 1
        assert (
            senate_division_record.senate_division_short_name == "test-senate-division"
        )

    def test_save_to_database_saves_department_association(self):
        data = {
            "committee_preferred": "test-committee-preferred",
            "choice": 1,
            "email": "johndoe@mail.com",
            "name": "John Doe",
            "senate_division": "test-senate-division",
            "department": "test-department",
            "job_title": "test-job-title",
            "is_interested": True,
            "expertise": "test-expertise",
        }

        store.save_to_database(data)
        faculty_query = dal.DBSession.query(Faculty).filter(
            Faculty.email == "johndoe@mail.com"
        )
        faculty_record = faculty_query.first()

        department_query = dal.DBSession.query(Department).filter(
            Department.name == "test-department"
        )
        department_record = department_query.first()

        department_association_query = dal.DBSession.query(
            DepartmentAssociations
        ).filter(
            DepartmentAssociations.email == faculty_record.email,
            DepartmentAssociations.department_id == department_record.department_id,
        )

        department_association_record = department_association_query.first()

        assert department_association_query.count() == 1
        assert department_association_record.department_id == 1
        assert department_association_record.email == "johndoe@mail.com"
