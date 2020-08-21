from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'pages/index.html')


def student(request):
    return render(request, 'pages/student_dashboard.html')
