from datetime import date
from sqlalchemy.orm import Session
from db.models.period import Period

def get_current_period(db: Session) -> Period | None:
    today = date.today()
    
    return db.query(Period).filter(
        Period.start_date <= today,
        Period.end_date >= today
    ).first()
