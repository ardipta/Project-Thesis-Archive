from django.shortcuts import render


# Create your views here.

def teacher_dashboard(request):
    return render(request, 'dashboard/teacher_dashboard.html')


def project_choice(request):
    return render(request, 'dashboard/choice_for_project.html')


def thesis_choice(request):
    return render(request, 'dashboard/choice_for_thesis.html')


def thesis_files(request):
    return render(request, 'dashboard/thesis_files.html')


def project_files(request):
    return render(request, 'dashboard/project_files.html')
