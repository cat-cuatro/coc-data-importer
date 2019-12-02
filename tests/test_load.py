from unittest import mock

from app import load


@mock.patch("app.load.dal.db_init")
@mock.patch("app.load.store.save_to_database")
def test_load_saves_to_database(mock_save_database, mock_db_init):
    data = [1, 2, 3, 4]

    load.load(data)

    mock_db_init.assert_called_once()
    assert mock_save_database.call_count == 4
