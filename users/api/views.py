from django.contrib.auth import authenticate, get_user_model

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from users import models
from users.api.serializers import UserSerializer
from .permissions import UserPermission


User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (UserPermission, )
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            (token, _) = Token.objects.get_or_create(user=user)

            return Response({"token": token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
