from sqlalchemy import Column, Integer, String, Date, UniqueConstraint
from db.models.base import Base

class Period(Base):
    __tablename__ = "periods"

    id = Column(Integer, primary_key=True)
    label = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    