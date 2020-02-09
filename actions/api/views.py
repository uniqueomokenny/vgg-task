from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from actions.models import Actions
from .serializers import ActionsSerializer


class ActionsViewSet(ModelViewSet):
    permission_classes = (AllowAny, )
    queryset = Actions.objects.all()
    serializer_class = ActionsSerializer
