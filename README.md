# prod-data-importer

## Overview

The purpose of this tool is to extract data from a committee survey spreadsheet and load it onto a database.
It does that in three steps:

* The data is extracted form the spreadsheet
* The data is transformed and sanitized
* The data is loaded onto a SQLite database

More information on the database schema can be found on the [ERDiagram V1](https://capstonefall19.atlassian.net/wiki/spaces/CF1/pages/4554821/ERDiagram+V1) Confluence page.

When ran, the tool will write to an in-memory database by default.
To override this, add `DATABASE_PATH=app.db` to an `.env` file.
See learn more about this, read this [section](#how-to-override-environment-variables).

## How to Develop

Install the required packages:

```bash
pip3 install -r requirements.txt
```

Pre-commit hooks are actions that execute before or after a hook.
The pre-commit configuration can be found in [pre-commit-config.yaml](.pre-commit-config.yaml).

Install pre-commit and pre-push hooks:

```bash
pre-commit install -t pre-commit
pre-commit install -t pre-push
```

Run the application:

```bash
python3 -m app
```

Test the application:

```bash
pytest
```

## How to Override Environment Variables

Instead of changing the code to override environment variables, it is enough to create an `.env` file with the desired environment variables.
This file will be automatically loaded on startup, and the environment variables populated.

See [settings.py](./app/settings.py) for a list of environment variables that can be overriden.

Note that the `.env` file should **NOT** be checked in into the repo, as it may potentially contain secrets.

## Example Queries

This query produces a table with some information on a faculty member:

```sql
SELECT email, full_name, senate_division, job_title, is_interested, expertise
  FROM survey_data SD
       NATURAL JOIN faculty F
 WHERE full_name = 'John Doe';
```
