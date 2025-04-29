import pytest
from apps.tasks.domain.entities import Task


def test_task_entity_creation():
    task = Task(id=1, title="Test", description="desc")
    assert task.id == 1
    assert task.title == "Test"
    assert not task.completed
