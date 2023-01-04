from django.contrib import admin
from .models import Student, Group, Subject, Note

# Register your models here.
admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Subject)
admin.site.register(Note)
