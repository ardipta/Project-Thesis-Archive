from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from accounts.models import Account


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


class StudentLoginForm(forms.Form):
    password = forms.CharField(label='password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('student_id', 'password')

        def clean(self):
            if self.is_valid():
                student_id = self.cleaned_data['student_id']
                password = self.cleaned_data['password']
                if not authenticate(student_id=student_id, password=password):
                    raise forms.ValidationError("Invalid login")


class TeacherLoginForm(forms.Form):
    password = forms.CharField(label='password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('employee_id', 'password')

        def clean(self):
            if self.is_valid():
                employee_id = self.cleaned_data['employee_id']
                password = self.cleaned_data['password']
                if not authenticate(employee_id=employee_id, password=password):
                    raise forms.ValidationError("Invalid login")