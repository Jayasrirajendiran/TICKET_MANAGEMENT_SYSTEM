from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


class UserCreate(BaseModel):

    user_name: str
    user_email: EmailStr
    user_password: str
    user_role: str


class UserUpdate(BaseModel):

    user_name: str
    user_email: EmailStr
    user_password: str
    user_role: str


class UserResponse(BaseModel):

    user_id: int
    user_name: str
    user_email: EmailStr
    user_role: str
    started_date: datetime
    updated_date: datetime

    model_config = ConfigDict(
        from_attributes=True
    )

class UserLogin(BaseModel):
    user_email: EmailStr
    user_password: str