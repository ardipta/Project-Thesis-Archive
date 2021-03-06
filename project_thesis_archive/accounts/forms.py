from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, UserChangeForm

from accounts.models import Account


class TeacherRegistration(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.')

    class Meta:
        model = Account
        fields = (
            'email',
            'fullname',
            'department',
            'designation',
            'employee_id',
            'password1',
            'password2',
            'role'

        )


class StudentRegistration(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.')

    class Meta:
        model = Account
        fields = (
            'email',
            'fullname',
            'department',
            'student_id',
            'password1',
            'password2',
            'role',

        )


class StudentEditProfileForm(UserChangeForm):
    class Meta:
        model = Account
        fields = (
            'email',
            'fullname',
            'student_id',
            'department',
            'image',
        )


class TeacherEditProfileForm(UserChangeForm):
    class Meta:
        model = Account
        fields = (
            'email',
            'fullname',
            'employee_id',
            'designation',
            'department',
            'image',
        )


#
# class StudentProfileForm(forms.ModelForm):
#     class Meta:
#         model = StudentProfile
#         fields = (
#             'phone',
#             'address',
#             'date_of_birth',
#             'blood_group',
#             'gender',
#             'department',
#             'religion',
#             'image'
#         )


class StudentLoginForm(forms.Form):
    class Meta:
        model = Account
        fields = (
            'email',
            'password',
        )

        def clean(self):
            if self.is_valid():
                email = self.cleaned_data['email']
                password = self.cleaned_data['password']
                if not authenticate(email=email, password=password):
                    raise forms.ValidationError("Invalid login")


class TeacherLoginForm(forms.Form):
    class Meta:
        model = Account
        fields = (
            'email',
            'password'
        )

        def clean(self):
            if self.is_valid():
                email = self.cleaned_data['email']
                password = self.cleaned_data['password']
                if not authenticate(email=email, password=password):
                    raise forms.ValidationError("Invalid login")


class TeacherPassChangeForm(PasswordChangeForm):
    class Meta:
        model = Account
        fields = (
            'ex-pass',
            'new-pass1',
            'new-pass2',
        )


class StudentPassChangeForm(PasswordChangeForm):
    class Meta:
        model = Account
        fields = (
            'ex-pass',
            'new-pass1',
            'new-pass2',
        )
