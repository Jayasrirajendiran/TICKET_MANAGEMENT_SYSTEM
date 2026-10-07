from fastapi import FastAPI
from user.router import router as user_router
from ticket.router import router as ticket_router
from comment.router import router as comment_router
app = FastAPI(title="Ticket Management System")
app.include_router(user_router)
app.include_router(ticket_router)
app.include_router(comment_router)