from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from datetime import datetime

# Create your views here.
from .forms import TrackForm
from .models import Tracker, Project


def index(request):
    """  """
    form = TrackForm
    print(form)
    context = {'form': form}
    return render(request, 'tracker/index.html', context)


@require_POST
def add(request):
    form = TrackForm(request.POST)

    if form.is_valid():

        title = request.POST['title']
        project = Project.objects.get(id=request.POST['project'])

        tracker = Tracker(title=title, startTime=datetime.now(),
                          endTime=datetime.now(), project=project)

        tracker.save()

    return redirect('index')
