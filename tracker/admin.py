from django.contrib import admin

# Register your models here.
from .models import Activity
from .models import Project

admin.site.register(Activity)
admin.site.register(Project)
