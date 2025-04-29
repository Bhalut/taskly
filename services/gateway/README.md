# Gateway Service

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

- API documentation: http://localhost:8002/docs
- Health check: http://localhost:8002/api/v1/ping

## Running Tests

```bash
make test
```

## Features

- Single entry point to all Taskly microservices
- Request routing and proxying
- Rate limiting protection (configured per endpoint)
- Authentication proxy for backend services
- Request/response transformation

## API Endpoints

The Gateway provides access to:

- Authentication services (`/api/v1/auth/*`)
  - Register: POST `/api/v1/auth/register`
  - Login: POST `/api/v1/auth/login`
  - Refresh: POST `/api/v1/auth/refresh`
  - Logout: POST `/api/v1/auth/logout`

- Task management (`/api/v1/tasks/*`)
  - List tasks: GET `/api/v1/tasks/`
  - Create task: POST `/api/v1/tasks/`
  - Get task: GET `/api/v1/tasks/{id}/`
  - Update task: PUT `/api/v1/tasks/{id}/`
  - Delete task: DELETE `/api/v1/tasks/{id}/`
