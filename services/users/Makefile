setup:
	poetry install
	poetry run pre-commit install
	poetry run python manage.py migrate

run:
	poetry run python manage.py runserver 0.0.0.0:8001

migrate:
	poetry run python manage.py migrate

test:
	poetry run pytest --cov=apps

lint:
	pre-commit run --all-files

format:
	black .
	isort .
