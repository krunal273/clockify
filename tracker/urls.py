from django.urls import path

from . import views

urlpatterns = [
    path('tracker/', views.index, name='index'),
]
