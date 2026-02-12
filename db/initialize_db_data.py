from passlib.context import CryptContext

from sqlalchemy.orm import Session
from db.models.student import Student
from db.models.course import Course
from db.models.enrollment import Enrollment
from db.models.score import Score

pw_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

def initialize_db_data(db: Session) -> None:
    if (db.query(Student).first()):
        return
    
    jane = Student(username='jane123', password=pw_context.hash("test123"))
    peter = Student(username='peter123', password=pw_context.hash("peter123"))

    course1 = Course(course_code='CS103', course_name="Intro to programming")
    course2 = Course(course_code='ECO101', course_name="Macro-economics")
    course3 = Course(course_code='PSY101', course_name="Intro to psychology")
    course4 = Course(course_code='CHEM104', course_name="Chemistry II")
    course5 = Course(course_code='MATH104', course_name="Calculus II")
    course6 = Course(course_code='THTR101', course_name="Intro to theater")

    jane.enrollments = [
        Enrollment(course=course1, score=Score(value=93)),
        Enrollment(course=course2, score=Score(value=80)),
        Enrollment(course=course3, score=Score(value=85)),
        Enrollment(course=course4, score=Score(value=98)),
        Enrollment(course=course5, score=Score(value=79)),
        Enrollment(course=course6, score=Score(value=95))
    ]

    peter.enrollments = [
        Enrollment(course=course1, score=Score(value=89)),
        Enrollment(course=course2, score=Score(value=98)),
        Enrollment(course=course3, score=Score(value=87)),
        Enrollment(course=course4, score=Score(value=79)),
        Enrollment(course=course5, score=Score(value=80)),
        Enrollment(course=course6, score=Score(value=100))
    ]

    db.add_all([jane, peter, course1, course2, course3, course4, course5, course6])
    db.commit()