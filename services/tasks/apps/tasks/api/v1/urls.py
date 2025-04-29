from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, HealthCheckView

router = DefaultRouter()
router.register(r"tasks", TaskViewSet, basename="task")

urlpatterns = router.urls + [
    path("health/", HealthCheckView.as_view(), name="health-check"),
]
