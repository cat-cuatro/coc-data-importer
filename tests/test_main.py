from app import main


def test_main_returns_integer():
    result = main.run()

    assert result == 1234567890
