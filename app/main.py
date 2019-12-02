from app.extract import extract
from app.load import load
from app.transform import transform


def run():
    """Entry point for the application.

    Extract data from an Excel spreadsheet, transforming and sanitizing it,
    and then loading it onto a database.

    :return: None
    """
    extracted = extract()
    transformed = transform(extracted)
    load(transformed)
