# Configurable variables
ENV ?= dev
SERVICE ?= tasks

# Determine Compose file based on environment
COMPOSE_FILE = infra/docker-compose.yml
ifeq ($(ENV),prod)
    COMPOSE_FILE = infra/docker-compose.prod.yml
endif

# Detect if running inside CI environment
ifeq ($(CI),true)
    ENV = ci
    COMPOSE_FILE = infra/docker-compose.ci.yml
endif

# Nice colors
GREEN  = \033[0;32m
YELLOW = \033[0;33m
NC     = \033[0m

help:
	@echo ""
	@echo "Usage: make [command] [ENV=dev|prod|ci] [SERVICE=tasks|users|gateway]"
	@echo ""
	@echo "Commands:"
	@echo "  up          => Build and start Docker services"
	@echo "  down        => Stop Docker services"
	@echo "  restart     => Restart Docker services"
	@echo "  logs        => Tail Docker logs"
	@echo "  ps          => List running containers"
	@echo "  migrate     => Apply Django migrations for a service"
	@echo "  shell       => Open Django shell for a service"
	@echo "  test        => Run tests for a service"
	@echo "  lint        => Run linters (pre-commit)"
	@echo "  format      => Format code (black + isort)"
	@echo "  setup       => Install dependencies (poetry + pre-commit)"
	@echo ""

# Docker Compose Operations
up:
	@echo "$(YELLOW)Starting services using $(ENV) environment...$(NC)"
	docker compose -f $(COMPOSE_FILE) -p taskly_$(ENV) up --build

down:
	@echo "$(YELLOW)Stopping services...$(NC)"
	docker compose -f $(COMPOSE_FILE) -p taskly_$(ENV) down

restart:
	@echo "$(YELLOW)Restarting services...$(NC)"
	docker compose -f $(COMPOSE_FILE) -p taskly_$(ENV) down
	docker compose -f $(COMPOSE_FILE) -p taskly_$(ENV) up --build

logs:
	docker compose -f $(COMPOSE_FILE) -p taskly_$(ENV) logs -f --tail=100

ps:
	docker compose -f $(COMPOSE_FILE) -p taskly_$(ENV) ps

# Per-service Operations
run:
	@echo "$(GREEN)Running service $(SERVICE)...$(NC)"
	cd services/$(SERVICE) && poetry run python manage.py runserver 0.0.0.0:8000

migrate:
	cd services/$(SERVICE) && poetry run python manage.py migrate

shell:
	cd services/$(SERVICE) && poetry run python manage.py shell

test:
	cd services/$(SERVICE) && poetry run pytest --cov=apps

lint:
	cd services/$(SERVICE) && pre-commit run --all-files

format:
	cd services/$(SERVICE) && black . && isort .

setup:
	cd services/$(SERVICE) && poetry install && poetry run pre-commit install
