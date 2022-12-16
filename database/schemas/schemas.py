from pydantic import BaseModel, EmailStr
from datetime import date


class UserBase(BaseModel):
    name: str
    email : EmailStr
    password: str

class TeacherBase(UserBase):
    t_id: int

class StudentBase(UserBase):
    s_id: int

class SubjectBase(BaseModel):
    sub_id: int
    sub_name: int
    t_id: int

class AttendanceBase(BaseModel):
    a_id: int
    s_id : int
    date: date
    attendance: int

class Token(BaseModel):
    access_token: str
    token_type: str