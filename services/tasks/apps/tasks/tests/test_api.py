import pytest
from rest_framework.test import APIClient
from django.urls import reverse

pytestmark = pytest.mark.django_db

client = APIClient()


def test_create_task_api(auth_client):
    payload = {"title": "E2E Task Auth", "description": "Testing with auth"}
    response = auth_client.post("/api/v1/tasks/", data=payload, format="json")

    assert response.status_code == 201


def test_list_tasks_api():
    # Create a task first
    client.post(
        reverse("task-list"),
        data={"title": "Task1", "description": "Desc1"},
        format="json",
    )

    response = client.get(reverse("task-list"))

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1
    assert any(task["title"] == "Task1" for task in data)
