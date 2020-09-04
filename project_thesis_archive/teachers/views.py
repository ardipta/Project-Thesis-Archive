from django.shortcuts import render
from students.models import ProjectDocument


def teacher_dashboard(request):
    return render(request, 'dashboard/teacher_dashboard.html')


def project_choice(request):
    return render(request, 'dashboard/choice_for_project.html')


def thesis_choice(request):
    return render(request, 'dashboard/choice_for_thesis.html')


def thesis_files(request):
    return render(request, 'dashboard/thesis_files.html')


def project_files(request):
    get_method = request.GET.copy()
    semester_name = get_method.get('semester_name') or None
    course_name = get_method.get('course_name') or None
    course_code = get_method.get('course_code') or None
    section = get_method.get('section') or None
    projects = ProjectDocument.objects.all()

    if semester_name is not None:
        semester_name = get_method['semester_name']
        projects = projects.filter(semester_name__iexact=semester_name)

    if course_name is not None:
        course_name = get_method['course_name']
        projects = projects.filter(course_name__iexact=course_name)

    if course_code is not None:
        course_code = get_method['course_code']
        projects = projects.filter(course_code__iexact=course_code)

    if section is not None:
        section = get_method['section']
        projects = projects.filter(section__iexact=section)

    context = {
        'get_method': get_method,
        'projects': projects,
    }

    return render(request, 'dashboard/project_files.html', context)
