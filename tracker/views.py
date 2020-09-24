from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from datetime import datetime

# Create your views here.
from .forms import ActivityForm, ProjectForm
from .models import Activity, Project


def index(request):
    """  """
    formActivity = ActivityForm
    formProject = ProjectForm
    activity = Activity.objects.all()

    context = {'formActivity': formActivity,
               'formProject': formProject, 'activity': activity}
    return render(request, 'tracker/activity.html', context)


@require_POST
def add(request):
    form = ActivityForm(request.POST)

    if form.is_valid():

        title = request.POST['title']
        project = Project.objects.get(id=request.POST['project'])

        tracker = Activity(title=title, startTime=datetime.now(),
                           endTime=datetime.now(), project=project)

        tracker.save()

    return redirect('index')


@require_POST
def project(request):
    form = ProjectForm(request.POST)

    if form.is_valid():
        title = request.POST['title']
        project = Project(title=title)
        project.save()

    return redirect('index')
