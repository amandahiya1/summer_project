from pydantic import BaseModel, EmailStr
from datetime import date


class UserBase(BaseModel):
    name: str
    email: EmailStr


class TeacherBase(UserBase):
    t_id: int

    class Config:
        orm_mode = True


class StudentBase(UserBase):
    s_id: int

    class Config:
        orm_mode = True


class CreateStudent(UserBase):
    password: str


class CreateTeacher(UserBase):
    password: str


class SubjectBase(BaseModel):
    sub_id: int
    sub_name: str
    t_id: int

    class Config:
        orm_mode = True


class AttendanceBase(BaseModel):
    a_id: int
    s_id: int
    sub_id: int
    date: date
    attendance: int

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str
