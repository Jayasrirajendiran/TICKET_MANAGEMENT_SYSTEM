from datetime import datetime

from pydantic import BaseModel, ConfigDict


class CommentCreate(BaseModel):

    comment_text: str
    comment_ticket_id: int
    comment_user_id: int


class CommentUpdate(BaseModel):

    comment_text: str
    comment_ticket_id: int
    comment_user_id: int


class CommentResponse(BaseModel):

    comment_id: int
    comment_text: str
    comment_ticket_id: int
    comment_user_id: int
    started_date: datetime
    updated_date: datetime

    model_config = ConfigDict(
        from_attributes=True
    )