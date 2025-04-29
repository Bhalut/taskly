setup:
	poetry install
	poetry run pre-commit install

run:
	poetry run uvicorn src.main:app --reload --host 0.0.0.0 --port 8002

test:
	poetry run pytest --cov=src

lint:
	pre-commit run --all-files

format:
	black .
	isort .
