from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('homepage', views.homepage, name='homepage'),
    path('total_students', views.total_students, name='total_students'),
    path('school_record', views.school_record, name='school_record'),
    path('total_groups', views.total_groups, name='total_groups'),
    path('users', views.users, name='users'),
    path('subjects', views.subjects, name='subjects'),
]