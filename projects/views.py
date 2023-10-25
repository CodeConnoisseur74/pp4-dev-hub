from django.shortcuts import render
from django.http import HttpResponse  # noqa: F401


def projects(request):
    page = 'projets'
    number = 10
    context = {'page': page, 'number': number, 'projects': projects}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    return render(request, 'projects/single-project.html')
