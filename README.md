# Theatre API

A RESTful API for managing theatre plays, actors, genres, theatre halls, performances, reservations, and tickets. Built with Django REST Framework.

## Technologies

- Python
- Django
- Django REST Framework
- Simple JWT
- drf-spectacular (OpenAPI and Swagger UI)
- Docker and Docker Compose
- SQLite (development database)

## Features

- **Genres:** Create, list, retrieve, update, and delete genres.
- **Actors:** Manage actors and their information.
- **Plays:** Manage plays, descriptions, actors, and genres.
- **Theatre halls:** Manage theatre halls, rows, seats per row, and automatically calculated capacity.
- **Performances:** Schedule plays in theatre halls.
- **Reservations:** Create reservations associated with the authenticated user.
- **Tickets:** Create tickets as part of a reservation and retrieve ticket information.
- **Seat validation:** Validate seat and row numbers against the theatre hall's dimensions.
- **Reservation integrity:** Create a reservation and its tickets within a database transaction.
- **JWT authentication:** Obtain and refresh authentication tokens.
- **Interactive API documentation:** Explore and test endpoints using Swagger UI.

## Requirements

To run the project locally, install:

- Python 3.12 or a compatible version supported by the installed dependencies.
- Git.

To run the project with Docker, install Docker Desktop with Docker Compose.

## Running locally

### 1. Clone the repository

```bash
git clone <https://github.com/EduardoMoen/theatre-api>
cd theatre-api
```

Replace the placeholder with your public repository URL.

### 2. Create and activate a virtual environment

On Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

On Linux or macOS:

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Create an administrator account

```bash
python manage.py createsuperuser
```

Follow the prompts to configure your username and password.

### 6. Start the development server

```bash
python manage.py runserver
```

The API will be available at:

- API base URL: `http://127.0.0.1:8000/api/`
- Swagger UI: `http://127.0.0.1:8000/api/docs/`
- OpenAPI schema: `http://127.0.0.1:8000/api/schema/`
- Django administration: `http://127.0.0.1:8000/admin/`

## Running with Docker

Make sure Docker Desktop is running and execute the following commands from the project root.

### 1. Build and start the application

```bash
docker compose up --build -d
```

### 2. Apply database migrations

```bash
docker compose exec web python manage.py migrate
```

### 3. Create an administrator account

```bash
docker compose exec web python manage.py createsuperuser
```

### 4. Access the application

- API: `http://127.0.0.1:8000/api/`
- Swagger UI: `http://127.0.0.1:8000/api/docs/`
- Django administration: `http://127.0.0.1:8000/admin/`

To stop the containers:

```bash
docker compose down
```

## Authentication

The API uses JSON Web Tokens (JWT).

### Obtain a token

Send a `POST` request to `/api/token/` with valid user credentials:

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

The response contains an access token and a refresh token.

### Access protected endpoints

Include the access token in the `Authorization` header:

```http
Authorization: Bearer YOUR_ACCESS_TOKEN
```

The reservations and tickets endpoints require authentication. Users can only retrieve their own reservations and associated tickets.

### Refresh a token

Send a `POST` request to `/api/token/refresh/`:

```json
{
  "refresh": "YOUR_REFRESH_TOKEN"
}
```

## API endpoints

All resource endpoints use the `/api/` prefix.

| Resource | Endpoint | Supported operations |
|---|---|---|
| Genres | `/api/genres/` | List, create |
| Actors | `/api/actors/` | List, create |
| Plays | `/api/plays/` | List, create |
| Theatre halls | `/api/theatre-halls/` | List, create |
| Performances | `/api/performances/` | List, create |
| Reservations | `/api/reservations/` | List, create, retrieve, delete |
| Tickets | `/api/tickets/` | List, retrieve (read-only) |

The resource endpoints implemented with `ModelViewSet` also support retrieving individual records, updating them, and deleting them where applicable. Use Swagger UI to inspect the available methods and required fields.

## Creating a reservation

Authenticate first and obtain an access token. Then send a `POST` request to `/api/reservations/` with one or more tickets.

Example request:

```json
{
  "tickets": [
    {
      "row": 2,
      "seat": 5,
      "performance": 1
    }
  ]
}
```

Replace the performance ID with an existing performance ID. The row and seat must be valid for the theatre hall associated with that performance, and the selected seat must be available.

The reservation is associated with the authenticated user. The reservation and its tickets are created in a single database transaction.

## API documentation

Swagger UI provides an interactive interface for exploring endpoints, reviewing request and response schemas, and sending requests.

Open:

`http://127.0.0.1:8000/api/docs/`

Use the **Authorize** option to authenticate when testing protected endpoints.

## Project structure

```text
theatre-api/
├── theatre/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── theatre_service/
│   ├── settings.py
│   └── urls.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── manage.py
└── README.md
```

## Screenshots and database diagram

Screenshots of the browsable API and the database relationship diagram can be added to the `docs/` directory.

These materials help demonstrate the implemented endpoints, data relationships, and interactive documentation.
