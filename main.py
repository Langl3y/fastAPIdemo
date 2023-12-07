from fastapi import FastAPI, Depends, status
from typing import Optional, Annotated
from database import engine, SessionLocal
from sqlalchemy.orm import Session

from basemodels import GetStudentsDeserializer, UpdateStudentsDeserializer, CreateStudentsDeserializer
import models
from common.responses import APIResponseMessage


app = FastAPI()
models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@app.post("/students/create_student/", status_code=status.HTTP_201_CREATED)
async def create_student(student: CreateStudentsDeserializer, db: db_dependency):
    try:
        db_student = models.Student(**student.model_dump())
        db.add(db_student)
        db.commit()
        db.refresh(db_student)

        APIResponseMessage.SUCCESSFULLY_CREATED["data"] = db_student

        return APIResponseMessage.SUCCESSFULLY_CREATED
    except Exception as e:
        return APIResponseMessage.FAILED_TO_CREATE


@app.post("/students/get_students/", status_code=status.HTTP_200_OK)
async def get_student(students: Optional[GetStudentsDeserializer] = None, db: Session = Depends(get_db)):
    filters = []

    if students:
        if students.id is not None:
            filters.append(models.Student.id == students.id)

        if students.name is not None:
            filters.append(models.Student.name == students.name)

        if students.age is not None:
            filters.append(models.Student.age == students.age)

        if students.course is not None:
            filters.append(models.Student.course == students.course)

        if students.is_deleted is not None:
            filters.append(models.Student.is_deleted == students.is_deleted)

    db_students = db.query(models.Student).filter(*filters).all()

    if not db_students:
        return APIResponseMessage.FAILED_TO_RETRIEVE

    APIResponseMessage.SUCCESSFULLY_RETRIEVED["data"] = db_students

    return APIResponseMessage.SUCCESSFULLY_RETRIEVED


@app.post("/students/update_student/", status_code=status.HTTP_200_OK)
async def update_student(id: int, student: UpdateStudentsDeserializer, db: db_dependency):
    db_student = db.query(models.Student).filter(models.Student.id == id).first()

    if db_student:
        if student.name is not None:
            db_student.name = student.name
        if student.age is not None:
            db_student.age = student.age
        if student.course is not None:
            db_student.course = student.course

        db.commit()
        db.refresh(db_student)

        APIResponseMessage.SUCCESSFULLY_UPDATED["data"] = db_student

        return APIResponseMessage.SUCCESSFULLY_UPDATED
    else:
        return APIResponseMessage.FAILED_TO_RETRIEVE


@app.post("/students/delete_student/", status_code=status.HTTP_200_OK)
async def delete_student(id: int, db: db_dependency):
    db_student = db.query(models.Student).filter(models.Student.id == id).first()

    db_student.is_deleted = True
    db.commit()

    return APIResponseMessage.SUCCESSFULLY_DELETED
