from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('create_student_teacher', views.create_student_teacher, name='create_student_teacher'),
    path('list_students', views.list_students, name='list_students'),
    path("test_orm", views.test_orm, name="test_orm"),
    path('mulitple_teachers', views.mulitple_teachers, name='mulitple_teachers'),
    path('list_teachers', views.list_teachers,name='list_teachers')
]
