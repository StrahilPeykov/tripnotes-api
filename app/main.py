from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import time
from .database import engine
from . import models
from .routers import users, trips
from .logging import logger

# Create tables in the database
#models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="TripNotes API",
    description="A REST API for managing travel journals and notes",
    version="0.1.0"
)

# Simple in-memory rate limiter
class RateLimiter:
    def __init__(self, requests_per_minute=60):
        self.requests_per_minute = requests_per_minute
        self.request_history = {}
    
    def is_allowed(self, client_ip):
        now = time.time()
        minute_ago = now - 60
        
        # Clean up old requests
        self.request_history = {ip: times for ip, times in self.request_history.items() 
                              if any(t > minute_ago for t in times)}
        
        # Initialize client history if not exists
        if client_ip not in self.request_history:
            self.request_history[client_ip] = []
        
        # Count recent requests
        recent_requests = [t for t in self.request_history[client_ip] if t > minute_ago]
        
        # Check if limit exceeded
        if len(recent_requests) >= self.requests_per_minute:
            return False
        
        # Add current request
        self.request_history[client_ip].append(now)
        return True

rate_limiter = RateLimiter()

@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    client_ip = request.client.host
    
    if not rate_limiter.is_allowed(client_ip):
        logger.warning(f"Rate limit exceeded for {client_ip}")
        return JSONResponse(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            content={"detail": "Rate limit exceeded. Please try again later."}
        )
    
    response = await call_next(request)
    return response

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
app.include_router(trips.router)

@app.get("/health", tags=["health"])
async def health_check():
    """Health check endpoint for monitoring"""
    return {
        "status": "healthy",
        "api_version": "0.1.0",
        "timestamp": datetime.utcnow()
    }