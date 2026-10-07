from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.database import get_db
from depends.auth import get_current_user

from comment.schema import CommentCreate, CommentUpdate

from comment.service import (
    create_comment,
    get_comments,
    get_comment_by_id,
    update_comment,
    delete_comment
)

router = APIRouter(
    prefix="/comments",
    tags=["Comments"]
)


@router.post("/")
def create_comment_api(
    comment: CommentCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return create_comment(db, comment)


@router.get("/")
def get_all_comments(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return get_comments(db)


@router.get("/{comment_id}")
def get_comment_api(
    comment_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return get_comment_by_id(db, comment_id)


@router.put("/{comment_id}")
def update_comment_api(
    comment_id: int,
    comment: CommentUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return update_comment(db, comment_id, comment)


@router.delete("/{comment_id}")
def delete_comment_api(
    comment_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return delete_comment(db, comment_id)