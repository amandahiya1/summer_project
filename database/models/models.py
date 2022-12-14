from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Students(Base):
    pass

class Teachers(Base):
    pass

class Subjects(Base):
    pass

class Attendance(Base):
    pass

