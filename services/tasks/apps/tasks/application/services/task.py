from apps.tasks.domain.entities import Task
from apps.tasks.domain.exceptions import TaskTitleTooShortException, TaskNotFoundException
from apps.tasks.domain.repositories import ITaskRepository
from typing import Optional


class TaskService:
    def __init__(self, repository: ITaskRepository):
        self.repository = repository

    def create_task(self, title: str, description: str) -> Task:
        if len(title) < 3:
            raise TaskTitleTooShortException(
                "Title must be at least 3 characters."
            )

        task = Task(
            id=None,
            title=title,
            description=description,
            completed=False,
        )
        return self.repository.create(task)

    def list_tasks(self) -> list[Task]:
        return self.repository.list_all()

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        return self.repository.get_by_id(task_id)

    def update_task(self, task_id: int, title: str, description: str, completed: bool) -> Task:
        task = self.repository.get_by_id(task_id)
        if not task:
            raise TaskNotFoundException(f"Task with id {task_id} not found")

        if len(title) < 3:
            raise TaskTitleTooShortException("Title must be at least 3 characters.")

        updated_task = Task(
            id=task_id,
            title=title,
            description=description,
            completed=completed,
        )

        return self.repository.update(updated_task)

    def delete_task(self, task_id: int) -> bool:
        task = self.repository.get_by_id(task_id)
        if not task:
            raise TaskNotFoundException(f"Task with id {task_id} not found")

        return self.repository.delete(task_id)