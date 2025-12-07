from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from ..database import get_db
from ..models import Venue, Event
from ..schemas import VenueCreate, VenueUpdate, VenueResponse, VenueWithEvents

router = APIRouter(prefix="/venues", tags=["venues"])


@router.get("", response_model=List[VenueResponse])
def get_all_venues(
    skip: int = 0, 
    limit: int = 100,
    search: Optional[str] = Query(None, description="Search by venue name"),
    city: Optional[str] = Query(None, description="Filter by city"),
    db: Session = Depends(get_db)
):
    """Get all venues with optional search and filtering"""
    query = db.query(Venue)
    
    if search:
        search_term = f"%{search}%"
        query = query.filter(Venue.name.ilike(search_term))
    if city:
        query = query.filter(Venue.city == city)
    
    venues = query.offset(skip).limit(limit).all()
    return venues


@router.get("/{venue_id}", response_model=VenueWithEvents)
def get_venue(venue_id: int, db: Session = Depends(get_db)):
    """Get a single venue by ID with its events"""
    venue = db.query(Venue).filter(Venue.id == venue_id).first()
    if not venue:
        raise HTTPException(status_code=404, detail="Venue not found")
    return venue


@router.post("", response_model=VenueResponse, status_code=status.HTTP_201_CREATED)
def create_venue(venue: VenueCreate, db: Session = Depends(get_db)):
    """Create a new venue"""
    db_venue = Venue(**venue.model_dump())
    db.add(db_venue)
    db.commit()
    db.refresh(db_venue)
    return db_venue


@router.put("/{venue_id}", response_model=VenueResponse)
def update_venue(venue_id: int, venue: VenueUpdate, db: Session = Depends(get_db)):
    """Update a venue"""
    db_venue = db.query(Venue).filter(Venue.id == venue_id).first()
    if not db_venue:
        raise HTTPException(status_code=404, detail="Venue not found")
    
    update_data = venue.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_venue, key, value)
    
    db.commit()
    db.refresh(db_venue)
    return db_venue


@router.delete("/{venue_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_venue(venue_id: int, db: Session = Depends(get_db)):
    """Delete a venue"""
    db_venue = db.query(Venue).filter(Venue.id == venue_id).first()
    if not db_venue:
        raise HTTPException(status_code=404, detail="Venue not found")
    
    db.delete(db_venue)
    db.commit()
    return None


@router.get("/{venue_id}/events", response_model=List[dict])
def get_venue_events(venue_id: int, db: Session = Depends(get_db)):
    """Get all events for a specific venue"""
    venue = db.query(Venue).filter(Venue.id == venue_id).first()
    if not venue:
        raise HTTPException(status_code=404, detail="Venue not found")
    
    events = db.query(Event).filter(Event.venue_id == venue_id).all()
    return [
        {
            "id": e.id,
            "title": e.title,
            "description": e.description,
            "category": e.category,
            "event_date": str(e.event_date),
            "event_time": str(e.event_time),
            "image_url": e.image_url,
            "created_at": e.created_at
        }
        for e in events
    ]
