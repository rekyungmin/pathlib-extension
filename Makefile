all:
	black .
	mypy pathlib_ext/
	pytest tests/

format:
	black .

type:
	mypy pathlib-ext/

test:
	pytest tests/
