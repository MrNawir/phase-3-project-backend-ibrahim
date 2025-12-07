from pydantic import BaseModel, Field, EmailStr
from datetime import datetime
from typing import Optional
from decimal import Decimal


class TicketBase(BaseModel):
    buyer_name: str = Field(..., min_length=1, max_length=100)
    buyer_email: str = Field(..., min_length=1, max_length=150)
    ticket_type: str = Field(default="Standard", pattern="^(Standard|VIP|Premium)$")
    price: Decimal = Field(..., gt=0, decimal_places=2)


class TicketCreate(TicketBase):
    event_id: int


class TicketResponse(TicketBase):
    id: int
    event_id: int
    confirmation_code: str
    purchase_date: datetime
    status: str

    class Config:
        from_attributes = True


class TicketWithEvent(TicketResponse):
    event_title: str
    event_date: str
    venue_name: str
