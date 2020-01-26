from app.database.manager import CommitteeManager
from app.database.manager import DepartmentManager
from app.database.manager import FacultyManager
from app.database.manager import SurveyChoiceManager
from app.database.manager import SurveyDataManager
from app.database.manager import DepartmentAssociationsManager
from app.database.manager import SenateDivisionManager
from app.logger import logger


def save_to_database(data):
    committee_preferred = data["committee_preferred"]
    choice = data["choice"]
    email = data["email"]
    name = data["name"]
    senate_division = data["senate_division"]
    department_name = data["department"]
    job_title = data["job_title"]
    is_interested = data["is_interested"]
    expertise = data["expertise"]

    logger.debug(f"Saving committee preferences for {name}")

    committee_id = None
    if committee_preferred:
        committee_record = CommitteeManager.add_committee(committee_preferred)
        committee_id = committee_record.committee_id

    department_record = DepartmentManager.add_department(department_name)
    department_id = department_record.department_id

    faculty_record = FacultyManager.add_faculty(
        name, email, job_title, senate_division
    )
    faculty_email = faculty_record.email

    SurveyChoiceManager.add_survey_choice(faculty_email, committee_id, choice)

    SurveyDataManager.add_survey_data(faculty_email, is_interested, expertise)

    SenateDivisionManager.add_senate_division(senate_division)

    DepartmentAssociationsManager.add_department_association(email, department_id)
