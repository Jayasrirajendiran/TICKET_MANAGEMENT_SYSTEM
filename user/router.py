from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from database.database import get_db
from depends.auth import get_current_user

from user.schema import UserCreate, UserUpdate

from user.service import (
    create_user,
    get_users,
    get_user_by_id,
    update_user,
    delete_user,
    login_user
)


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/token")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    return login_user(
        db,
        form_data.username,
        form_data.password
    )


@router.get("/me")
def get_current_user_details(
    current_user=Depends(get_current_user)
):
    return current_user


@router.post("/")
def create_user_api(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return create_user(db, user)


@router.get("/")
def get_all_users(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return get_users(db)


@router.get("/{user_id}")
def get_user_api(
    user_id: int,
    db: Session = Depends(get_db)
):
    return get_user_by_id(db, user_id)


@router.put("/{user_id}")
def update_user_api(
    user_id: int,
    user: UserUpdate,
    db: Session = Depends(get_db)
):
    return update_user(db, user_id, user)


@router.delete("/{user_id}")
def delete_user_api(
    user_id: int,
    db: Session = Depends(get_db)
):
    return delete_user(db, user_id)