from database import session
from models import Student, Professor, Course, Exam
from datetime import date

# CREATE
student = Student(StudentID=1, Name="Alice", DegreeProgram="CS")
session.add(student)

professor = Professor(ProfessorID=1, Name="Dr. Smith")
session.add(professor)

course = Course(CourseID=1, Name="Databases", Credits=6, ProfessorID=1)
session.add(course)

exam = Exam(
    ExamID=1,
    ExamDate=date.today(),
    Grade=28,
    StudentID=1,
    CourseID=1
)
session.add(exam)

session.commit()

# READ
students = session.query(Student).all()
for s in students:
    print(s.Name)

# UPDATE
student.Name = "Alice Updated"
session.commit()

# DELETE
session.delete(student)
session.commit()

