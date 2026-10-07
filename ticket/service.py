from sqlalchemy.orm import Session

from common.model_helper import ModelHelper
from models.ticket import Ticket_Tbl
from ticket.schema import TicketCreate, TicketUpdate


def create_ticket(db: Session, ticket: TicketCreate):

    new_ticket = ModelHelper.from_schema(
        Ticket_Tbl,
        ticket
    )

    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)

    return new_ticket


def get_tickets(db: Session):

    return db.query(Ticket_Tbl).all()


def get_ticket_by_id(
    db: Session,
    ticket_id: int
):

    return db.query(Ticket_Tbl).filter(
        Ticket_Tbl.ticket_id == ticket_id
    ).first()


def update_ticket(
    db: Session,
    ticket_id: int,
    ticket: TicketUpdate
):

    existing_ticket = db.query(Ticket_Tbl).filter(
        Ticket_Tbl.ticket_id == ticket_id
    ).first()

    if not existing_ticket:
        return None

    existing_ticket.ticket_title = ticket.ticket_title
    existing_ticket.ticket_description = ticket.ticket_description
    existing_ticket.ticket_status = ticket.ticket_status
    existing_ticket.ticket_user_id = ticket.ticket_user_id

    db.commit()
    db.refresh(existing_ticket)

    return existing_ticket


def delete_ticket(
    db: Session,
    ticket_id: int
):

    existing_ticket = db.query(Ticket_Tbl).filter(
        Ticket_Tbl.ticket_id == ticket_id
    ).first()

    if not existing_ticket:
        return None

    db.delete(existing_ticket)
    db.commit()

    return {
        "message": "Ticket deleted successfully"
    }