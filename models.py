from sqlalchemy import Boolean, Column, Integer, String, DateTime, func
from database import Base


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True)
    age = Column(Integer, unique=False)
    course = Column(String(50), unique=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    is_deleted = Column(Boolean, default=False)