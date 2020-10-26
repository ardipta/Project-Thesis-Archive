from django.shortcuts import render
from students.models import ProjectDocument, ThesisPaper


def index(request):
    get_method = request.GET.copy()
    # desc = get_method.get('desc')
    # name = get_method.get('name')
    keywords = get_method.get('keywords')
    title = get_method.get('title')
    projects = ProjectDocument.objects.order_by('-uploaded_at')[:4]
    # thesis = ThesisPaper.objects.order_by('-uploaded_at')[:2]
    # thesis_files = ThesisPaper.objects.all()
    projects_files = ProjectDocument.objects.all()
    # if desc is not None:
    #     desc = get_method['desc']
    #     thesis_files = thesis_files.filter(description__icontains=desc)
    # if name is not None:
    #     name = get_method['name']
    #     thesis_files = thesis_files.filter(thesis_title__icontains=name)
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
        # 'thesis_files': thesis_files,
    }
    return render(request, 'pages/index.html', context)
