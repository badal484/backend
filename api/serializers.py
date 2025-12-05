from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField(required=False)
    completed = serializers.CharField(default="False")
