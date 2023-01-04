from django.urls import path
from . import views

urlpatterns = [
    # teachers
    path('', views.index, name='index'),
    path('homepage/', views.homepage, name='homepage'),
    path('logout/', views.logout_user, name="logout"),
    path('total_students/', views.total_students, name='total_students'),
    path('single_student/<str:student_id>/', views.single_student, name='single_student'),
    path('total_groups/', views.total_groups, name='total_groups'),
    path('students_for_group/<str:group_id>/', views.students_for_group, name='students_for_group'),
    path('upload_grades/', views.upload_grades, name='upload_grades'),

    #admin
    path('homepage_admin/', views.homepage_admin, name='homepage_admin'),
    path('total_students_admin/', views.total_students_admin, name='total_students_admin'),
    path('school_record_admin/', views.school_record_admin, name='school_record_admin'),
    path('total_groups_admin/', views.total_groups_admin, name='total_groups_admin'),
    path('users_admin/', views.users_admin, name='users_admin'),
    path('subjects_admin/', views.subjects_admin, name='subjects_admin'),
]
