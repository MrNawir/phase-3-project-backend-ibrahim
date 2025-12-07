from sqlalchemy import Column, Integer, String, Numeric, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..database import Base
import secrets


def generate_confirmation_code():
    """Generate a unique confirmation code"""
    return secrets.token_hex(8).upper()


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("events.id"), nullable=False)
    buyer_name = Column(String(100), nullable=False)
    buyer_email = Column(String(150), nullable=False)
    ticket_type = Column(String(50), default="Standard")  # Standard, VIP, Premium
    price = Column(Numeric(10, 2), nullable=False)
    confirmation_code = Column(String(20), unique=True, nullable=False, default=generate_confirmation_code)
    purchase_date = Column(DateTime(timezone=True), server_default=func.now())
    status = Column(String(20), default="confirmed")  # confirmed, cancelled, used

    # Relationships
    event = relationship("Event", back_populates="tickets")

    def __repr__(self):
        return f"<Ticket(id={self.id}, code='{self.confirmation_code}', status='{self.status}')>"
