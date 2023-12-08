from fastapi import APIRouter, Depends, status
from typing import Optional
from database import SessionLocal
from sqlalchemy.orm import Session

from basemodels import (
    GetStudentsDeserializer,
    UpdateStudentsDeserializer,
    CreateStudentsDeserializer,
    DeleteStudentDeserializer
)
from common.responses import APIResponseCode
from services.students import (create_student,
                               get_students,
                               update_students,
                               delete_student
                               )

router = APIRouter()


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.post("/create_student/", status_code=status.HTTP_201_CREATED)
async def create_student_handler(student: CreateStudentsDeserializer,
                                 db: Session = Depends(get_db)):
    try:
        db_student = create_student(db, student)

        return APIResponseCode.SUCCESS, db_student
    except Exception as e:
        return APIResponseCode.SERVER_ERROR, {}


@router.post("/get_students/", status_code=status.HTTP_200_OK)
async def get_students_handler(db: Session = Depends(get_db),
                               students: Optional[GetStudentsDeserializer] = None):
    db_students = get_students(db, students)

    if not db_students:
        return APIResponseCode.NOT_FOUND, []

    return APIResponseCode.SUCCESS, db_students


@router.post("/update_student/", status_code=status.HTTP_200_OK)
async def update_student_handler(student: Optional[UpdateStudentsDeserializer],
                                 db: Session = Depends(get_db)):
    db_student = update_students(student.id, student, db)

    if db_student is None:
        return APIResponseCode.NOT_FOUND, {}

    return APIResponseCode.SUCCESS, db_student


@router.post("/delete_student/", status_code=status.HTTP_200_OK)
async def delete_student_handler(student: DeleteStudentDeserializer,
                                 db: Session = Depends(get_db)):
    db_student = delete_student(student.id, db)

    if db_student is None:
        return APIResponseCode.NOT_FOUND, {}

    return APIResponseCode.SUCCESS, db_student
