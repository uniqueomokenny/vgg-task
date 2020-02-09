from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import ProjectsViewSet

router = DefaultRouter()
router.register("", ProjectsViewSet, basename="projects")

urlpatterns = router.urls
