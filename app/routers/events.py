from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session, joinedload
from typing import List, Optional

from ..database import get_db
from ..models import Event, Venue
from ..schemas import EventCreate, EventUpdate, EventResponse, EventWithVenue

router = APIRouter(prefix="/events", tags=["events"])


@router.get("", response_model=List[EventWithVenue])
def get_all_events(
    skip: int = 0, 
    limit: int = 100,
    category: Optional[str] = Query(None, description="Filter by category"),
    venue_id: Optional[int] = Query(None, description="Filter by venue"),
    search: Optional[str] = Query(None, description="Search in title and description"),
    db: Session = Depends(get_db)
):
    """Get all events with optional filtering and search"""
    query = db.query(Event).options(joinedload(Event.venue))
    
    if category:
        query = query.filter(Event.category == category)
    if venue_id:
        query = query.filter(Event.venue_id == venue_id)
    if search:
        search_term = f"%{search}%"
        query = query.filter(
            (Event.title.ilike(search_term)) | (Event.description.ilike(search_term))
        )
    
    events = query.offset(skip).limit(limit).all()
    return events


@router.get("/{event_id}", response_model=EventWithVenue)
def get_event(event_id: int, db: Session = Depends(get_db)):
    """Get a single event by ID with venue info"""
    event = db.query(Event).options(joinedload(Event.venue)).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event


@router.post("", response_model=EventResponse, status_code=status.HTTP_201_CREATED)
def create_event(event: EventCreate, db: Session = Depends(get_db)):
    """Create a new event"""
    # Verify venue exists
    venue = db.query(Venue).filter(Venue.id == event.venue_id).first()
    if not venue:
        raise HTTPException(status_code=404, detail="Venue not found")
    
    db_event = Event(**event.model_dump())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event


@router.put("/{event_id}", response_model=EventResponse)
def update_event(event_id: int, event: EventUpdate, db: Session = Depends(get_db)):
    """Update an event"""
    db_event = db.query(Event).filter(Event.id == event_id).first()
    if not db_event:
        raise HTTPException(status_code=404, detail="Event not found")
    
    # If updating venue, verify it exists
    if event.venue_id:
        venue = db.query(Venue).filter(Venue.id == event.venue_id).first()
        if not venue:
            raise HTTPException(status_code=404, detail="Venue not found")
    
    update_data = event.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_event, key, value)
    
    db.commit()
    db.refresh(db_event)
    return db_event


@router.delete("/{event_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_event(event_id: int, db: Session = Depends(get_db)):
    """Delete an event"""
    db_event = db.query(Event).filter(Event.id == event_id).first()
    if not db_event:
        raise HTTPException(status_code=404, detail="Event not found")
    
    db.delete(db_event)
    db.commit()
    return None
