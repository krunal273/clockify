from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db.models import Q
from datetime import datetime

# Create your views here.
from .forms import ActivityForm, ProjectForm
from .models import Activity, Project


def tracker(request):
    """ tracker page """
    formActivity = ActivityForm
    formProject = ProjectForm
    activity = Activity.objects.order_by('-startTime')

    context = {'formActivity': formActivity,
               'formProject': formProject, 'activity': activity}
    return render(request, 'tracker/activity.html', context)


@require_POST
def add(request):
    form = ActivityForm(request.POST)

    if form.is_valid():

        title = request.POST['title']
        project = Project.objects.get(id=request.POST['project'])

        tracker = Activity(
            title=title, startTime=datetime.now(), project=project)

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


def complete(request, activity_id):
    activity = Activity.objects.get(pk=activity_id)
    activity.complete = True
    activity.endTime = datetime.now()
    activity.totalTime = (
        activity.endTime - activity.startTime.replace(tzinfo=None)).total_seconds()
    activity.save()

    return redirect('index')


def dashboard(request):
    return render(request, 'tracker/dashboard.html')


def fetchData(request):
    print(request.method)
    activities = list(Activity.objects.values('startTime', 'totalTime'))
    return JsonResponse({'data': activities})


def search(request):
    if request.method == 'GET':
        query = request.GET.get('q')

        if query is not None:
            lookups = Q(title__icontains=query)

            activity = Activity.objects.filter(lookups).distinct()

            context = {'activity': activity}

            return render(request, 'tracker/search.html', context)

        else:
            return render(request, 'tracker/search.html')

    else:
        return render(request, 'tracker/search.html')
