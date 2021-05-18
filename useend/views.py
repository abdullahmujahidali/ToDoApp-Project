from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView,FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Task


class CustomLoginView(LoginView):
    template_name = 'useend/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')

class RegisterPage(FormView):
    template_name='useend/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True

class TaskList(LoginRequiredMixin,ListView):
    model = Task
    context_object_name = 'todoTasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[' todoTasks'] = context['todoTasks'].filter(user=self.request.user)
        context['count'] = context['todoTasks'].filter(complete=False).count()
        return context


class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task
    context_object_name = 'taskDetail'
    template_name = 'useend/task.html'

class TaskCreate(LoginRequiredMixin,CreateView):
    model = Task
    fields = {'description','title','priority', 'complete'}
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate,self).form_valid(form)

class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Task
    fields = {'title', 'description','priority','complete'}
    success_url = reverse_lazy('tasks')

class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')

