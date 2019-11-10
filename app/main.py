import pandas as pd


def run():
    """Entry point for the application.

    :return: DataFrame representation of a CSV file
    """
    return pd.read_csv("data/faculty.csv")
