from unittest import mock

from app import main


@mock.patch("app.main.load")
@mock.patch("app.main.transform")
@mock.patch("app.main.extract")
def test_main_runs_etl(mock_extract, mock_transform, mock_load):
    mock_extract.return_value = None
    mock_transform.return_value = None
    mock_load.return_value = None

    main.run()

    mock_extract.assert_called_once()
    mock_transform.assert_called_once()
    mock_load.assert_called_once()
