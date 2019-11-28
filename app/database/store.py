from app.database.manager import CommitteeManager
from app.database.manager import DepartmentManager
from app.database.manager import FacultyManager
from app.database.manager import SurveyChoiceManager
from app.database.manager import SurveyDataManager


def save_to_database(data):
    committee_preferred = data["committee_preferred"]
    choice = data["choice"]
    # email = data["email"]
    name = data["name"]
    senate_division = data["senate_division"]
    department_name = data["department"]
    job_title = data["job_title"]
    is_interested = data["is_interested"]
    expertise = data["expertise"]

    committee_id = None
    if committee_preferred:
        committee_record = CommitteeManager.add_committee(committee_preferred)
        committee_id = committee_record.committee_id

    department_record = DepartmentManager.add_department(department_name)
    department_id = department_record.department_id

    faculty_record = FacultyManager.add_faculty(
        name, job_title, senate_division, department_id
    )
    faculty_id = faculty_record.faculty_id

    SurveyChoiceManager.add_survey_choice(faculty_id, committee_id, choice)

    SurveyDataManager.add_survey_data(faculty_id, is_interested, expertise)
