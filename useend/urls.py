from django.urls import path
from django.urls.resolvers import URLPattern
from .views import TaskList
 
urlpatterns = [
    path('',TaskList.as_view(),name='tasks'),
]