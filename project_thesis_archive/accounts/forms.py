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
    class Meta:
        model = Account
        fields = ('student_id', 'password')

        def clean(self):
            if self.is_valid():
                email = self.cleaned_data['email']
                password = self.cleaned_data['password']
                if not authenticate(email=email, password=password):
                    raise forms.ValidationError("Invalid login")


class TeacherLoginForm(forms.Form):
    class Meta:
        model = Account
        fields = ('employee_id', 'password')

        def clean(self):
            if self.is_valid():
                email = self.cleaned_data['email']
                password = self.cleaned_data['password']
                if not authenticate(email=email, password=password):
                    raise forms.ValidationError("Invalid login")
