from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'pages/index.html')


def student_register(request):
    if request.method == "POST":
        method_dict = request.POST.copy()
        s_name = method_dict.get('s_name')
        s_email = method_dict.get('s_email')
        s_id = method_dict.get('s_id')
        s_password = method_dict.get('s_password')
        s_re_password = method_dict.get('s_re_password')

        if s_password != s_re_password:
            messages.error(request, 'Password does not match!!')
        elif s_password == s_re_password:
            if User.objects.filter(s_id=s_id).exists():
                messages.error(request, 'Student ID already exists!')
            else:
                if User.objects.filter(s_email=s_email).exists():
                    messages.error(request, 'Email already exists!')
                else:
                    User.objects.create_user(
                        s_name=s_name,
                        s_email=s_email,
                        s_id=s_id,
                        s_password=s_password
                    )
                    messages.success(request, 'Registration successfully completed!!!')
