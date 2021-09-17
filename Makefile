format:
	poetry run black pathlib_ext/ tests/

type:
	poetry run mypy pathlib_ext/

test:
	poetry run pytest --cov-report term-missing:skip-covered --cov=pathlib_ext tests/

all: format type test