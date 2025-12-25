from django.http import HttpResponse
from todo.models import Task
def ok(request):
    return HttpResponse("ok")