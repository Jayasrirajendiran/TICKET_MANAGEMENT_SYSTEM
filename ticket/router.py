from fastapi.responses import FileResponse

from reports.excel_report import generate_ticket_report
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.database import get_db
from depends.auth import get_current_user

from ticket.schema import TicketCreate, TicketUpdate

from ticket.service import (
    create_ticket,
    get_tickets,
    get_ticket_by_id,
    update_ticket,
    delete_ticket
)


router = APIRouter(
    prefix="/tickets",
    tags=["Tickets"]
)


@router.post("/")
def create_ticket_api(
    ticket: TicketCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return create_ticket(db, ticket)


@router.get("/")
def get_all_tickets(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return get_tickets(db)


@router.get("/{ticket_id}")
def get_ticket_api(
    ticket_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return get_ticket_by_id(db, ticket_id)


@router.put("/{ticket_id}")
def update_ticket_api(
    ticket_id: int,
    ticket: TicketUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return update_ticket(db, ticket_id, ticket)


@router.delete("/{ticket_id}")
def delete_ticket_api(
    ticket_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return delete_ticket(db, ticket_id)


@router.get("/report/excel")
def download_ticket_report(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    file_path = generate_ticket_report(db)

    return FileResponse(
        path=file_path,
        filename="ticket_report.xlsx",
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )