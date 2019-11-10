from unittest import mock

import pandas as pd

from app import main


@mock.patch("pandas.read_csv")
def test_main_returns_dataframe(read_csv_mock):
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
    result = main.run()

    # assert
    read_csv_mock.assert_called_once()
    pd.testing.assert_frame_equal(expected, result)