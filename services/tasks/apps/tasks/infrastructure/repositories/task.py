from apps.tasks.infrastructure.models import Task as TaskModel
from apps.tasks.domain.entities import Task
from apps.tasks.domain.repositories import ITaskRepository
from typing import Optional


class TaskRepository(ITaskRepository):

    @staticmethod
    def create(task: Task) -> Task:
        model = TaskModel.objects.create(
            title=task.title,
            description=task.description,
            completed=task.completed,
        )
        return TaskRepository._to_entity(model)

    @staticmethod
    def list_all() -> list[Task]:
        return [
            TaskRepository._to_entity(task)
            for task in TaskModel.objects.all()
        ]

    @staticmethod
    def get_by_id(task_id: int) -> Optional[Task]:
        try:
            model = TaskModel.objects.get(id=task_id)
            return TaskRepository._to_entity(model)
        except TaskModel.DoesNotExist:
            return None

    @staticmethod
    def update(task: Task) -> Task:
        model = TaskModel.objects.get(id=task.id)
        model.title = task.title
        model.description = task.description
        model.completed = task.completed
        model.save()
        return TaskRepository._to_entity(model)

    @staticmethod
    def delete(task_id: int) -> bool:
        try:
            model = TaskModel.objects.get(id=task_id)
            model.delete()
            return True
        except TaskModel.DoesNotExist:
            return False

    @staticmethod
    def _to_entity(model: TaskModel) -> Task:
        return Task(
            id=model.id,
            title=model.title,
            description=model.description,
            completed=model.completed,
            created_at=model.created_at,
            updated_at=model.updated_at,
        )