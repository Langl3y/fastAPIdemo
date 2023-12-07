from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Optional, Annotated

import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


class StudentBase(BaseModel):
    name: str
    age: int
    course: str



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@app.post("/students/create_student/", status_code=status.HTTP_201_CREATED)
async def create_student(student: StudentBase, db: db_dependency):
    db_student = models.Student(**student.model_dump())
    db.add(db_student)
    db.commit()

    response = {
        "status_code": status.HTTP_201_CREATED,
        "message": "Student created successfully",
        "data": db_student
    }

    return response


@app.get("/students/get_student/", status_code=status.HTTP_200_OK)
async def get_student(
        id: Optional[int] = None,
        name: Optional[str] = None,
        age: Optional[int] = None,
        course: Optional[str] = None,
        is_deleted: Optional[bool] = None,
        db: Session = Depends(get_db)
):
    filters = []

    if id is not None:
        filters.append(models.Student.id == id)
    if name is not None:
        filters.append(models.Student.name == name)
    if age is not None:
        filters.append(models.Student.age == age)
    if course is not None:
        filters.append(models.Student.course == course)
    if is_deleted is not None:
        filters.append(models.Student.is_deleted == is_deleted)

    db_students = db.query(models.Student).filter(*filters).all()

    if not db_students:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No student found")

    response = {
        "status_code": status.HTTP_200_OK,
        "message": "Students retrieved successfully",
        "data": db_students
    }

    return response


