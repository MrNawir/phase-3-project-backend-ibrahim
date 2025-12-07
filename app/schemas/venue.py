from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List


class VenueBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    address: str = Field(..., min_length=1, max_length=255)
    city: str = Field(..., min_length=1, max_length=100)
    capacity: int = Field(..., gt=0)
    image_url: Optional[str] = None


class VenueCreate(VenueBase):
    pass


class VenueUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    address: Optional[str] = Field(None, min_length=1, max_length=255)
    city: Optional[str] = Field(None, min_length=1, max_length=100)
    capacity: Optional[int] = Field(None, gt=0)
    image_url: Optional[str] = None


class VenueResponse(VenueBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class EventSummary(BaseModel):
    id: int
    title: str
    event_date: str
    category: Optional[str]

    class Config:
        from_attributes = True


class VenueWithEvents(VenueResponse):
    events: List[EventSummary] = []
