from fastapi import FastAPI
from routers import students

app = FastAPI()

app.include_router(students.router, prefix="/students")


@app.get("/")
def root():
    return {"message": "Welcome to my FastAPI demo"}
