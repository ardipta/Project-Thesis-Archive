from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from students.models import ProjectDocument, ThesisPaper


def index(request):
    get_method = request.GET.copy()
    keywords = get_method.get('keywords')
    title = get_method.get('title')
    projects = ProjectDocument.objects.order_by('-uploaded_at')[:4]
    # thesis = ThesisPaper.objects.order_by('-uploaded_at')[:2]
    projects_files = ProjectDocument.objects.all()
    if keywords is not None:
        keywords = get_method['keywords']
        projects_files = projects_files.filter(description__icontains=keywords)
    if title is not None:
        title = get_method['title']
        projects_files = projects_files.filter(project_name__icontains=title)
    context = {
        'get_method': get_method,
        'projects': projects,
        'projects_files': projects_files,
    }
    return render(request, 'pages/index.html', context)
