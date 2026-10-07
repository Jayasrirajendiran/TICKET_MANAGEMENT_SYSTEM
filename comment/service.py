from sqlalchemy.orm import Session

from common.model_helper import ModelHelper
from comment.schema import CommentCreate, CommentUpdate
from models.comment import Comment_Tbl


def create_comment(
    db: Session,
    comment: CommentCreate
):

    new_comment = ModelHelper.from_schema(
        Comment_Tbl,
        comment
    )

    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)

    return new_comment


def get_comments(db: Session):

    return db.query(Comment_Tbl).all()


def get_comment_by_id(
    db: Session,
    comment_id: int
):

    return db.query(Comment_Tbl).filter(
        Comment_Tbl.comment_id == comment_id
    ).first()


def update_comment(
    db: Session,
    comment_id: int,
    comment: CommentUpdate
):

    existing_comment = db.query(Comment_Tbl).filter(
        Comment_Tbl.comment_id == comment_id
    ).first()

    if not existing_comment:
        return None

    existing_comment.comment_text = comment.comment_text
    existing_comment.comment_ticket_id = comment.comment_ticket_id
    existing_comment.comment_user_id = comment.comment_user_id

    db.commit()
    db.refresh(existing_comment)

    return existing_comment


def delete_comment(
    db: Session,
    comment_id: int
):

    existing_comment = db.query(Comment_Tbl).filter(
        Comment_Tbl.comment_id == comment_id
    ).first()

    if not existing_comment:
        return None

    db.delete(existing_comment)
    db.commit()

    return {
        "message": "Comment deleted successfully"
    }