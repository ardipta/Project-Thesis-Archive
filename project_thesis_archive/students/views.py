from django.shortcuts import render
from django.contrib import messages
from .models import ProjectDocument, ThesisPaper
from django.core.files.storage import FileSystemStorage


def student_choice(request):
    return render(request, 'dashboard/student_dashboard_choice.html')


def project_upload(request):
    if request.method == 'POST' and request.FILES['projectFile'] and request.FILES['docFile'] and request.FILES['thumbnail']:
        project_name = request.POST["project_name"]
        semester_name = request.POST["semester_name"]
        course_name = request.POST["course_name"]
        course_code = request.POST["course_code"]
        section = request.POST['section']
        description = request.POST['desc']
        project_file = request.FILES['projectFile']
        doc_file = request.FILES['docFile']
        thumbnail = request.FILES['thumbnail']
        fs = FileSystemStorage()
        fs1 = FileSystemStorage()
        fs2 = FileSystemStorage()
        obj = ProjectDocument.objects.create(project_name=project_name, semester_name=semester_name,
                                             course_name=course_name, course_code=course_code, section=section,  description=description)
        obj.save()
        project_name = fs.save(project_file.name, project_file)
        doc_name = fs1.save(doc_file.name, doc_file)
        thumbnail = fs2.save(thumbnail.name, thumbnail)
        uploaded_file_url = fs.url(project_name)
        uploaded_file_url1 = fs1.url(doc_name)
        uploaded_file_url2 = fs2.url(thumbnail)
        return render(request, 'dashboard/project_upload.html', {
            'uploaded_file_url': uploaded_file_url, 'uploaded_file_url1': uploaded_file_url1, 'uploaded_file_url2': uploaded_file_url2,
        })
    return render(request, 'dashboard/project_upload.html')


def thesis_upload(request):
    if request.method == 'POST' and request.FILES['thesis_up'] and request.FILES['thumbnail']:
        thesis_title = request.POST["thesis_title"]
        semester_name = request.POST["semester_name"]
        course_name = request.POST["course_name"]
        course_code = request.POST["course_code"]
        section = request.POST['section']
        description = request.POST['desc']
        thesis_file = request.FILES['thesis_up']
        thumbnail = request.FILES['thumbnail']
        fs = FileSystemStorage()
        fs1 = FileSystemStorage()
        obj = ThesisPaper.objects.create(thesis_title=thesis_title, semester_name=semester_name,
                                         course_name=course_name, course_code=course_code, section=section, description=description)
        obj.save()
        messages.success(request, 'Upload Successful')
        thesis_file = fs.save(thesis_file.name, thesis_file)
        thumbnail = fs1.save(thumbnail.name, thumbnail)
        uploaded_file_url = fs.url(thesis_file)
        uploaded_file_url1 = fs1.url(thumbnail)
        return render(request, 'dashboard/thesis_upload.html', {
            'uploaded_file_url': uploaded_file_url, 'uploaded_file_url1': uploaded_file_url1
        })
    return render(request, 'dashboard/thesis_upload.html')
