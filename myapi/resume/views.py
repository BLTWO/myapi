from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .models import Resume
from .serializers import ResumeSerializer


class ResumeViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ResumeSerializer

    def list(self, request):
        resume = Resume.objects.first()
        if not resume:
            return Response(
                {"detail": "Resume not found."}, status=status.HTTP_404_NOT_FOUND
            )
        return Response(ResumeSerializer(resume).data, status=status.HTTP_200_OK)
