from django.contrib import messages
from django.shortcuts import render, redirect
from accounts.forms import TeacherRegistration, StudentRegistration, StudentLoginForm, TeacherLoginForm
from django.contrib.auth import login, authenticate


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
            messages.success(request, 'Registration Successful')
            return redirect('teacher_reg')
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
            messages.success(request, 'Registration Successful')
            return redirect('student_reg')
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
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('student_dashboard')
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
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect("student_dashboard")
    else:
        form = TeacherLoginForm()

    context['teacher_login_form'] = form
    return render(request, 'teacher_login.html', context)