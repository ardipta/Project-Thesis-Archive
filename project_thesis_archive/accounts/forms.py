from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from accounts.models import Account, StudentProfile


class TeacherRegistration(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.')

    class Meta:
        model = Account
        fields = (
            'email',
            'username',
            'employee_id',
            'password1',
            'password2',
        )


class StudentRegistration(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.')

    class Meta:
        model = Account
        fields = (
            'email',
            'username',
            'student_id',
            'password1',
            'password2',
        )


class StudentEditProfileForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = (
            'email',
            'username',
            'student_id',
        )


class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = (
            'full_name',
            'phone',
            'address',
            'date_of_birth',
            'blood_group',
            'gender',
            'department',
            'religion',
            'image'
        )


class StudentLoginForm(forms.Form):
    class Meta:
        model = Account
        fields = ('email', 'password')

        def clean(self):
            if self.is_valid():
                email = self.cleaned_data['email']
                password = self.cleaned_data['password']
                if not authenticate(email=email, password=password):
                    raise forms.ValidationError("Invalid login")


class TeacherLoginForm(forms.Form):
    class Meta:
        model = Account
        fields = ('email', 'password')

        def clean(self):
            if self.is_valid():
                email = self.cleaned_data['email']
                password = self.cleaned_data['password']
                if not authenticate(email=email, password=password):
                    raise forms.ValidationError("Invalid login")
