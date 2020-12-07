# cookiecutter-advent-of-code-template

## Requirements

You need the following:
- Python 3.9+, probably works with 3.4+, but I haven't tested
- [cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/)
- [Pipenv](https://pipenv.pypa.io/en/latest/)

Since this template's code is using
[advent-of-code-data](https://github.com/wimglenn/advent-of-code-data/),
you'll also need to provide your cookies for
[adventofcode.com](https://adventofcode.com). Checkout
advent-of-code-data about this for more instructions.

## Installation

```bash
$ cookiecutter gh:ifosch/cookiecutter-advent-of-code-template
username [your_GH_username]: <username>
full_name [Your Full Name]: <Your Full Name>
email [your@email.address]: <your@email.address>
python_version [3.9]: <Python version>
$ cd advent-of-code-<username>
$ pipenv shell
$ pipenv install --pre --dev
```

## Setup a new puzzle

Within a Pipenv shell:
```bash
$ setup 2015 1
```

## Run tests for a puzzle

Within a Pipenv shell:
```bash
$ run_tests 2015 1
```

## Run

Within a Pipenv shell:
```bash
$ check 2015 1
```

## Roadmap

* [ ] Consider adding tooling to run black
* [ ] Generate git repository
* [ ] Consider adding other languages to work on AoC
* [ ] Generate GH origin for the repository
* [ ] Use other testing frameworks and linters
