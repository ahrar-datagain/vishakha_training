from django.shortcuts import render, HttpResponse
from django.views import View
from django.http import JsonResponse
from .sqlalchemy_setup import get_session
from .models_sqlalchemy import Student, Teacher
from django.views.decorators.csrf import csrf_exempt
import json


def home(request):
    return JsonResponse({"hello":"yesy"})



@csrf_exempt
def create_student_teacher(request):
    session = next(get_session())

    data = json.loads(request.body)
    # Create a new student and teacher
    if 'subject' in data :
        data = Teacher(name=data['name'], subject=data['subject'])
    
    data = Student(name=data['name'], age=data['age'])

    # Add to the session and commit
    session.add(data)
    session.commit()

    return JsonResponse({'status': 'success', 'message': 'New entry added!'})


def list_students(request):
    session = next(get_session())
    
    # Query all students
    students = session.query(Student).all()
    data = [{'name': s.name, 'age': s.age, 'teachers': [t.name for t in s.teachers]} for s in students]

    return JsonResponse({'students': data})


def test_orm(request):
    session = next(get_session())

    # Deleted duplicate student and teacher entry and then unique file name migration was applied.
    students = session.query(Student).all()
    for student in students[1:3]:
        session.delete(student)
    session.commit()
    return JsonResponse({"vibe check":'yay'})


# Add multiple teachers
@csrf_exempt
def mulitple_teachers(request):
    print(json.loads(request.body))
    if request.method == 'POST':
        try:
            # Parse the JSON data from the request body
            data = json.loads(request.body)
            session = next(get_session())
            teacher_names = data.get('names', [])
            teacher_subjects = data.get('subjects', [])

            # Check if both lists have the same length
            if len(teacher_names) != len(teacher_subjects):
                return JsonResponse({"response": "Error: Mismatch between number of names and subjects."})

            # Create Teacher objects dynamically
            teachers = [Teacher(name=teacher_names[i], subject=teacher_subjects[i]) for i in range(len(teacher_names))]

            # Add the list of teachers to the session and commit
            session.add_all(teachers)
            session.commit()
            return JsonResponse({"response":"yes"})
        except json.JSONDecodeError:
            return JsonResponse({"response": "Error: Invalid JSON data"}, status=400)

# list all teachers
def list_teachers(request):
    session = next(get_session())

    teachers = session.query(Teacher).all()
    data = [{'name': s.name, 'subject': s.subject, 'students':[t.name for t in s.students]} for s in teachers]

    return JsonResponse({'teachers': data})


# Create a student with Multiple Teachers.
def student_with_multiple_teachers(request):

    session = next(get_session())
    data = json.loads(request.body)
    new_student = Student(name=data['name'], age=data['age'])
    return JsonResponse({"status":"success"})