lint:
	poetry run flake8 .

install:
	poetry install

build: check
	poetry build

test-coverage:
	poetry run pytest --cov=gendiff

test:
	poetry run pytest