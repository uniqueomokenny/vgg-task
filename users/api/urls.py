from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import UserViewSet, LoginViewSet, LogoutViewSet

router = DefaultRouter()
router.register("auth", LoginViewSet, basename="auth")
router.register("logout", LogoutViewSet, basename="logout")
router.register('', UserViewSet)

urlpatterns = router.urls
