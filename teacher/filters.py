from django import forms
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

class StudentsForGroupFilter(django_filters.FilterSet):
    subject = CharFilter(
              field_name='subject__subject',
              lookup_expr='iexact',
              widget=forms.TextInput(attrs={"max_length":"100", 'placeholder':'Nombre materia', "class":"form-control rounded"}))

    class Meta:
        model = Notes
        fields = ['subject']
