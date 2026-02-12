from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.models.base import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    enrollments = relationship("Enrollment", back_populates="student")