from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint, CheckConstraint
from sqlalchemy.orm import relationship
from db.models.base import Base

class Score(Base):
    __tablename__ = "scores"

    id = Column(Integer, primary_key=True)
    value = Column(Integer, nullable=False)

    enrollment_id = Column(Integer, ForeignKey("enrollments.id"), unique=True, nullable=False)
    enrollment = relationship("Enrollment", back_populates="score")
    