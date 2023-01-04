from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Student, Subject, Group, Note
from .filters import TotalStudentFilter, StudentsForGroupFilter, TotalStudentAdminFilter, TotalSubjectsAdminFilter, TotalUsersAdminFilter
from .decorators import unauthenticated_user, teacher_only, admin_only

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)

@unauthenticated_user
def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            group = None
            if user.groups.exists():
                group = user.groups.all()[0].name
            if group == 'admin':
                return redirect('homepage_admin')
            return redirect('homepage')
        else:
            messages.info(request, 'Username OR password is incorrect')

    return render(request, "teachers/index.html")

def logout_user(request):
	logout(request)
	return redirect('index')

@login_required(login_url='index')
@teacher_only
def homepage(request):
    return render(request, "teachers/homepage.html")

@login_required(login_url='index')
@admin_only
def homepage_admin(request):
    return render(request, "teachers/homepage_admin.html")

@login_required(login_url='index')
@teacher_only
def total_students(request):
    subjects = request.user.subject_set.all()

    subject_filter = TotalStudentFilter(request.GET, queryset=subjects)

    subjects = subject_filter.qs

    context = {
        'subjects': subjects,
        'subject_filter': subject_filter
    }

    return render(request, "teachers/total_students.html", context)

@login_required(login_url='index')
@teacher_only
def single_student(request, student_id):
    student = Student.objects.get(id=student_id)
    notes = Note.objects.filter(student_id=student_id)

    context = {
        'student': student,
        'notes': notes
    }

    return render(request, "teachers/single_student.html", context)

@login_required(login_url='index')
@teacher_only
def total_groups(request):
    groups = []

    for subject in request.user.subject_set.all():
        for student in subject.students.all():
            groups.append(student.group)

    groups = list(dict.fromkeys(groups))

    context = {
        'groups': groups
    }

    return render(request, "teachers/total_groups.html", context)

@login_required(login_url='index')
@teacher_only
def students_for_group(request, group_id):
    group = Group.objects.get(id=group_id)
    notes = Note.objects.filter(group_id=group_id)

    notes_filter = StudentsForGroupFilter(request.GET, queryset=notes)

    notes = notes_filter.qs

    context = {
        'group': group,
        'notes': notes,
        'notes_filter': notes_filter
    }

    return render(request, "teachers/students_for_group.html", context)

@login_required(login_url='index')
@teacher_only
def upload_grades(request):
    return render(request, "teachers/upload_grades.html")

@login_required(login_url='index')
@admin_only
def total_students_admin(request):
    students = Student.objects.all()

    students_filter = TotalStudentAdminFilter(request.GET, queryset=students)

    students = students_filter.qs

    context = {
        'students': students,
        'subject_filter': students_filter
    }

    return render(request, "teachers/total_students_admin.html", context)

@login_required(login_url='index')
@admin_only
def school_record_admin(request):
    return render(request, "teachers/school_record_admin.html")

@login_required(login_url='index')
@admin_only
def total_groups_admin(request):
    groups = Group.objects.values()

    context = {
        'groups': groups
    }

    return render(request, "teachers/total_groups_admin.html", context)

@login_required(login_url='index')
@admin_only
def users_admin(request):
    teachers = []
    users = User.objects.all()

    teachers_filter = TotalUsersAdminFilter(request.GET, queryset=users)

    users = teachers_filter.qs

    for user in users:
        if is_member(user) == True:
            teachers.append(user)

    context = {
        'users': teachers,
        'teachers_filter': teachers_filter
    }

    return render(request, "teachers/users_admin.html", context)

@login_required(login_url='index')
@admin_only
def subjects_admin(request):
    subjects = Subject.objects.all()

    subjects_filter = TotalSubjectsAdminFilter(request.GET, queryset=subjects)

    subjects = subjects_filter.qs

    context = {
        'subjects': subjects,
        'subject_filter': subjects_filter
    }

    return render(request, "teachers/subjects_admin.html", context)

def is_member(user):
    return user.groups.filter(name='teacher').exists()
