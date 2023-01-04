from django.contrib import admin
from .models import Student, StudentsGroup, Subject, Note

# Register your models here.
admin.site.register(Student)
admin.site.register(StudentsGroup)
admin.site.register(Subject)
admin.site.register(Note)
