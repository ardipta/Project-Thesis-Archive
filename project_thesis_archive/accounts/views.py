from django.shortcuts import render, redirect
from accounts.forms import TeacherRegistration, StudentRegistration
from django.contrib.auth import login, authenticate, logout


# from django.contrib.auth import login, authenticate
# from accounts.forms import TeacherRegistration, StudentRegistration


# def teacher_reg_view(request):
#     # if request.POST:
#     #     form = TeacherRegistration(request.POST or None)
#     #     if form.is_valid():
#     #         form.save()
#     #         email_ = form.cleaned_data.get('email')
#     #         name_ = form.cleaned_data.get('name')
#     #         emp_id = form.cleaned_data.get('employee_id')
#     #         password_ = form.cleaned_data.get('password')
#     #         account = authenticate(email=email_, name=name_, employee_id=emp_id, password=password_)
#     #         login(request, account)
#     #         return redirect('index')
#     #     else:
#     #         context = {
#     #             'form': form
#     #         }
#     # else:
#     #     form = TeacherRegistration()
#     #     context = {
#     #         'form': form
#     #     }
#     return render(request, 'teacher_reg.html')


# def student_reg_view(request):
#     # context = {}
#     # if request.POST:
#     #     form = StudentRegistration(request.POST)
#     #     if form.is_valid():
#     #         form.save()
#     #         email_ = form.cleaned_data.get('email')
#     #         name_ = form.cleaned_data.get('name')
#     #         std_id = form.cleaned_data.get('student_id')
#     #         password_ = form.cleaned_data.get('password')
#     #         account = authenticate(email=email_, name=name_, student_id=std_id, password=password_)
#     #         login(request, account)
#     #         return redirect('index')
#     #     else:
#     #         context['student_reg_form'] = form
#     # else:
#     #     form = StudentRegistration()
#     #     context['student_reg_form'] = form
#     return render(request, 'student_reg.html')


def teacher_login_view(request):
    return render(request, 'teacher_login.html')


def student_login_view(request):
    return render(request, 'student_login.html')


def teacher_reg_view(request):
    context = {}
    if request.POST:
        form = TeacherRegistration(request.POST)
        if form.is_valid():
            form.save()
            # email = form.cleaned_data.get('email')
            # raw_password = form.cleaned_data.get('password1')
            # account = authenticate(email=email, password=raw_password)
            # login(request, account)
            return redirect('index')
        else:
            context['teacher_reg_form'] = form

    else:
        form = TeacherRegistration()
        context['teacher_reg_form'] = form
    return render(request, 'teacher_reg.html', context)


def student_reg_view(request):
    context = {}
    if request.POST:
        form = StudentRegistration(request.POST)
        if form.is_valid():
            form.save()
            # email = form.cleaned_data.get('email')
            # raw_password = form.cleaned_data.get('password1')
            # account = authenticate(email=email, password=raw_password)
            # login(request, account)
            return redirect('index')
        else:
            context['student_reg_form'] = form

    else:
        form = StudentRegistration()
        context['student_reg_form'] = form
    return render(request, 'student_reg.html', context)
