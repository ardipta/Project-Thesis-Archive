from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Account


# class TeacherRegistration(UserCreationForm):
#     email = forms.EmailField(max_length=60, help_text='Required')
#
#     class Meta:
#         model = Account
#         fields = ("email", "username", "employee_id", "password", "re_password")
#
#
# class StudentRegistration(UserCreationForm):
#     email = forms.EmailField(max_length=60, help_text='Required')
#
#     class Meta:
#         model = Account
#         fields = ('email', 'name', 'student_id', 'password', 're_password')

class TeacherRegistration(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.')

    class Meta:
        model = Account
        fields = ('email', 'username', 'employee_id', 'password1', 'password2',)


class StudentRegistration(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.')

    class Meta:
        model = Account
        fields = ('email', 'username', 'student_id', 'password1', 'password2',)
