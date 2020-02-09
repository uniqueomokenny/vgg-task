from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from projects.models import Projects
from .serializers import ProjectsSerializer


class ProjectsViewSet(ModelViewSet):
    permission_classes = (AllowAny, )
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
