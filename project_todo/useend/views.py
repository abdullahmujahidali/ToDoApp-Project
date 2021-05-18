from django.shortcuts import render
from django.http import HttpResponse

def taskList(request):
    return HttpResponse('My To Do List')