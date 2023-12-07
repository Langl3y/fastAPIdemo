from pydantic import BaseModel
from typing import Optional


class CreateStudentsDeserializer(BaseModel):
    name: str
    age: int
    course: str


class GetStudentsDeserializer(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    age: Optional[int] = None
    course: Optional[str] = None
    is_deleted: Optional[bool] = None


class UpdateStudentsDeserializer(BaseModel):
    id: int
    name: Optional[str] = None
    age: Optional[int] = None
    course: Optional[str] = None
    is_deleted: Optional[bool] = None


class DeleteStudentDeserializer(BaseModel):
    id: int
