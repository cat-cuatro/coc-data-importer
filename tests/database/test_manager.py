import unittest

from app.database import dal
from app.database.entities import Committee
from app.database.entities import Department
from app.database.entities import Faculty
from app.database.entities import SurveyChoice
from app.database.entities import SurveyData
from app.database.manager import CommitteeManager
from app.database.manager import DepartmentManager
from app.database.manager import FacultyManager
from app.database.manager import SurveyChoiceManager
from app.database.manager import SurveyDataManager


class TestDatabaseQueryManager(unittest.TestCase):
    def setUp(self):
        dal.db_init("sqlite:///:memory:")

    def tearDown(self):
        dal.close()

    def test_committee_manager_adds_data_to_database(self):
        expected = CommitteeManager.add_committee("test-committee")
        actual = (
            dal.DBSession.query(Committee)
            .filter(Committee.name == "test-committee")
            .first()
        )

        assert actual.committee_id == expected.committee_id
        assert actual.name == expected.name

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
        department_record = DepartmentManager.add_department("test-department")
        department_id = department_record.department_id

        expected = FacultyManager.add_faculty(
            "test-full-name", "test-job-title", "test-senate-division", department_id
        )
        actual = (
            dal.DBSession.query(Faculty)
            .filter(Faculty.full_name == "test-full-name")
            .first()
        )

        assert actual.faculty_id == expected.faculty_id
        assert actual.full_name == expected.full_name
        assert actual.job_title == expected.job_title
        assert actual.senate_division == expected.senate_division
        assert actual.department_id == expected.department_id

    def test_survey_choice_manager_adds_data_to_database(self):
        department_record = DepartmentManager.add_department("test-department")
        department_id = department_record.department_id
        faculty_record = FacultyManager.add_faculty(
            "test-full-name", "test-job-title", "test-senate-division", department_id
        )
        faculty_id = faculty_record.faculty_id
        committee_record = CommitteeManager.add_committee("test-committee")
        committee_id = committee_record.committee_id

        expected = SurveyChoiceManager.add_survey_choice(faculty_id, committee_id)
        actual = (
            dal.DBSession.query(SurveyChoice)
            .filter(
                SurveyChoice.faculty_id == faculty_id,
                SurveyChoice.committee_id == committee_id,
            )
            .first()
        )

        assert actual.survey_choice_id == 1
        assert actual.faculty_id == expected.faculty_id
        assert actual.committee_id == expected.committee_id
        assert actual.choice_priority is None

    def test_survey_choice_manager_adds_data_to_database_with_priority(self):
        department_record = DepartmentManager.add_department("test-department")
        department_id = department_record.department_id
        faculty_record = FacultyManager.add_faculty(
            "test-full-name", "test-job-title", "test-senate-division", department_id
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
            "test-full-name", "test-job-title", "test-senate-division", department_id
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
            "test-full-name", "test-job-title", "test-senate-division", department_id
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
