from datetime import datetime
from zoneinfo import ZoneInfo

from sqlalchemy import Column, DateTime

from database.database import Base


IST = ZoneInfo("Asia/Kolkata")


def get_ist_time():
    return datetime.now(IST).replace(tzinfo=None)

class CustomModel(Base):
    __abstract__ = True

    started_date = Column(
        DateTime,
        default=lambda: datetime.now(IST),
        nullable=False
    )

    updated_date = Column(
        DateTime,
        default=None,
        nullable=True,
        onupdate=lambda: datetime.now(IST)
    )