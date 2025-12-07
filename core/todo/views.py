from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *


# Create your views here.
# a view to show tasks as a list
class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'
    ordering = ['-created_at']

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy('todo:task-list')
