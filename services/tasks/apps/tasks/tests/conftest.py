import pytest
from rest_framework.test import APIClient


@pytest.fixture
def auth_client(db):
    from django.contrib.auth import get_user_model

    User = get_user_model()
    user = User.objects.create_user(username="testuser", password="testpass")
    client = APIClient()
    response = client.post(
        "/api/token/",
        {"username": "testuser", "password": "testpass"},
        format="json"
    )
    token = response.data["access"]
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    return client
