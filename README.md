Red Flag
========

A toy implementatino of Flamme Rouge to play with AI techniques.

[![Build Status](https://travis-ci.com/afaulconbridge/redflag.svg?branch=master)](https://travis-ci.com/afaulconbridge/redflag)
[![PyPI version](https://badge.fury.io/py/redflag.svg)](https://badge.fury.io/py/redflag)
[![Run on Repl.it](https://repl.it/badge/github/afaulconbridge/redflag)](https://repl.it/github/afaulconbridge/redflag)

development
-----------

```sh
pip install -e .[dev]  # Install using pip including development extras
pre-commit install  # Enable pre-commit hooks
pre-commit run --all-files  # Run pre-commit hooks without committing
# Note pre-commit is configured to use:
# - seed-isort-config to better categorise third party imports
# - isort to sort imports
# - black to format code
pip-compile  # Freeze dependencies
pytest  # Run tests
coverage run --source=redflag -m pytest && coverage report -m  # Run tests, print coverage
mypy .  # Type checking
pipdeptree  # Print dependencies
```

Global git ignores per https://help.github.com/en/github/using-git/ignoring-files#configuring-ignored-files-for-all-repositories-on-your-computer

For release to PyPI see https://packaging.python.org/tutorials/packaging-projects/
