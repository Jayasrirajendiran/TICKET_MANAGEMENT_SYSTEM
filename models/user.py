from sqlalchemy import Column, Integer, String

from models.base import CustomModel


class User_Tbl(CustomModel):

    __tablename__ = "users"

    user_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_name = Column(
        String(100),
        nullable=False
    )

    user_email = Column(
        String(150),
        unique=True,
        nullable=False,
        index=True
    )

    user_password = Column(
        String(255),
        nullable=False
    )

    user_role = Column(
        String(50),
        nullable=False
    )