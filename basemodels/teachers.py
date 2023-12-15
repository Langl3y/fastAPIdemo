from pydantic import BaseModel
from typing import Optional


class CreateTeachersDeserializer(BaseModel):
    name: str
    age: int
    course: str


class GetTeachersDeserializer(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    age: Optional[int] = None
    course: Optional[str] = None
    is_deleted: Optional[bool] = None


class UpdateTeacherDeserializer(BaseModel):
    id: int
    name: Optional[str] = None
    age: Optional[int] = None
    course: Optional[str] = None
    is_deleted: Optional[bool] = None


class DeleteTeacherDeserializer(BaseModel):
    id: int
