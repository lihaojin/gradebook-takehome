from pydantic import BaseModel

class CourseWithScore(BaseModel):
    course_id: int
    course_code: str
    course_name: str
    score: int | None = None

class LoginPayload(BaseModel):
    username: str
    password: str

class LoginResponse(BaseModel):
    access_token: str
    refresh_token: str
    courses: list[CourseWithScore]