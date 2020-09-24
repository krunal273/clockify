from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from datetime import datetime

# Create your views here.
from .forms import TrackForm
from .models import Tracker


def index(request):
    """  """
    form = TrackForm
    context = {'form': form}
    return render(request, 'tracker/index.html', context)


@require_POST
def add(request):
    form = TrackForm(request.POST)

    if form.is_valid():
        # data = {
        #     'title': request.POST['title'],
        # }

        title = request.POST['title']
        # startTime = datetime.now()

        tracker = Tracker(title=title, startTime=datetime.now(),
                          endTime=datetime.now())
        tracker.save()

    return redirect('index')
