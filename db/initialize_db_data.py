from passlib.context import CryptContext
from datetime import date

from sqlalchemy.orm import Session
from db.models.student import Student
from db.models.course import Course
from db.models.enrollment import Enrollment
from db.models.score import Score
from db.models.period import Period

pw_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

def initialize_db_data(db: Session) -> None:
    if (db.query(Student).first()):
        return
    
    previous_period = Period(
        label="Fall 2025",
        start_date=date(2025, 8, 1),
        end_date=date(2025, 12, 31)
    )
    current_period = Period(
        label="Spring 2026",
        start_date=date(2026, 1, 1),
        end_date=date(2026, 5, 31)
    )
    
    jane = Student(username='jane123', password=pw_context.hash("test123"))
    peter = Student(username='peter123', password=pw_context.hash("peter123"))

    course1 = Course(course_code='CS103', course_name="Intro to programming", period=current_period)
    course2 = Course(course_code='ECO101', course_name="Macro-economics", period=current_period)
    course3 = Course(course_code='PSY101', course_name="Intro to psychology", period=current_period)
    course4 = Course(course_code='CHEM104', course_name="Chemistry II", period=current_period)
    course5 = Course(course_code='MATH104', course_name="Calculus II", period=current_period)
    course6 = Course(course_code='THTR101', course_name="Intro to theater", period=current_period)

    course7 = Course(course_code='CS102', course_name="Intro to programming", period=previous_period)
    course8 = Course(course_code='ECO100', course_name="Macro-economics", period=previous_period)
    course9 = Course(course_code='PSY100', course_name="Intro to psychology", period=previous_period)
    course10 = Course(course_code='CHEM103', course_name="Chemistry II", period=previous_period)
    course11 = Course(course_code='MATH103', course_name="Calculus II", period=previous_period)
    course12 = Course(course_code='THTR100', course_name="Intro to theater", period=previous_period)

    jane.enrollments = [
        Enrollment(course=course1, score=Score(value=93)),
        Enrollment(course=course2, score=Score(value=80)),
        Enrollment(course=course3, score=Score(value=85)),
        Enrollment(course=course4, score=Score(value=98)),
        Enrollment(course=course5, score=Score(value=79)),
        Enrollment(course=course6, score=Score(value=95)),
        Enrollment(course=course7, score=Score(value=89)),
        Enrollment(course=course8, score=Score(value=98)),
        Enrollment(course=course9, score=Score(value=87)),
        Enrollment(course=course10, score=Score(value=79)),
        Enrollment(course=course11, score=Score(value=80)),
        Enrollment(course=course12, score=Score(value=100))
    ]

    peter.enrollments = [
        Enrollment(course=course1, score=Score(value=89)),
        Enrollment(course=course2, score=Score(value=98)),
        Enrollment(course=course3, score=Score(value=87)),
        Enrollment(course=course4, score=Score(value=79)),
        Enrollment(course=course5, score=Score(value=80)),
        Enrollment(course=course6, score=Score(value=100)),
        Enrollment(course=course7, score=Score(value=89)),
        Enrollment(course=course8, score=Score(value=98)),
        Enrollment(course=course9, score=Score(value=87)),
        Enrollment(course=course10, score=Score(value=79)),
        Enrollment(course=course11, score=Score(value=80)),
        Enrollment(course=course12, score=Score(value=100))
    ]

    db.add_all([
        previous_period,
        current_period,
        jane,
        peter,
        course1,
        course2,
        course3,
        course4,
        course5,
        course6
    ])
    db.commit()