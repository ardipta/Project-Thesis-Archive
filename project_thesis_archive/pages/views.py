from django.shortcuts import render
from students.models import ProjectDocument
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def index(request):
    get_method = request.GET.copy()
    keywords = get_method.get('keywords')
    title = get_method.get('title')
    # projects = ProjectDocument.objects.order_by()[:4]
    # thesis = ThesisPaper.objects.order_by('-uploaded_at')[:2]
    projects_files = ProjectDocument.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(projects_files, 3)

    try:
        pages = paginator.page(page)

    except PageNotAnInteger:
        # fall back to first page
        pages = paginator.page(1)
    except EmptyPage:
        # fall back to last page
        pages = paginator.page(paginator.num_pages)

    if keywords is not None:
        keywords = get_method['keywords']
        projects_files = projects_files.filter(description__icontains=keywords)
    if title is not None:
        title = get_method['title']
        projects_files = projects_files.filter(project_name__icontains=title)
    context = {
        'get_method': get_method,
        'projects_files': projects_files,
        'pages': pages,
        # 'thesis_files': thesis_files,
    }
    return render(request, 'pages/index.html', context)

# def thesis_search(request):
#     get_method = request.GET.copy()
#     desc = get_method.get('desc')
#     name = get_method.get('name')
#     thesis_files = ThesisPaper.objects.all()
#     if desc is not None:
#         desc = get_method['desc']
#         thesis_files = thesis_files.filter(description__icontains=desc)
#     if name is not None:
#         name = get_method['name']
#         thesis_files = thesis_files.filter(thesis_title__icontains=name)
#
#     context = {
#         'get_method': get_method,
#         'thesis_files': thesis_files,
#     }
#     return render(request, 'pages/index.html', context)
