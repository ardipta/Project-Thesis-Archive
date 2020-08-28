from django.shortcuts import render

from students.models import ProjectDocument, ThesisPaper


def index(request):
    projects = ProjectDocument.objects.all()
    thesis = ThesisPaper.objects.all()
    print(projects)
    print(thesis)
    context = {
        'projects': projects,
        'thesis': thesis,
    }
    return render(request, 'pages/index.html', context)
