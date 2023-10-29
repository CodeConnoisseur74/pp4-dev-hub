from django.shortcuts import render
from django.http import HttpResponse  # noqa: F401
from .models import Project

projectsList = [
    {
        "id": "1",
        "title": "Ecommerce Website",
        "description": "Fully functional ecommerce website",
    },
    {
        "id": "2",
        "title": "Portfolio Website",
        "description": "A Project from my portfolio",
    },
    {
        "id": "3",
        "title": "Social Network",
        "description": "Awesome project in progress",
    },
]


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, "projects/projects.html", context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, "projects/single-project.html",{'projectObj': project})
