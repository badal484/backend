from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Task
from rest_framework import status

from .serializers import TaskSerializer

class TaskList(APIView):
    def get(self, request):
        tasks = Task.objects()
        return Response(TaskSerializer(tasks, many=True).data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            task = Task(**serializer.validated_data).save()
            return Response(TaskSerializer(task).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
