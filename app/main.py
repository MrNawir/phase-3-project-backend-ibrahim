from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import engine, Base
from .routers import venues_router, events_router, tickets_router, stats_router

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="TicketToU API",
    description="Event ticketing API for managing venues, events, and ticket sales",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173", "http://localhost:5174", "http://127.0.0.1:5174"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(venues_router)
app.include_router(events_router)
app.include_router(tickets_router)
app.include_router(stats_router)


@app.get("/", tags=["root"])
def root():
    """API root endpoint"""
    return {
        "message": "Welcome to TicketToU API",
        "docs": "/docs",
        "version": "1.0.0"
    }


@app.get("/health", tags=["health"])
def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}
