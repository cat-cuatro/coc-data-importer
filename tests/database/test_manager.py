import unittest

from app.database import dal
from app.database.entities import Committee
from app.database.entities import Department
from app.database.entities import Faculty
from app.database.entities import SurveyChoice
from app.database.entities import SurveyData
from app.database.entities import SenateDivision
from app.database.entities import DepartmentAssociations
from app.database.manager import CommitteeManager
from app.database.manager import DepartmentManager
from app.database.manager import FacultyManager
from app.database.manager import SurveyChoiceManager
from app.database.manager import SurveyDataManager
from app.database.manager import SenateDivisionManager
from app.database.manager import DepartmentAssociationsManager


class TestDatabaseQueryManager(unittest.TestCase):
    def setUp(self):
        dal.db_init("sqlite:///:memory:")

    def tearDown(self):
        dal.close()

    def test_committee_manager_adds_data_to_database(self):
        expected = CommitteeManager.add_committee("test-committee", None, 10)
        actual = (
            dal.DBSession.query(Committee)
            .filter(Committee.name == "test-committee",
                    Committee.total_slots == 10)
            .first()
        )

        assert actual.committee_id == expected.committee_id
        assert actual.name == expected.name
        assert actual.total_slots == expected.total_slots

    def test_department_manager_adds_data_to_database(self):
        expected = DepartmentManager.add_department("test-department")
        actual = (
            dal.DBSession.query(Department)
            .filter(Department.name == "test-department")
            .first()
        )

        assert actual.department_id == expected.department_id
        assert actual.name == expected.name

    def test_faculty_manager_adds_data_to_database(self):
        expected = FacultyManager.add_faculty(
            "test-full-name",
            "test-email",
            "test-job-title",
            "test-senate-division",
        )
        actual = (
            dal.DBSession.query(Faculty)
            .filter(Faculty.email == "test-email")
            .first()
        )

        assert actual.full_name == expected.full_name
        assert actual.email == expected.email
        assert actual.job_title == expected.job_title
        assert actual.senate_division_short_name == expected.senate_division_short_name

    def test_survey_choice_manager_adds_data_to_database(self):
        faculty_record = FacultyManager.add_faculty(
            "test-full-name",
            "test-email",
            "test-job-title",
            "test-senate-division",
        )
        faculty_email = faculty_record.email
        committee_record = CommitteeManager.add_committee("test-committee")
        committee_id = committee_record.committee_id

        expected = SurveyChoiceManager.add_survey_choice(faculty_email, committee_id)
        actual = (
            dal.DBSession.query(SurveyChoice)
            .filter(
                SurveyChoice.email == faculty_email,
                SurveyChoice.committee_id == committee_id,
            )
            .first()
        )

        assert actual.survey_choice_id == 1
        assert actual.email == expected.email
        assert actual.committee_id == expected.committee_id
        assert actual.choice_priority is None

    def test_survey_choice_manager_adds_data_to_database_with_priority(self):
        department_record = DepartmentManager.add_department("test-department")
        department_id = department_record.department_id
        faculty_record = FacultyManager.add_faculty(
            "test-full-name",
            "test-email",
            "test-job-title",
            "test-senate-division",
            department_id,
        )
        faculty_id = faculty_record.faculty_id
        committee_record = CommitteeManager.add_committee("test-committee")
        committee_id = committee_record.committee_id

        expected = SurveyChoiceManager.add_survey_choice(faculty_id, committee_id, 1)
        actual = (
            dal.DBSession.query(SurveyChoice)
            .filter(
                SurveyChoice.faculty_id == faculty_id,
                SurveyChoice.committee_id == committee_id,
            )
            .first()
        )

        assert actual.faculty_id == expected.faculty_id
        assert actual.committee_id == expected.committee_id
        assert actual.choice_priority == 1

    def test_survey_data_manager_adds_data_to_database(self):
        department_record = DepartmentManager.add_department("test-department")
        department_id = department_record.department_id
        faculty_record = FacultyManager.add_faculty(
            "test-full-name",
            "test-email",
            "test-job-title",
            "test-senate-division",
            department_id,
        )
        faculty_id = faculty_record.faculty_id

        expected = SurveyDataManager.add_survey_data(faculty_id, True)
        actual = (
            dal.DBSession.query(SurveyData)
            .filter(SurveyData.faculty_id == faculty_id)
            .first()
        )

        assert actual.faculty_id == expected.faculty_id
        assert actual.is_interested == expected.is_interested
        assert actual.expertise is None

    def test_survey_data_manager_adds_data_to_database_with_expertise(self):
        department_record = DepartmentManager.add_department("test-department")
        department_id = department_record.department_id
        faculty_record = FacultyManager.add_faculty(
            "test-full-name",
            "test-email",
            "test-job-title",
            "test-senate-division",
            department_id,
        )
        faculty_id = faculty_record.faculty_id

        expected = SurveyDataManager.add_survey_data(faculty_id, True, "test-expertise")
        actual = (
            dal.DBSession.query(SurveyData)
            .filter(SurveyData.faculty_id == faculty_id)
            .first()
        )

        assert actual.faculty_id == expected.faculty_id
        assert actual.is_interested == expected.is_interested
        assert actual.expertise == expected.expertise

    def test_senate_division_manager_adds_data_to_database(self):
        expected = SenateDivisionManager.add_senate_division("TSD", "test-senate-division")
        actual = (
            dal.DBSession.query(SenateDivision)
            .filter(
                SenateDivision.senate_division_short_name == "TSD",
                SenateDivision.name == "test-senate-division"
            )
            .first()
        )

        assert actual.senate_division_short_name == expected.senate_division_short_name
        assert actual.name == expected.name

    def test_department_associations_manager_adds_data_to_database(self):
        department_record = DepartmentManager.add_department("test-department")
        department_id = department_record.department_id
        faculty_record = FacultyManager.add_faculty(
            "test-full-name",
            "test-email",
            "test-job-title",
            "test-senate-division",
            department_id,
        )
        faculty_email = faculty_record.email

        expected = DepartmentAssociationsManager.add_department_association(faculty_email, department_id)
        actual = (
            dal.DBSession.query(DepartmentAssociations)
            .filter(
                DepartmentAssociations.email == faculty_email,
                DepartmentAssociations.department_id == department_id
            )
            .first()
        )

        assert actual.department_id == expected.department_id
        assert actual.email == expected.email
