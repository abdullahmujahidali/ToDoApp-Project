from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
 
from .models import Task


class UserLoginView(LoginView):
    template_name = 'useend/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def user_success_url(self):
        return reverse_lazy('tasks')

class TaskList(ListView):
    model = Task
    context_object_name = 'todoTasks'


class TaskDetail(DetailView):
    model = Task
    context_object_name = 'taskDetail'
    template_name = 'useend/task.html'

class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')

