from django.shortcuts import render, redirect
from accounts.forms import TeacherRegistration, StudentRegistration, StudentLoginForm, TeacherLoginForm
from django.contrib.auth import login, authenticate, logout


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


def student_login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect("index")

    if request.POST:
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            student_id = request.POST['student_id']
            password = request.POST['password']
            user = authenticate(student_id=student_id, password=password)

            if user:
                login(request, user)
                return redirect('index')
    else:
        form = StudentLoginForm()

    context['student_login_form'] = form
    return render(request, 'student_login.html', context)


def teacher_login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect("index")

    if request.POST:
        form = TeacherLoginForm(request.POST)
        if form.is_valid():
            employee_id = request.POST['employee_id']
            password = request.POST['password']
            user = authenticate(employee_id=employee_id, password=password)
            if user:
                login(request, user)
                return redirect("index")
    else:
        form = TeacherLoginForm()

    context['teacher_login_form'] = form
    return render(request, 'teacher_login.html', context)


