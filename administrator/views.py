from django.shortcuts import render, redirect
from django.http import HttpResponse
from administrator.forms import LoginForm

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
        
    return render(request, "administrator/index.html", {'form': form})

def homepage(request):
    return render(request, "administrator/homepage.html")

def total_students(request):
    return render(request, "administrator/total_students.html")

def school_record(request):
    return render(request, "administrator/school_record.html")

def total_groups(request):
    return render(request, "administrator/total_groups.html")

def students_for_group(request):
    return render(request, "administrator/students_for_group.html")

def users(request):
    return render(request, "administrator/users.html") 

def subjects(request):
    return render(request, "administrator/subjects.html") 
