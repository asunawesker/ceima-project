from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Student, Subject, Group, Notes
from .filters import TotalStudentFilter, StudentsForGroupFilter
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
    subjects = Subject.objects.all()

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
    notes = Notes.objects.filter(student_id=student_id)

    context = {
        'student': student,
        'notes': notes
    }

    return render(request, "teachers/single_student.html", context)

@login_required(login_url='index')
@teacher_only
def total_groups(request):
    groups = Group.objects.all()

    context = {
        'groups': groups
    }

    return render(request, "teachers/total_groups.html", context)

@login_required(login_url='index')
@teacher_only
def students_for_group(request, group_id):
    group = Group.objects.get(id=group_id)
    notes = Notes.objects.filter(group_id=group_id)

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
    return render(request, "teachers/total_students_admin.html")

@login_required(login_url='index')
@admin_only
def school_record_admin(request):
    return render(request, "teachers/school_record_admin.html")

@login_required(login_url='index')
@admin_only
def total_groups_admin(request):
    return render(request, "teachers/total_groups_admin.html")

@login_required(login_url='index')
@admin_only
def users_admin(request):
    return render(request, "teachers/users_admin.html")

@login_required(login_url='index')
@admin_only
def subjects_admin(request):
    return render(request, "teachers/subjects_admin.html")
