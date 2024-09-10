from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# Create a base class for our models
Base = declarative_base()

# Association table for the many-to-many relationship between students and teachers
student_teacher_association = Table('student_teacher', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id'), primary_key=True),
    Column('teacher_id', Integer, ForeignKey('teachers.id'), primary_key=True)
)

# Student model
class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    age = Column(Integer, nullable=False)

    # Many-to-many relationship with teachers
    teachers = relationship('Teacher', secondary=student_teacher_association, back_populates='students')

    def __repr__(self):
        return f"<Student(name={self.name}, age={self.age})>"

# Teacher model
class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    subject = Column(String, nullable=False)

    # Many-to-many relationship with students
    students = relationship('Student', secondary=student_teacher_association, back_populates='teachers')

    def __repr__(self):
        return f"<Teacher(name={self.name}, subject={self.subject})>"
