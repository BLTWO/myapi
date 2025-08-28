from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Resume
from .serializers import ResumeSerializer
from rest_framework.permissions import IsAuthenticated
from userauth.permissions import IsAdminOrReadOnly
from dj_rest_auth.jwt_auth import JWTCookieAuthentication


class ResumeViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    authentication_classes = [JWTCookieAuthentication]
    serializer_class = ResumeSerializer

    def list(self, request):
        latest_resume = Resume.objects.order_by("-date").first()
        if not latest_resume:
            from . import resumefetch

            resumefetch.fetch_and_update_resume()

        latest_resume = Resume.objects.order_by("-date").first()

        serializer = ResumeSerializer(latest_resume)
        return Response(serializer.data, status=status.HTTP_200_OK)
