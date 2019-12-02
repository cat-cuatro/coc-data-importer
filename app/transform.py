def transform(extracted):
    """Transforms and sanitizes a list of data corresponding to spreadsheet rows.

    :param extracted: A list of spreadsheet rows
    :return:          A cleaned up list of spreadsheet rows
    """
    transformed = [transform_row(row) for row in extracted]

    # [print(e) for e in extracted]
    # [print(t) for t in transformed]
    return transformed


def transform_row(row):
    """Transforms a spreadsheet row, sanitizing its values and changing key names.

    Replaces some column names with more descriptive names.
    Replaces some columns values with data that better matches its semantics.

    :param row: Row to sanitize
    :return:    Transformed and sanitized row
    """
    committee_preferred = sanitize_committee_preference(row["Committee Preferred"])
    choice = sanitize_choice(row["Choice"], committee_preferred)
    is_interested = sanitize_interest(row["Able to serve"])
    expertise = sanitize_expertise(
        row[
            "expertise, interest, or previous experience pertaining to the preferences indicated"
        ]
    )

    return {
        "committee_preferred": committee_preferred,
        "choice": choice,
        "email": row["Email"],
        "name": row["Name"],
        "senate_division": row["Senate Division"],
        "department": row["Department"],
        "job_title": row["Job Title"],
        "is_interested": is_interested,
        "expertise": expertise,
    }


def sanitize_committee_preference(preference):
    """Sanitizes the 'Committee Preference' column data.

    :param preference: The column value to sanitize
    :return:           None if the column was empty, otherwise keeps its column value
    """
    return None if preference in [" ", ""] else preference


def sanitize_choice(choice, committee_preferred):
    """Sanitizes the 'Choice' column data.

    :param choice:              The column value to sanitize
    :param committee_preferred: The preferred committee
    :return:                    Integer representation of the choice,
                                or None if no committee was selected
    """
    if not committee_preferred:
        return None

    return {"1st choice": 1, "2nd choice": 2, "3rd choice": 3, "4th choice": 4}.get(
        choice, None
    )


def sanitize_expertise(expertise):
    """Sanitizes the 'Expertise' column data.

    :param expertise: The column value to sanitize
    :return:          None if the column data is "No Response", otherwise keeps its column value
    """
    return None if expertise.lower() == "no response" else expertise


def sanitize_interest(interest):
    """Sanitizes the 'Able to serve' column data.

    :param interest: The column value to sanitize
    :return:         True if faculty member is interested, False otherwise
    """
    return interest.startswith("I am unable")
