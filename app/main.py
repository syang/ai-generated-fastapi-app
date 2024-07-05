from fastapi import FastAPI
from .routers import items
from .database import engine, Base

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

app.include_router(items.router)
