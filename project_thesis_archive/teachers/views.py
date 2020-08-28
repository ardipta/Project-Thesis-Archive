from django.shortcuts import render

from accounts.models import Account
from teachers.form_choices import Semester_Choices, Course_Choices, Course_Code_Choices, Section_Choices


# Create your views here.

def teacher_choice(request):
    context = {
        'Semester_Choices': Semester_Choices,
        'Course_Choices': Course_Choices,
        'Course_Code_Choices': Course_Code_Choices,
        'Section_Choices': Section_Choices
    }
    return render(request, 'dashboard/teacher_dashboard_choice.html', context)


def teacher_show(request):
    objs = Account.objects.all()
    context = {
        'objs': objs,
    }
    return render(request, 'dashboard/teacher_show_info.html', context)
