from django.contrib import admin

# Register your models here.
from .models import Tracker
from .models import Project

admin.site.register(Tracker)
admin.site.register(Project)
