import pandas as pd

from app import settings


def extract():
    """Extracts data from a spreadsheet.

    Loads data into a Pandas DataFrame and converts it into a list of dictionaries.

    :return: List of extracted data
    """
    df = pd.read_excel(settings.DATA_XLSX, sheet_name=1)

    return df.to_dict(orient="records")
