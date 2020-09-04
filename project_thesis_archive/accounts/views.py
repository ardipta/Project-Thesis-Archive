from django.contrib import messages, auth
from django.core.cache import cache
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from accounts.forms import TeacherRegistration, StudentRegistration, StudentLoginForm, TeacherLoginForm, \
    StudentEditProfileForm, StudentProfileForm
from django.contrib.auth import login, authenticate
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.conf import settings

userprofile = settings.AUTH_PROFILE_MODULE


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
    if request.POST:
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                messages.success(request, 'Login Successful')
                # return HttpResponseRedirect(reverse('student_dashboard'))
                next_url = request.GET.get('next', 'student_dashboard')
                return redirect(next_url)
    else:
        form = StudentLoginForm()

    context['student_login_form'] = form
    return render(request, 'student_login.html', context)


def teacher_login_view(request):
    context = {}
    if request.POST:
        form = TeacherLoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect("teacher_dashboard")
    else:
        form = TeacherLoginForm()

    context['teacher_login'] = form
    return render(request, 'teacher_login.html', context)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = StudentEditProfileForm(request.POST, instance=request.user)
        profile_form = StudentProfileForm(request.POST, request.FILES, instance=request.user)

        if form.is_valid() and profile_form.is_valid():
            user_form = form.save()
            custom_form = profile_form.save(False)
            custom_form.user = user_form
            custom_form.save()
            messages.success(request, 'Profile update successful')
            return redirect('dashboard/edit_profile.html')
    else:
        form = StudentEditProfileForm(instance=request.user)
        profile_form = StudentProfileForm(instance=request.user)
        print(profile_form)
        context = {
            'form': form,
            'profile_form': profile_form
        }
        return render(request, 'dashboard/edit_profile.html', context)


def student_logout(request):
    auth.logout(request)
    return redirect('index')
