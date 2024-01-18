lint:
	poetry run flake8 .

install:
	poetry install

build: check
	poetry build

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

test:
	poetry run pytest