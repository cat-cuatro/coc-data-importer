# poc-data-importer

## Overview

This application is a POC (Proof of Concept) for a service that aims to extract data from a CSV file and load it onto a database.

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
