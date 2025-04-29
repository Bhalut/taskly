setup:
	poetry install
	poetry run pre-commit install
	poetry run python manage.py migrate
	poetry run python manage.py createsuperuser

run:
	poetry run python manage.py runserver 0.0.0.0:8000

migrate:
	poetry run python manage.py migrate

test:
	poetry run pytest --cov=apps

test-unit:
	pytest apps/tasks/tests/test_domain.py apps/tasks/tests/test_application.py

test-integration:
	pytest apps/tasks/tests/test_api.py

test-all:
	make test-unit && make test-integration

lint:
	pre-commit run --all-files

format:
	black .
	isort .
