from django.urls import path
from .views import ok


app_name = 'api-v1'

urlpatterns = [
    path("ok/", ok, name="ok"),
]