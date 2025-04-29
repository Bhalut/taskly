import pytest
from apps.tasks.application.services import TaskService
from apps.tasks.infrastructure.models import Task as TaskModel
from apps.tasks.domain.exceptions import (
    TaskTitleTooShortException
)
from apps.tasks.domain.repositories import TaskRepository

pytestmark = pytest.mark.django_db


def test_create_task():
    task = TaskService.create_task(
        "Learn DDD", "Understand Entities, Aggregates, Repositories."
    )

    assert task.id is not None
    assert task.title == "Learn DDD"
    assert not task.completed
    assert TaskModel.objects.count() == 1


def test_create_task_with_short_title_raises_exception():
    service = TaskService(repository=TaskRepository())

    with pytest.raises(TaskTitleTooShortException):
        service.create_task(title="Hi", description="Short title")


def test_list_tasks():
    TaskService.create_task("Task 1", "Desc 1")
    TaskService.create_task("Task 2", "Desc 2")

    tasks = TaskService.list_tasks()

    assert len(tasks) == 2
    titles = [t.title for t in tasks]
    assert "Task 1" in titles
    assert "Task 2" in titles
