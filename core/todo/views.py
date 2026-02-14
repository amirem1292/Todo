from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import *
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout


# Create your views here.
# a view to show tasks as a list
class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks"

    # filter tasks by their author
    def get_queryset(self):
        return Task.objects.filter(author=self.request.user).order_by(
            "created_at"
        )


# create a new Task
class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy("todo:task-list")

    # logged in user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(TaskCreateView, self).form_valid(form)


# change the is_done field
class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskUpdateForm
    success_url = reverse_lazy("todo:task-list")
    template_name = "todo/task_update.html"


# delete tasks
class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy("todo:task-list")

    # show the name of task
    def get_context_data(self, **kwargs):
        context = super(TaskDeleteView, self).get_context_data(**kwargs)
        context["task"] = Task.objects.get(pk=self.kwargs["pk"])
        return context


# there was a problem with accounts urls so, I used fbv
# login view
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                username=cd["username"], password=cd["password"]
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("todo:task-list")
    else:
        form = LoginForm()

    return render(request, "registration/login.html", {"form": form})


# log out view
def logout_view(request):
    logout(request)
    return redirect("todo:task-list")
