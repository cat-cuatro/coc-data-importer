from unittest import mock

import pandas as pd

from app import extract


@mock.patch("app.extract.pd.read_excel")
def test_extract_returns_list_of_rows_from_spreadsheet(read_excel_mock):
    mock_data = {
        "Committee Preferred": pd.Series(["Honors Council", "Library Committee"]),
        "Choice": pd.Series(["1st Choice", "1st Choice"]),
        "Email": pd.Series(["alice@pdx.edu", "bob@pdx.edu"]),
        "Name": pd.Series(["Alice", "Bob"]),
        "Senate Division": pd.Series(["GSE", "AO"]),
        "Department": pd.Series(["CMP Computer Science Office", "FLL World Languages"]),
        "Job Title": pd.Series(["CMP UP Professor", "EDU UP Prof"]),
        "Able to serve": pd.Series(
            [
                "I am unable to serve on a committee during 2018-19",
                "I am able to serve on a committee during 2018-19",
            ]
        ),
        "expertise, interest, or previous experience pertaining to "
        "the preferences indicated": pd.Series(["No Response", "Some expertise"]),
    }
    expected = [
        {
            "Committee Preferred": "Honors Council",
            "Choice": "1st Choice",
            "Email": "alice@pdx.edu",
            "Name": "Alice",
            "Senate Division": "GSE",
            "Department": "CMP Computer Science Office",
            "Job Title": "CMP UP Professor",
            "Able to serve": "I am unable to serve on a committee during 2018-19",
            "expertise, interest, or previous experience pertaining to "
            "the preferences indicated": "No Response",
        },
        {
            "Committee Preferred": "Library Committee",
            "Choice": "1st Choice",
            "Email": "bob@pdx.edu",
            "Name": "Bob",
            "Senate Division": "AO",
            "Department": "FLL World Languages",
            "Job Title": "EDU UP Prof",
            "Able to serve": "I am able to serve on a committee during 2018-19",
            "expertise, interest, or previous experience pertaining to "
            "the preferences indicated": "Some expertise",
        },
    ]
    read_excel_mock.return_value = pd.DataFrame(mock_data)

    extracted = extract.extract()

    read_excel_mock.assert_called_once()
    assert extracted == expected
