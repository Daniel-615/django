from .models import Project
from rest_framework import viewsets,permissions
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset=Project.objects.all()
    permission_classes=[permissions.AllowAny] #cualquier aplicacion cliente puede solicitar datos al servidor
    serializer_class= ProjectSerializer