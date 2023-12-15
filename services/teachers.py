from sqlalchemy.orm import Session
import models
from basemodels import (CreateTeachersDeserializer,
                        GetTeachersDeserializer,
                        UpdateTeacherDeserializer
                        )
from typing import Optional


def create_teacher(db: Session, teacher: CreateTeachersDeserializer):
    db_teacher = models.Teacher(**teacher.model_dump())
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)

    return db_teacher


def get_teachers(db: Session, teachers: Optional[GetTeachersDeserializer] = None):
    filters = []

    if teachers:
        if teachers.id is not None:
            filters.append(models.Teacher.id == teachers.id)

        if teachers.name is not None:
            filters.append(models.Teacher.name == teachers.name)

        if teachers.age is not None:
            filters.append(models.Teacher.age == teachers.age)

        if teachers.course is not None:
            filters.append(models.Teacher.course == teachers.course)

        if teachers.is_deleted is not None:
            filters.append(models.Teacher.is_deleted == teachers.is_deleted)

    filters.append(models.Teacher.is_deleted == False)

    db_teachers = db.query(models.Teacher).filter(*filters).all()

    return db_teachers


def update_teacher(id: int, teacher: UpdateTeacherDeserializer, db: Session):
    db_teacher = db.query(models.Teacher).filter(models.Teacher.id == id).first()

    if db_teacher:
        if teacher.name is not None:
            db_teacher.name = teacher.name
        if teacher.age is not None:
            db_teacher.age = teacher.age
        if teacher.course is not None:
            db_teacher.course = teacher.course

        db.commit()
        db.refresh(db_teacher)

    return db_teacher


def delete_teacher(id: int, db: Session):
    db_teacher = db.query(models.Teacher).filter(models.Teacher.id == id).first()
    db_teacher.is_deleted = True
    db.commit()

    return db_teacher
