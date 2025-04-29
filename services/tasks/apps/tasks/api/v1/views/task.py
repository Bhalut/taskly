from rest_framework.viewsets import ViewSet
from rest_framework.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from apps.tasks.api.v1.serializers import TaskCreateSerializer, TaskSerializer, TaskUpdateSerializer
from apps.tasks.application.services import TaskService
from apps.tasks.infrastructure.repositories import TaskRepository
from apps.tasks.domain.exceptions import TaskTitleTooShortException, TaskNotFoundException

task_service = TaskService(repository=TaskRepository())


class TaskViewSet(ViewSet):
    """
    ViewSet for managing tasks with full CRUD operations.
    """

    permission_classes = [IsAuthenticated]

    def list(self, request):
        tasks = task_service.list_tasks()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = TaskCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        task = task_service.create_task(
            title=serializer.validated_data["title"],
            description=serializer.validated_data["description"],
        )
        return Response(TaskSerializer(task).data, status=HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        task = task_service.get_task_by_id(task_id=int(pk))
        if not task:
            return Response({"detail": "Task not found"}, status=404)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def update(self, request, pk=None):
        serializer = TaskUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            task = task_service.update_task(
                task_id=int(pk),
                title=serializer.validated_data["title"],
                description=serializer.validated_data["description"],
                completed=serializer.validated_data["completed"],
            )
            return Response(TaskSerializer(task).data)
        except TaskNotFoundException:
            return Response({"detail": "Task not found"}, status=404)
        except TaskTitleTooShortException as e:
            return Response({"detail": str(e)}, status=400)

    def partial_update(self, request, pk=None):
        task = task_service.get_task_by_id(task_id=int(pk))
        if not task:
            return Response({"detail": "Task not found"}, status=404)

        data = {
            "title": request.data.get("title", task.title),
            "description": request.data.get("description", task.description),
            "completed": request.data.get("completed", task.completed),
        }

        serializer = TaskUpdateSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        try:
            task = task_service.update_task(
                task_id=int(pk),
                title=serializer.validated_data["title"],
                description=serializer.validated_data["description"],
                completed=serializer.validated_data["completed"],
            )
            return Response(TaskSerializer(task).data)
        except TaskTitleTooShortException as e:
            return Response({"detail": str(e)}, status=400)

    def destroy(self, request, pk=None):
        try:
            success = task_service.delete_task(task_id=int(pk))
            if success:
                return Response(status=HTTP_204_NO_CONTENT)
            else:
                return Response({"detail": "Failed to delete task"}, status=500)
        except TaskNotFoundException:
            return Response({"detail": "Task not found"}, status=404)