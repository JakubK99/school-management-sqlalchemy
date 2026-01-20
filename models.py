from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Student(Base):
    __tablename__ = "student"
    StudentID = Column(Integer, primary_key=True)
    Name = Column(String)
    DegreeProgram = Column(String)

class Professor(Base):
    __tablename__ = "professor"
    ProfessorID = Column(Integer, primary_key=True)
    Name = Column(String)

class Course(Base):
    __tablename__ = "course"
    CourseID = Column(Integer, primary_key=True)
    Name = Column(String)
    Credits = Column(Integer)
    ProfessorID = Column(Integer, ForeignKey("professor.ProfessorID"))

class Exam(Base):
    __tablename__ = "exam"
    ExamID = Column(Integer, primary_key=True)
    ExamDate = Column(Date)
    Grade = Column(Integer)
    StudentID = Column(Integer, ForeignKey("student.StudentID"))
    CourseID = Column(Integer, ForeignKey("course.CourseID"))

