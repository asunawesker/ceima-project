from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('homepage', views.homepage, name='homepage'),
    path('total_students', views.total_students, name='total_students'),
    path('single_student', views.single_student, name='single_student'),
    path('total_groups', views.total_groups, name='total_groups'),
    path('students_for_group', views.students_for_group, name='students_for_group'),
    path('upload_grades', views.upload_grades, name='upload_grades'),
]