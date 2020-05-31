from django.shortcuts import render

from .models import Project

def index(request):
    projects = Project.objects
    return render(request, 'projects/index.html', {'projects':projects})
