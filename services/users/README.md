# Users Service

## Requirements

- Python 3.11
- Poetry
- Docker & Docker Compose

## Local Development

```bash
make setup
make run
```

Access the API:

- Swagger: http://localhost:8001/api/docs/
- Health: http://localhost:8001/api/v1/health/
- Registration: http://localhost:8001/api/v1/register/
- Login: http://localhost:8001/api/v1/login/
- Token Refresh: http://localhost:8001/api/v1/refresh/

## Running Tests

```bash
make test
```

## Features

- User registration and authentication
- JWT token-based authentication
- User profile management
- Secure password handling
