from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import ActionsViewSet

router = DefaultRouter()
router.register("", ActionsViewSet, basename="actions")

urlpatterns = router.urls
