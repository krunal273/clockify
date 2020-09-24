from django.urls import path

from . import views

urlpatterns = [
    path('', views.tracker, name='index'),
    path('add', views.add, name='add'),
    path('project', views.project, name='project'),
    path('complete/<activity_id>', views.complete, name='complete'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('fetch-data', views.fetchData, name="fetch-data")
]
