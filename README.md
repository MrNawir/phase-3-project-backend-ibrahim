# Ticket2U Backend API 🎫

**FastAPI REST API** for the Ticket2U event ticketing platform.

---

## Tech Stack

- **FastAPI** - Modern Python web framework
- **SQLAlchemy** - ORM for database operations
- **Pydantic** - Data validation
- **Alembic** - Database migrations
- **SQLite** - Database (development)
- **Pipenv** - Dependency management

---

## Project Structure

```
backend/
├── app/
│   ├── models/          # SQLAlchemy models (Event, Venue, Ticket)
│   ├── routers/         # API endpoints
│   ├── schemas/         # Pydantic validation schemas
│   ├── database.py      # Database configuration
│   └── main.py          # FastAPI application entry
├── alembic/             # Database migrations
├── seed.py              # Database seeder with sample data
├── Pipfile              # Pipenv dependencies
├── Pipfile.lock         # Locked dependencies
└── README.md
```

---

## Local Development Setup

### Prerequisites

- **Python 3.10+**
- **Pipenv** (`pip install pipenv`)

### Installation

```bash
# Install dependencies
pipenv install

# Seed the database with sample Kenyan events/venues
pipenv run python seed.py

# Start the development server
pipenv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Access

- **API**: http://localhost:8000
- **Swagger Docs**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| **Venues** | | |
| GET | `/venues` | List all venues |
| GET | `/venues/{id}` | Get venue with events |
| POST | `/venues` | Create new venue |
| PUT | `/venues/{id}` | Update venue |
| DELETE | `/venues/{id}` | Delete venue |
| **Events** | | |
| GET | `/events` | List all events |
| GET | `/events/{id}` | Get event details |
| POST | `/events` | Create new event |
| PUT | `/events/{id}` | Update event |
| DELETE | `/events/{id}` | Delete event |
| **Tickets** | | |
| GET | `/tickets` | List all tickets |
| GET | `/tickets/{id}` | Get ticket |
| GET | `/tickets/code/{code}` | Get ticket by confirmation code |
| POST | `/tickets` | Purchase a ticket |
| DELETE | `/tickets/{id}` | Cancel ticket |
| **Stats** | | |
| GET | `/stats/dashboard` | Get dashboard statistics |

---

## Database Models

### Venue
- `id`, `name`, `address`, `city`, `capacity`, `image_url`, `created_at`

### Event
- `id`, `venue_id`, `title`, `description`, `category`, `event_date`, `event_time`, `image_url`, `created_at`

### Ticket
- `id`, `event_id`, `buyer_name`, `buyer_email`, `ticket_type`, `price`, `confirmation_code`, `status`, `purchase_date`

---

## Development Commands

```bash
# Run development server
pipenv run uvicorn app.main:app --reload

# Run database migrations
pipenv run alembic upgrade head

# Create new migration
pipenv run alembic revision --autogenerate -m "description"

# Re-seed database
pipenv run python seed.py
```

---

## License

MIT
