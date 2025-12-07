from .venues import router as venues_router
from .events import router as events_router
from .tickets import router as tickets_router
from .stats import router as stats_router

__all__ = ["venues_router", "events_router", "tickets_router", "stats_router"]
