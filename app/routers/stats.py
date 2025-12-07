from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime

from ..database import get_db
from ..models import Venue, Event, Ticket

router = APIRouter(prefix="/stats", tags=["stats"])


@router.get("/dashboard")
def get_dashboard_stats(db: Session = Depends(get_db)):
    """Get dashboard statistics for admin panel"""
    
    # Counts
    total_venues = db.query(func.count(Venue.id)).scalar() or 0
    total_events = db.query(func.count(Event.id)).scalar() or 0
    total_tickets = db.query(func.count(Ticket.id)).scalar() or 0
    
    # Revenue (confirmed tickets only)
    total_revenue = db.query(func.sum(Ticket.price)).filter(
        Ticket.status != "cancelled"
    ).scalar() or 0
    
    # Recent tickets (last 10)
    recent_tickets = db.query(Ticket).order_by(
        Ticket.purchase_date.desc()
    ).limit(10).all()
    
    # Upcoming events (next 5)
    upcoming_events = db.query(Event).filter(
        Event.event_date >= datetime.now().date()
    ).order_by(Event.event_date).limit(5).all()
    
    # Ticket stats by status
    confirmed_tickets = db.query(func.count(Ticket.id)).filter(
        Ticket.status == "confirmed"
    ).scalar() or 0
    
    cancelled_tickets = db.query(func.count(Ticket.id)).filter(
        Ticket.status == "cancelled"
    ).scalar() or 0
    
    return {
        "total_venues": total_venues,
        "total_events": total_events,
        "total_tickets": total_tickets,
        "total_revenue": float(total_revenue),
        "confirmed_tickets": confirmed_tickets,
        "cancelled_tickets": cancelled_tickets,
        "recent_tickets": [
            {
                "id": t.id,
                "confirmation_code": t.confirmation_code,
                "buyer_name": t.buyer_name,
                "buyer_email": t.buyer_email,
                "event_id": t.event_id,
                "ticket_type": t.ticket_type,
                "price": float(t.price),
                "status": t.status,
                "purchase_date": t.purchase_date.isoformat() if t.purchase_date else None
            }
            for t in recent_tickets
        ],
        "upcoming_events": [
            {
                "id": e.id,
                "title": e.title,
                "event_date": e.event_date.isoformat() if e.event_date else None,
                "event_time": e.event_time,
                "category": e.category,
                "venue_id": e.venue_id
            }
            for e in upcoming_events
        ]
    }
