from django.db import models

# Create your models here.
class Group(models.Model):
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
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.fullname + " " + self.group.grade

class Subject(models.Model):
    subject = models.CharField(max_length=50)
    teacher = models.CharField(max_length=80, blank=True)
    students = models.ManyToManyField(Student, null=True)

    def __str__(self):
        return self.subject

class Notes(models.Model):
    student = models.ForeignKey(to=Student, on_delete=models.CASCADE)
    group = models.ForeignKey(to=Group, on_delete=models.CASCADE)
    subject = models.ForeignKey(to=Subject, on_delete=models.CASCADE)
    first_trimester = models.IntegerField()
    second_trimester = models.IntegerField()
    third_trimester = models.IntegerField()
