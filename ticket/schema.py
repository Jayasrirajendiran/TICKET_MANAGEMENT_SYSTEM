from datetime import datetime

from pydantic import BaseModel, ConfigDict


class TicketCreate(BaseModel):

    ticket_title: str
    ticket_description: str
    ticket_status: str = "open"
    ticket_user_id: int


class TicketUpdate(BaseModel):

    ticket_title: str
    ticket_description: str
    ticket_status: str
    ticket_user_id: int


class TicketResponse(BaseModel):

    ticket_id: int
    ticket_title: str
    ticket_description: str
    ticket_status: str
    ticket_user_id: int
    started_date: datetime
    updated_date: datetime

    model_config = ConfigDict(
        from_attributes=True
    )