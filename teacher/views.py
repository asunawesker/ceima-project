from django.shortcuts import render, redirect
from django.http import HttpResponse
from teacher.forms import LoginForm

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)

def index(request):
    if request.method == 'POST':
        # create an instance of our form, and fill it with the POST data
        form = LoginForm(request.POST)
        return redirect("homepage")
    else:
        # this must be a GET request, so create an empty form
        form = LoginForm()
        
    return render(request, "teachers/index.html", {'form': form})

def homepage(request):
    return render(request, "teachers/homepage.html")

def total_students(request):
    return render(request, "teachers/total_students.html")

def single_student(request):
    return render(request, "teachers/single_student.html")

def total_groups(request):
    return render(request, "teachers/total_groups.html")

def students_for_group(request):
    return render(request, "teachers/students_for_group.html")

def upload_grades(request):
    return render(request, "teachers/upload_grades.html") 
