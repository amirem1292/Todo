from django.urls import path
from core import settings
from django.conf.urls.static import static

app_name = 'todo'

urlpatterns = [

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)