from rest_framework.filters import OrderingFilter
from todo.api.v1.serializers import TaskSerializer
from todo.models import Task
from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = [
        "is_done",
    ]
    ordering_fields = [
        "created_at",
    ]
