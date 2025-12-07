from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..models import Ticket, Event
from ..schemas import TicketCreate, TicketResponse

router = APIRouter(prefix="/tickets", tags=["tickets"])


@router.get("", response_model=List[TicketResponse])
def get_all_tickets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all tickets"""
    tickets = db.query(Ticket).offset(skip).limit(limit).all()
    return tickets


@router.get("/{ticket_id}", response_model=TicketResponse)
def get_ticket(ticket_id: int, db: Session = Depends(get_db)):
    """Get a single ticket by ID"""
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket


@router.get("/code/{confirmation_code}", response_model=TicketResponse)
def get_ticket_by_code(confirmation_code: str, db: Session = Depends(get_db)):
    """Get a ticket by confirmation code"""
    ticket = db.query(Ticket).filter(Ticket.confirmation_code == confirmation_code).first()
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket


@router.post("", response_model=TicketResponse, status_code=status.HTTP_201_CREATED)
def purchase_ticket(ticket: TicketCreate, db: Session = Depends(get_db)):
    """Purchase a new ticket"""
    # Verify event exists
    event = db.query(Event).filter(Event.id == ticket.event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    
    db_ticket = Ticket(**ticket.model_dump())
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket


@router.delete("/{ticket_id}", status_code=status.HTTP_204_NO_CONTENT)
def cancel_ticket(ticket_id: int, db: Session = Depends(get_db)):
    """Cancel a ticket (sets status to cancelled)"""
    db_ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not db_ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    
    if db_ticket.status == "cancelled":
        raise HTTPException(status_code=400, detail="Ticket is already cancelled")
    
    db_ticket.status = "cancelled"
    db.commit()
    return None


@router.get("/event/{event_id}", response_model=List[TicketResponse])
def get_event_tickets(event_id: int, db: Session = Depends(get_db)):
    """Get all tickets for a specific event"""
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    
    tickets = db.query(Ticket).filter(Ticket.event_id == event_id).all()
    return tickets
