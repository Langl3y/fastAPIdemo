from sqlalchemy import Boolean, Column, Integer, String, DateTime, func, ForeignKey
from database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(50), unique=False)
    email = Column(String(50), unique=False)
    role = Column(String(50), unique=False)
    is_disabled = Column(Boolean, default=False)
