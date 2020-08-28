from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages, auth
from django.urls import reverse

from .models import ProjectDocument, ThesisPaper
from django.shortcuts import redirect
from django.contrib.auth.models import User


def student_choice(request):
    return render(request, 'dashboard/student_dashboard_choice.html')


def project_upload(request):
    if request.method == 'POST':
        project_name = request.POST["project_name"]
        semester_name = request.POST["semester_name"]
        course_name = request.POST["course_name"]
        course_code = request.POST["course_code"]
        section = request.POST['section']
        description = request.POST['desc']
        project_file = request.FILES['projectFile']
        document = request.FILES['docFile']
        thumbnail = request.FILES['thumbnail']
        obj = ProjectDocument.objects.create(project_name=project_name, semester_name=semester_name, document=document,
                                             thumbnail=thumbnail,
                                             course_name=course_name, course_code=course_code, section=section,
                                             description=description, project_file=project_file)
        obj.save()
        messages.success(request, 'Upload Successful')
        return render(request, 'dashboard/project_upload.html')
    return render(request, 'dashboard/project_upload.html')


def thesis_upload(request):
    if request.method == 'POST':
        thesis_title = request.POST["thesis_title"]
        semester_name = request.POST["semester_name"]
        course_name = request.POST["course_name"]
        course_code = request.POST["course_code"]
        section = request.POST['section']
        description = request.POST['desc']
        thesis_file = request.FILES['thesis_up']
        thumbnail = request.FILES['thumbnail']
        obj = ThesisPaper.objects.create(thesis_title=thesis_title, semester_name=semester_name,
                                         thesis_file=thesis_file, thumbnail=thumbnail,
                                         course_name=course_name, course_code=course_code, section=section,
                                         description=description)
        obj.save()
        messages.success(request, 'Upload Successful')
        return render(request, 'dashboard/thesis_upload.html')
    return render(request, 'dashboard/thesis_upload.html')


def view_project_details(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'You need to login first')
        return redirect("student_login")
    projects = ProjectDocument.objects.all()
    print(projects)
    context = {
        'projects': projects,
    }
    return render(request, 'dashboard/view_project_details.html', context)


def view_thesis_details(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'You need to login first')
        return redirect("student_login")
    thesis = ThesisPaper.objects.all()
    print(thesis)
    context = {
        'thesis': thesis,
    }
    return render(request, 'dashboard/view_thesis_details.html', context)


# def logout(request):
#     if request.method == "POST":
#         logout(request)
#         return HttpResponseRedirect(reverse('index'))
