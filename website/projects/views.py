from django.shortcuts import render
from .models import Project, Part


def home(request):
    projects = Project.objects.all()
    return render(request, "index.html", {"projects": projects})


def project(request, pk):
    current_project = Project.objects.get(id=pk)
    parts = Part.objects.filter(project_id=pk)
    return render(request, "project.html", {"project": current_project, "parts": parts})

