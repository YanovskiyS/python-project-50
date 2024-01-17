lint:
	poetry run flake8 .

install:
	poetry install

build: check
	poetry build

test-coverage:
	poetry run pytest poetry run pytest --cov