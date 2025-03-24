# TripNotes API

A RESTful API for managing travel journals and notes, built with FastAPI and PostgreSQL.

## Features

- User authentication with JWT
- CRUD operations for trips
- Nested notes for each trip
- Support for markdown in notes
- Optional media links in notes

## Tech Stack

- **Framework**: FastAPI (Python, async)
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy + Alembic
- **Authentication**: JWT (via `python-jose`)
- **Versioning**: Git + GitHub

## API Endpoints

### Authentication
- `POST /signup`: Register a user
- `POST /login`: Log in, receive JWT
- `POST /logout`: Invalidate current token

### Trips
- `GET /trips`: List all trips (for current user)
- `POST /trips`: Add a trip
- `GET /trips/{id}`: View a trip's details
- `PUT /trips/{id}`: Edit a trip
- `DELETE /trips/{id}`: Delete a trip

### Notes
- `POST /trips/{id}/notes`: Add a note
- `GET /trips/{id}/notes`: Get all notes for a trip
- `GET /trips/{id}/notes/{note_id}`: Get a specific note
- `PUT /trips/{id}/notes/{note_id}`: Update a note
- `DELETE /trips/{id}/notes/{note_id}`: Delete a note

## Setup and Installation

### Prerequisites
- Python 3.8+
- PostgreSQL

### Installation
### Installation
1. Clone this repository
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Copy `.env.example` to `.env` and update with your PostgreSQL credentials
6. Generate a secret key: `python key.py`
7. Run migrations: `alembic upgrade head`
8. Start the server: `uvicorn app.main:app --reload`