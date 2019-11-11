from unittest import mock

import pandas as pd

from app import main


@mock.patch("pandas.read_csv")
def test_main_returns_faculty_count_and_names(read_csv_mock):
    # arrange
    mock_data = {
        "Name": pd.Series(["Alice", "Bob"]),
        "Email": pd.Series(["alice@pdx.edu", "bob@pdx.edu"]),
        "Phone": pd.Series(["555-55-5555", "777-77-7777"]),
        "Department": pd.Series(["Computer Science", "Anthropology"]),
    }
    expected = pd.DataFrame(mock_data)
    read_csv_mock.return_value = expected

    # act
    count, names = main.run()

    # assert
    read_csv_mock.assert_called_once()
    assert count == 2
    assert names == ["Alice", "Bob"]
