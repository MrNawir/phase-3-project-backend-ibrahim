from pydantic import BaseModel, Field
from datetime import date, time, datetime
from typing import Optional


class EventBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=150)
    description: Optional[str] = None
    category: Optional[str] = Field(None, max_length=50)
    event_date: date
    event_time: time
    image_url: Optional[str] = None


class EventCreate(EventBase):
    venue_id: int


class EventUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=150)
    description: Optional[str] = None
    category: Optional[str] = Field(None, max_length=50)
    event_date: Optional[date] = None
    event_time: Optional[time] = None
    venue_id: Optional[int] = None
    image_url: Optional[str] = None


class VenueSummary(BaseModel):
    id: int
    name: str
    city: str
    capacity: int

    class Config:
        from_attributes = True


class EventResponse(EventBase):
    id: int
    venue_id: int
    created_at: datetime

    class Config:
        from_attributes = True


class EventWithVenue(EventResponse):
    venue: VenueSummary
