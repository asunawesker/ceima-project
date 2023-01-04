from django.urls import path
from . import views

urlpatterns = [
    # teachers
    path('', views.index, name='index'),
    path('homepage/', views.homepage, name='homepage'),
    path('logout/', views.logout_user, name="logout"),
    path('total_students/', views.total_students, name='total_students'),
    path('single_student_grade/<str:student_id>/', views.single_student_grade, name='single_student_grade'),
    path('single_student/<str:student_id>/', views.single_student, name='single_student'),
    path('total_groups/', views.total_groups, name='total_groups'),
    path('students_for_group/<str:group_id>/', views.students_for_group, name='students_for_group'),
    path('upload_grades/', views.upload_grades, name='upload_grades'),
    path('upload_grade/<str:note_id>/', views.upload_grade, name='upload_grade'),

    #admin
    path('homepage_admin/', views.homepage_admin, name='homepage_admin'),
    path('total_students_admin/', views.total_students_admin, name='total_students_admin'),
    path('total_groups_admin/', views.total_groups_admin, name='total_groups_admin'),
    path('users_admin/', views.users_admin, name='users_admin'),
    path('subjects_admin/', views.subjects_admin, name='subjects_admin'),
    path('add_group/', views.add_group, name='add_group'),
    path('add_subject/', views.add_subject, name='add_subject'),
    path('update_subject/<str:subject_id>/', views.update_subject, name='update_subject'),
    path('add_user/', views.add_user, name='add_user'),
    path('update_user/<str:teacher_id>/', views.update_user, name='update_user'),
    path('delete_group/<str:group_id>/', views.delete_group, name='delete_group'),
    path('delete_subject/<str:subject_id>/', views.delete_subject, name='delete_subject'),
    path('delete_user/<str:teacher_id>/', views.delete_user, name='delete_user'),
]
