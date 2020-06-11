from django.shortcuts import render
from .models import Project


def index(request):
    projects = Project.objects.all()
    return render(request, 'projects/index.html', {'projects': projects})


def detail(request):
    # TODO: how can I get a single object from the database again?
    return render(request, 'projects/detail.html', {'project': project})
