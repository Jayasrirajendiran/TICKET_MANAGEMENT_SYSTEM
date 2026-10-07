from sqlalchemy import Column, ForeignKey, Integer, Text

from models.base import CustomModel


class Comment_Tbl(CustomModel):

    __tablename__ = "comments"

    comment_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    comment_text = Column(
        Text,
        nullable=False
    )

    comment_ticket_id = Column(
        Integer,
        ForeignKey("tickets.ticket_id"),
        nullable=False
    )

    comment_user_id = Column(
        Integer,
        ForeignKey("users.user_id"),
        nullable=False
    )