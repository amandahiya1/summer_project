from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Students(Base):
    __tablename__ = "students"
    s_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30), nullable=False)
    email = Column(String(40), nullable=False, unique=True)
    password = Column(String(150), nullable=False)


class Teachers(Base):
    __tablename__ = "teachers"
    t_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30), nullable=False)
    email = Column(String(40), nullable=False, unique=True)
    password = Column(String(150), nullable=False)


class Subjects(Base):
    __tablename__ = "subjects"
    sub_id = Column(Integer, primary_key=True, index=True)
    sub_name = Column(String(30), nullable=False)
    t_id = Column(Integer, ForeignKey('teachers.t_id', ondelete="CASCADE"))


class Attendance(Base):
    __tablename__ = "attendance"
    a_id = Column(Integer, primary_key=True, index=True)
    s_id = Column(Integer, ForeignKey('students.s_id', ondelete="CASCADE"))
    date = Column(Date, nullable=False)
    attendance = Column(Integer, nullable=False)
