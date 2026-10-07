from sqlalchemy.orm import Session

from common.model_helper import ModelHelper
from models.user import User_Tbl
from user.schema import UserCreate, UserUpdate

from fastapi import HTTPException
from depends.auth import create_access_token


def create_user(db: Session, user: UserCreate):

    new_user = ModelHelper.from_schema(User_Tbl, user)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def get_users(db: Session):

    return db.query(User_Tbl).all()


def get_user_by_id(db: Session, user_id: int):

    return db.query(User_Tbl).filter(
        User_Tbl.user_id == user_id
    ).first()


def update_user(
    db: Session,
    user_id: int,
    user: UserUpdate
):

    existing_user = db.query(User_Tbl).filter(
        User_Tbl.user_id == user_id
    ).first()

    if not existing_user:
        return None

    existing_user.user_name = user.user_name
    existing_user.user_email = user.user_email
    existing_user.user_password = user.user_password
    existing_user.user_role = user.user_role

    db.commit()
    db.refresh(existing_user)

    return existing_user


def delete_user(db: Session, user_id: int):

    existing_user = db.query(User_Tbl).filter(
        User_Tbl.user_id == user_id
    ).first()

    if not existing_user:
        return None

    db.delete(existing_user)
    db.commit()

    return {
        "message": "User deleted successfully"
    }


def login_user(db: Session, user_email: str, user_password: str):
    user = db.query(User_Tbl).filter(
        User_Tbl.user_email == user_email
    ).first()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    if user.user_password != user_password:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    token = create_access_token({
        "user_id": user.user_id,
        "user_name": user.user_name,
        "user_email": user.user_email,
        "user_role": user.user_role
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }