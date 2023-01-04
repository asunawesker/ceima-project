from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import StudentsGroup, Subject

class CreateUserForm(UserCreationForm):
	password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'placeholder':'Contraseña'})
    )

	password2 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'placeholder':'Confirmar contraseña'})
    )

	class Meta:
		model = User
		widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Usuario'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Correo electrónico'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Nombre'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Apellidos'}),
        }
		fields = ['username', 'email', 'first_name', 'last_name']

class UpdateUserForm(UserCreationForm):
	password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'placeholder':'Contraseña'})
    )

	password2 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password', 'placeholder':'Confirmar contraseña'})
    )

	class Meta:
		model = User
		fields = ['password1', 'password2']

class StudentsGroupForm(ModelForm):
    class Meta:
        model = StudentsGroup
        fields = ['grade', 'group']

class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'
