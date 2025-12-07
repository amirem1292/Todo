from django.urls import path
from core import settings
from django.conf.urls.static import static

from todo import views

app_name = 'todo'

urlpatterns = [
    path('', views.TaskListView.as_view(), name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)