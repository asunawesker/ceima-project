from django import forms

class LoginForm(forms.Form):
   user = forms.CharField(required=False, widget=forms.TextInput(attrs={"class":"form-control", "style": "margin-bottom:20px"}))
   password = forms.CharField(required=False, widget=forms.PasswordInput(attrs={"class":"form-control" , "style": "margin-bottom:20px"}))
