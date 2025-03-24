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
TODO