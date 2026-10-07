from sqlalchemy import Column, ForeignKey, Integer, String, Text

from models.base import CustomModel


class Ticket_Tbl(CustomModel):

    __tablename__ = "tickets"

    ticket_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    ticket_title = Column(
        String(200),
        nullable=False
    )

    ticket_description = Column(
        Text,
        nullable=False
    )

    ticket_status = Column(
        String(50),
        nullable=False,
        default="open"
    )

    ticket_user_id = Column(
        Integer,
        ForeignKey("users.user_id"),
        nullable=False
    )