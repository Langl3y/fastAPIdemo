from sqlalchemy.orm import Session
import models
from basemodels import CreateStudentsDeserializer, GetStudentsDeserializer, UpdateStudentsDeserializer
from typing import Optional


def create_student(db: Session, student: CreateStudentsDeserializer):
    db_student = models.Student(**student.model_dump())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)

    return db_student


def get_students(db: Session, students: Optional[GetStudentsDeserializer] = None):
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

    return db_students


def update_students(id: int, student: UpdateStudentsDeserializer, db: Session):
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

    return db_student


def delete_student(id: int, db: Session):
    db_student = db.query(models.Student).filter(models.Student.id == id).first()
    db_student.is_deleted = True
    db.commit()

    return db_student
