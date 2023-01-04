from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class StudentsGroup(models.Model):
    GRADE_OPTIONS = (
        ('Primero', 'Primero'),
        ('Segundo', 'Segundo'),
        ('Tercero', 'Tercero'),
    )

    GROUP_SELECTION = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
    )

    grade = models.CharField(max_length=7, choices=GRADE_OPTIONS)
    group = models.CharField(max_length=1, choices=GROUP_SELECTION)

    def __str__(self):
        return self.grade + " " + self.group

class Student(models.Model):
    fullname = models.CharField(max_length=100)
    group = models.ForeignKey(StudentsGroup, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.fullname + " " + self.group.grade

class Subject(models.Model):
    subject = models.CharField(max_length=50)
    teacher = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, null=True)

    def __str__(self):
        return self.subject

class Note(models.Model):
    student = models.ForeignKey(to=Student, on_delete=models.CASCADE)
    group = models.ForeignKey(to=StudentsGroup, on_delete=models.CASCADE)
    subject = models.ForeignKey(to=Subject, on_delete=models.CASCADE)
    first_trimester = models.IntegerField(null=True, blank=True)
    second_trimester = models.IntegerField(null=True, blank=True)
    third_trimester = models.IntegerField(null=True, blank=True)
