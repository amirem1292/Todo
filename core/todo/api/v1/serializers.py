from django.shortcuts import get_object_or_404
from rest_framework import serializers
from django.contrib.auth.models import User
from todo.models import Task


class TaskSerializer(serializers.ModelSerializer):
    full_url = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = [
            "id",
            "author",
            "title",
            "is_done",
            "created_at",
            "full_url",
        ]
        read_only_fields = ["author", "created_at"]

    def get_full_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.id)

    def create(self, validated_data):
        validated_data["author"] = get_object_or_404(
            User, pk=self.context.get("request").user.id
        )
        return super().create(validated_data)
