from fastapi import APIRouter, Depends, HTTPException
from api.schemas.login import LoginPayload, LoginResponse, CourseWithScore
from api.utils.authentication import verify_password, create_access_token, create_refresh_token
from db.session import get_db
from sqlalchemy.orm import Session
from db.models.student import Student

router = APIRouter()

@router.post("/login")
async def login(payload: LoginPayload, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.username == payload.username).first()
    
    if not student:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    if not verify_password(payload.password, student.password):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    data = {"sub": str(student.id), "username": student.username}
    access_token = create_access_token(data)
    refresh_token = create_refresh_token(data)

    courses = [
        CourseWithScore(
            course_id=enrollment.course.id,
            course_code=enrollment.course.course_code,
            course_name=enrollment.course.course_name,
            score=enrollment.score.value
        )
        for enrollment in student.enrollments
    ]

    return LoginResponse(
        access_token=access_token,
        refresh_token=refresh_token,
        courses=courses
    )