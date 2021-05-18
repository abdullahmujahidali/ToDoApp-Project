from django.contrib import admin
from .models import Task

# Register your models here.

admin.site.register(Task)

fields = ( 'priority')
radio_fields = {'priority': admin.VERTICAL}