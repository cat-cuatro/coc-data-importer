from unittest import mock

import pandas as pd

from app import extract


@mock.patch("app.extract.pd.read_excel")
def test_extract_returns_list_of_rows(read_excel_mock):
    mock_data = {
        "Name": pd.Series(["Alice", "Bob"]),
        "Email": pd.Series(["alice@pdx.edu", "bob@pdx.edu"]),
        "Phone": pd.Series(["555-55-5555", "777-77-7777"]),
        "Department": pd.Series(["Computer Science", "Anthropology"]),
    }
    expected = [
        {
            "Name": "Alice",
            "Email": "alice@pdx.edu",
            "Phone": "555-55-5555",
            "Department": "Computer Science",
        },
        {
            "Name": "Bob",
            "Email": "bob@pdx.edu",
            "Phone": "777-77-7777",
            "Department": "Anthropology",
        },
    ]
    read_excel_mock.return_value = pd.DataFrame(mock_data)

    extracted = extract.extract()

    read_excel_mock.assert_called_once()
    assert extracted == expected
