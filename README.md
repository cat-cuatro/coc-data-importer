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
