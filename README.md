# Taskly 🚀

Taskly is a modern, microservices-based task management application built with Django, FastAPI, and PostgreSQL. The project follows a hexagonal architecture pattern, is fully containerized using Docker, and orchestrated via Docker Compose.

![License](https://img.shields.io/badge/license-MIT-blue)

## 📋 Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Technology Stack](#technology-stack)
- [Services](#services)
- [Getting Started](#getting-started)
- [Development Environment](#development-environment)
- [Environment Configuration](#environment-configuration)
- [API Documentation](#api-documentation)
- [Code Quality](#code-quality-tools)
- [Branching Strategy](#branching-strategy-trunk-based-development)
- [Directory Structure](#directory-structure)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## 📝 Overview

Taskly offers a streamlined task management experience with:

- User authentication and profile management
- Task creation, assignment, and status tracking
- RESTful API for easy integration with other systems
- Rate-limited access to prevent abuse
- API Gateway for unified access to all microservices

## 🏗️ Architecture

Taskly follows a microservices architecture with these key components:

```
          ┌─────────────┐
          │    Client   │
          └──────┬──────┘
                 │
                 ▼
          ┌─────────────┐
          │   Gateway   │ FastAPI API Gateway with rate limiting
          └──────┬──────┘
                 │
         ┌───────┴───────┐
         │               │
         ▼               ▼
┌─────────────┐  ┌─────────────┐
│    Users    │  │    Tasks    │ Django services with REST API
└──────┬──────┘  └──────┬──────┘
       │                │
       └────────┬───────┘
                │
                ▼
        ┌───────────────┐
        │  PostgreSQL   │ Shared database
        └───────────────┘
```

Each service follows hexagonal architecture principles:
- **Domain** - Core business logic
- **Application** - Use cases and services
- **Infrastructure** - External interfaces (API, database)

## 🔧 Technology Stack

- **Backend**:
  - **Python 3.11+**
  - **Django 5.2** (Users & Tasks services)
  - **Django REST Framework 3.16** (API for Django services)
  - **FastAPI 0.115** (Gateway service)
  - **Poetry** (Dependency management)

- **Database**:
  - **PostgreSQL 14+**

- **Infrastructure**:
  - **Docker & Docker Compose** (Containerization)
  - **Nginx** (Reverse proxy for production)
  - **GitHub Actions** (CI/CD)

- **Testing**:
  - **Pytest** (Testing framework)
  - **Coverage** (Code coverage)

## 📦 Services

Taskly consists of three main microservices:

### 1. Tasks Service

A Django application responsible for task management with:

- Full CRUD operations for tasks
- Domain-driven design following hexagonal architecture
- RESTful API with JWT authentication
- PostgreSQL for data persistence

### 2. Users Service

A Django application handling user management:

- User registration and authentication
- JWT token issuance and validation
- Profile management
- Secure password handling

### 3. Gateway Service

A FastAPI application serving as an API Gateway:

- Single entry point for all client requests
- Request routing to appropriate microservices
- Rate limiting to prevent abuse
- Authentication verification

## 🚀 Getting Started

### Prerequisites

- Docker and Docker Compose
- Python 3.11+ (optional for local-only setup)
- Poetry (dependency management)
- Git

### Quick Start

1. Clone the repository:
   ```bash
   git clone https://github.com/bhalut/taskly.git
   cd taskly
   ```

2. Initialize environment files:
   ```bash
   cp services/tasks/.env.example services/tasks/.env
   cp services/users/.env.example services/users/.env
   cp services/gateway/.env.example services/gateway/.env
   ```

3. Start all services:
   ```bash
   make up ENV=dev
   ```

4. Access the services:
   - Gateway API: http://localhost:8002
   - Tasks API: http://localhost:8000
   - Users API: http://localhost:8001

## 🛠 Development Environment

### Common Commands

| Task | Command | Description |
|:---|:---|:---|
| Start services | `make up ENV=dev` | Start all services in development mode |
| Stop services | `make down` | Stop all running services |
| Restart services | `make restart` | Restart all services |
| View logs | `make logs` | Display logs from all services |
| Run tests | `make test SERVICE=tasks` | Run tests for a specific service |
| Set up a service | `make setup SERVICE=tasks` | Install dependencies for a service |
| Lint code | `make lint SERVICE=tasks` | Run linters on a service |
| Format code | `make format SERVICE=tasks` | Apply code formatters to a service |

> **Note**: Replace `tasks` with `users` or `gateway` as needed.

### Individual Service Setup

Each service can be developed and run independently:

#### Tasks Service
```bash
cd services/tasks
make setup
make run
```

#### Users Service
```bash
cd services/users
make setup
make run
```

#### Gateway Service
```bash
cd services/gateway
make setup
make run
```

## 🌎 Environment Configuration

Each service has its own environment configuration files:

- `.env.example` — Development defaults (copy to `.env`)
- `.env.production` — Production environment variables
- `.env.ci` — Used for automated testing during CI runs

### Important Environment Variables

#### Tasks Service
```
# .env example
# SECURITY
SECRET_KEY="django-insecure-jab2gsgoc-89a$8@8r7r&7bu$=-&dm%8se#h4cwt0fz_v$=mpv"
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# POSTGRESQL DATABASE CONFIGURATION
POSTGRES_DB=tasks_db
POSTGRES_USER=tasks_user
POSTGRES_PASSWORD=tasks_password
POSTGRES_HOST=db
POSTGRES_PORT=5432

# CORS CONFIGURATION
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://localhost:8000

```

#### Users Service
```
# .env example
# SECURITY
SECRET_KEY="django-insecure-jab2gsgoc-89a$8@8r7r&7bu$=-&dm%8se#h4cwt0fz_v$=mpv"
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# POSTGRESQL DATABASE CONFIGURATION
POSTGRES_DB=users_db
POSTGRES_USER=users_user
POSTGRES_PASSWORD=users_password
POSTGRES_HOST=db
POSTGRES_PORT=5432

# CORS CONFIGURATION
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://localhost:8000

```

#### Gateway Service
```
# .env example
USERS_SERVICE_URL=http://users:8001/api/v1/auth
JWT_SECRET_KEY=your_real_secret_key
ACCESS_TOKEN_EXPIRE_MINUTES=30

```

## 📚 API Documentation

### Gateway API

- Swagger UI: http://localhost:8002/docs
- OpenAPI JSON: http://localhost:8002/openapi.json

### Tasks API

- Swagger UI: http://localhost:8000/api/docs/
- OpenAPI JSON: http://localhost:8000/api/schema/

### Users API

- Swagger UI: http://localhost:8001/api/docs/
- OpenAPI JSON: http://localhost:8001/api/schema/


## 🧹 Code Quality Tools

Taskly uses several tools to maintain code quality:

- **Black**: Python code formatter
- **Isort**: Import statement organizer
- **Flake8**: Style guide enforcement
- **MyPy**: Static type checking
- **Ruff**: Fast Python linter
- **Pre-commit**: Git hooks for code quality checks

### Using Code Quality Tools

```bash
# Install pre-commit hooks
pre-commit install

# Format code in a service
make format SERVICE=tasks

# Lint code in a service
make lint SERVICE=tasks
```

## 📚 Branching Strategy: Trunk Based Development

Taskly follows a **Trunk Based Development** strategy:

| Branch | Purpose |
|:---|:---|
| `develop` | Integration branch for all feature work |
| `main` | Stable production-ready branch |
| `feature/*` | Temporary branches for new features |
| `bugfix/*` | Temporary branches for fixing bugs |
| `hotfix/*` | Emergency fixes for production issues |

### Development Workflow

1. Create a branch from `develop`:
   ```bash
   git checkout develop
   git pull
   git checkout -b feature/my-new-feature
   ```

2. Make changes and commit:
   ```bash
   git add .
   git commit -m "Add new feature"
   ```

3. Push and create a PR:
   ```bash
   git push -u origin feature/my-new-feature
   # Create PR through GitHub UI
   ```

4. Ensure all checks pass
5. Get PR approved and merge to `develop`
6. Manually promote to production via a Release

## 📂 Directory Structure

Taskly follows a well-organized directory structure:

```
.
├── .github/                  # GitHub workflows and templates
├── infra/                    # Infrastructure configuration
│   ├── docker/               # Dockerfiles for services
│   ├── docker-compose.*.yml  # Docker Compose configurations
│   └── nginx/                # Nginx configuration for production
├── services/                 # Microservices
│   ├── gateway/              # API Gateway service
│   ├── tasks/                # Task management service
│   └── users/                # User management service
├── CONTRIBUTING.md           # Contributing guidelines
├── .pre-commit-config.yaml   # Pre-commit hooks configuration
├── Makefile                  # Project-level make commands
├── pyproject.toml            # Project-level Python configuration
└── README.md                 # Project documentation
```

Each service follows its own internal structure:

### Tasks Service Structure

```
tasks/
├── apps/                     # Django applications
│   └── tasks/                # Tasks app following hexagonal architecture
│       ├── api/              # API layer (interfaces)
│       ├── application/      # Application services
│       ├── domain/           # Domain models and business logic
│       └── infrastructure/   # Infrastructure adapters
├── config/                   # Django settings and configuration
├── scripts/                  # Utility scripts
└── tests/                    # Test suite
```

### Users Service Structure

```
users/
├── apps/                     # Django applications
│   └── accounts/             # User accounts app
│       ├── api/              # API layer
│       └── infrastructure/   # Infrastructure adapters
├── config/                   # Django settings and configuration
└── tests/                    # Test suite
```

### Gateway Service Structure

```
gateway/
├── src/                      # Source code
│   └── app/                  # FastAPI application
│       ├── api/              # API routes
│       ├── core/             # Core functionality
│       └── main.py           # Application entry point
└── tests/                    # Test suite
```

## 🔧 Troubleshooting

### Common Issues

#### Services Cannot Connect to Database

- Check if PostgreSQL container is running: `docker ps | grep db`
- Verify database credentials in service `.env` files
- Make sure networks are properly configured in Docker Compose

#### JWT Authentication Issues

- Ensure `SECRET_KEY` is identical across services
- Check token expiration settings
- Verify that the user exists in the database

#### Docker Build Fails

- Check for syntax errors in Dockerfiles
- Verify dependency versions in `pyproject.toml` files
- Make sure Docker has sufficient resources

### Debugging

Enable debug logs by setting `DEBUG=True` in service `.env` files and restart:

```bash
make restart
```

View logs with:

```bash
make logs
```

Or for a specific service:

```bash
docker-compose logs -f tasks
```

## 🤝 Contributing

We welcome contributions to Taskly! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

### Quick Contribution Guidelines

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests and linters
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## 📄 License

Taskly is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

# 🏆 Built with ❤️ by the Taskly team.
