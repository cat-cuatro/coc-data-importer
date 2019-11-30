import pytest

from app import transform

choices = [("1st choice", 1), ("2nd choice", 2), ("3rd choice", 3), ("4th choice", 4)]
test_row = {
    "Committee Preferred": "Scholastic Standards Committee",
    "Choice": "1st choice",
    "Email": "johndoe@mail.com",
    "Name": "John Doe",
    "Senate Division": "CLAS-SCI",
    "Department": "CS Math Office",
    "Job Title": "MTH UP Assistant Professor",
    "Able to serve": "I am interested in committee work",
    "expertise, interest, or previous experience pertaining to the "
    "preferences indicated": "Some valid expertise",
}
valid_rows = [
    "committee_preferred",
    "choice",
    "email",
    "name",
    "senate_division",
    "department",
    "job_title",
    "is_interested",
    "expertise",
]


def test_transform_transforms_columns_of_all_rows():
    extracted = [test_row, test_row]

    transformed = transform.transform(extracted)

    assert [
        all(key in valid_rows for key in transformed_row)
        for transformed_row in transformed
    ]


def test_transform_row_renames_all_column_names():
    transformed_row = transform.transform_row(test_row)

    assert all(key in valid_rows for key in transformed_row)


def test_sanitize_committee_preference_returns_committee_name_if_not_empty():
    preference = "python software foundation"

    assert transform.sanitize_committee_preference(preference) == preference


def test_sanitize_committee_preference_returns_none_when_preference_is_empty_string():
    preference = ""

    assert transform.sanitize_committee_preference(preference) is None


def test_sanitize_committee_preference_returns_none_when_preference_is_empty_space():
    preference = " "

    assert transform.sanitize_committee_preference(preference) is None


@pytest.mark.parametrize("choice, expected", choices)
def test_sanitize_choice_returns_numerical_representation_of_choice(choice, expected):
    committee = "test-committee"

    assert transform.sanitize_choice(choice, committee) == expected


@pytest.mark.parametrize("choice, expected", choices)
def test_sanitize_choice_returns_none_when_committee_is_none(choice, expected):
    committee = None

    assert transform.sanitize_choice(choice, committee) is None


def test_sanitize_choice_returns_none_choice_is_invalid():
    choice = "7th choice"
    committee = None

    assert transform.sanitize_choice(choice, committee) is None


def test_sanitize_expertise_returns_expertise_when_valid_expertise():
    expertise = "some valid expertise"

    assert transform.sanitize_expertise(expertise) == expertise


def test_sanitize_expertise_returns_none_when_expertise_is_invalid():
    expertise = "No Response"

    assert transform.sanitize_expertise(expertise) is None
