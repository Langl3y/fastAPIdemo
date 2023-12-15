from sqlalchemy import Boolean, Column, Integer, String, DateTime, func, ForeignKey
from database import Base


class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(50), unique=False)
    age = Column(Integer, unique=False)
    course = Column(String(50), unique=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    is_deleted = Column(Boolean, default=False)
