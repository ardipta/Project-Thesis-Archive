from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'pages/index.html')


def student_choice(request):
    return render(request, 'dashboard/student_dashboard_choice.html')


def project_upload(request):
    return render(request, 'dashboard/project_upload.html')


def thesis_upload(request):
    return render(request, 'dashboard/thesis_upload.html')
