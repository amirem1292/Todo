from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import *


# Create your views here.

class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'todo/tasklist.html'
    ordering = ['-created_at']
