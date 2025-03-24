from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine
from . import models
from .routers import users

# Create tables in the database
#models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="TripNotes API",
    description="A REST API for managing travel journals and notes",
    version="0.1.0"
)

# CORS middleware configuration
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",  # If we create a frontend later
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to TripNotes API!"}

# Include routers
app.include_router(users.router)