from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('homepage')
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func

def teacher_only(view_func):
	def wrapper_function(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name

		if group == 'teacher':
			return view_func(request, *args, **kwargs)
		else:
			return HttpResponse('You are not authorized to view this page')

	return wrapper_function

def admin_only(view_func):
	def wrapper_function(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name

		if group == 'admin':
			return view_func(request, *args, **kwargs)
		else:
			return HttpResponse('You are not authorized to view this page')

	return wrapper_function
