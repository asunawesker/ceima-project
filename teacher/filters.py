from django import forms
from django.contrib.auth.models import User
import django_filters
from django_filters import ChoiceFilter, CharFilter
from .models import *

class TotalStudentFilter(django_filters.FilterSet):
    subject = ChoiceFilter(choices=[],
              widget=forms.Select(attrs=
                {"class":"form-control", "style":"background-color:#79986E; color: white", 'placeholder':'Materia'}),
              label="Materia")

    students = CharFilter(
               field_name='students__fullname',
               lookup_expr='icontains',
               label="Nombre estudiante",
               widget=forms.TextInput(attrs={"max_length":"100", 'placeholder':'Nombre estudiante', "class":"form-control rounded"}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['subject'].extra['choices'] = [
            (subject, subject)
            for subject in Subject.objects.values_list('subject', flat=True)
        ]

    class Meta:
        model = Subject
        fields = ['subject']

class TotalStudentAdminFilter(django_filters.FilterSet):
    group = ChoiceFilter(
        label="Grupo",
        widget=forms.Select(attrs={"class":"form-control", "style":"background-color:#79986E; color: white", 'placeholder':'Grupo'})
    )

    fullname = CharFilter(
        label="Nombre estudiante",
        widget=forms.TextInput(attrs={"max_length":"100", 'placeholder':'Nombre estudiante', "class":"form-control rounded"})
    )

    class Meta:
        model = Student
        fields = '__all__'

class TotalSubjectsAdminFilter(django_filters.FilterSet):

    subject = CharFilter(
        label="Materia",
        widget=forms.TextInput(attrs={"max_length":"100", 'placeholder':'Nombre materia', "class":"form-control rounded"})
    )

    class Meta:
        model = Subject
        fields = ['subject', 'teacher']

class TotalUsersAdminFilter(django_filters.FilterSet):
    first_name = CharFilter(
        label="Nombre docente",
        widget=forms.TextInput(attrs={"max_length":"100", 'placeholder':'Nombre docente', "class":"form-control rounded"})
    )

    last_name = CharFilter(
        label="Nombre docente",
        widget=forms.TextInput(attrs={"max_length":"100", 'placeholder':'Apellido docente', "class":"form-control rounded"})
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name']

class StudentsForGroupFilter(django_filters.FilterSet):
    subject = CharFilter(
              field_name='subject__subject',
              lookup_expr='iexact',
              widget=forms.TextInput(attrs={"max_length":"100", 'placeholder':'Nombre materia', "class":"form-control rounded"}))

    class Meta:
        model = Note
        fields = ['subject']
