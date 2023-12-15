from fastapi import APIRouter, Depends, status
from typing import Optional
from database import SessionLocal
from sqlalchemy.orm import Session

from basemodels import (
    GetTeachersDeserializer,
    UpdateTeacherDeserializer,
    CreateTeachersDeserializer,
    DeleteTeacherDeserializer
)
from common.responses import APIResponseCode
from services.teachers import (create_teacher,
                               get_teachers,
                               update_teacher,
                               delete_teacher
                               )

router = APIRouter()


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.post("/create_teacher/", status_code=status.HTTP_201_CREATED)
async def create_student_handler(student: CreateTeachersDeserializer,
                                 db: Session = Depends(get_db)):
    try:
        db_student = create_teacher(db, student)

        return APIResponseCode.SUCCESS, db_student
    except Exception as e:
        return APIResponseCode.SERVER_ERROR, {}


@router.post("/get_teachers/", status_code=status.HTTP_200_OK)
async def get_students_handler(db: Session = Depends(get_db),
                               students: Optional[GetTeachersDeserializer] = None):
    db_students = get_teachers(db, students)

    if not db_students:
        return APIResponseCode.NOT_FOUND, []

    return APIResponseCode.SUCCESS, db_students


@router.post("/update_teacher/", status_code=status.HTTP_200_OK)
async def update_student_handler(student: Optional[UpdateTeacherDeserializer],
                                 db: Session = Depends(get_db)):
    db_student = update_teacher(student.id, student, db)

    if db_student is None:
        return APIResponseCode.NOT_FOUND, {}

    return APIResponseCode.SUCCESS, db_student


@router.post("/delete_teacher/", status_code=status.HTTP_200_OK)
async def delete_student_handler(student: DeleteTeacherDeserializer,
                                 db: Session = Depends(get_db)):
    db_student = delete_teacher(student.id, db)

    if db_student is None:
        return APIResponseCode.NOT_FOUND, {}

    return APIResponseCode.SUCCESS
