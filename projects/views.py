from django.shortcuts import render
from django.http import HttpResponse  # noqa: F401
from .models import Project
#from .forms import ProjectForm


def createProject(request):
    projects, search_query = () #searchProjects(request)
    custom_range, projects = () #paginateProjects(request, projects, 6)

    context = {
        "projects": projects,
        "search_query": search_query,
        "custom_range": custom_range,
    }
    return render(request, "projects/projects.html", context)


def projects(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "projects/projects.html", context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, "projects/single-project.html", {"project": projectObj})
