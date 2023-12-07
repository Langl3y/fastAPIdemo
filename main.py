from fastapi import FastAPI
from routers import students
from models import Base
from database import engine

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(students.router, prefix="/students")


@app.get("/")
def root():
    return {"message": "Welcome to my FastAPI demo"}
