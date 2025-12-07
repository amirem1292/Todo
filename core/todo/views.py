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

# create a new Task
class TaskCreateView(CreateView):
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy('todo:task-list')

# change the is_done field
class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskUpdateForm
    success_url = reverse_lazy('todo:task-list')
    template_name = 'todo/task_update.html'

# delete tasks
class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('todo:task-list')

    def get_context_data(self, **kwargs):
        context = super(TaskDeleteView, self).get_context_data(**kwargs)
        context['task'] = Task.objects.get(pk=self.kwargs['pk'])
        return context
