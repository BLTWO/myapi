from rest_framework import viewsets
from .models import Project
from .serializers import ProjectSerializer
from userauth.permissions import IsAdminOrReadOnly
from dj_rest_auth.jwt_auth import JWTCookieAuthentication
from rest_framework.permissions import IsAuthenticated


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    authentication_classes = [JWTCookieAuthentication]
