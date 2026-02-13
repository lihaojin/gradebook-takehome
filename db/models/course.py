from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    course_code = Column(String, unique=True, nullable=False)
    course_name = Column(String, nullable=False)
    period_id = Column(Integer, ForeignKey("periods.id", ondelete="RESTRICT"), nullable=False)

    period = relationship("Period", back_populates="courses")
    enrollments = relationship("Enrollment", back_populates="course")