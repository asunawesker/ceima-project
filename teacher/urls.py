from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('homepage/', views.homepage, name='homepage'),
    path('homepage_admin/', views.homepage_admin, name='homepage_admin'),
    path('logout/', views.logout_user, name="logout"),
    path('total_students/', views.total_students, name='total_students'),
    path('single_student/<str:student_id>/', views.single_student, name='single_student'),
    path('total_groups/', views.total_groups, name='total_groups'),
    path('students_for_group/<str:group_id>/', views.students_for_group, name='students_for_group'),
    path('upload_grades/', views.upload_grades, name='upload_grades'),
]
