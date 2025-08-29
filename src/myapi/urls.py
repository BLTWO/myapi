"""
URL configuration for myapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin

from rest_framework.routers import DefaultRouter
from django.urls import include, path
# from experience.views import ExperienceViewSet
from django.shortcuts import redirect
from project.views import ProjectViewSet
from resume.views import ResumeViewSet
# from link.views import LinksViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse


router = DefaultRouter()
# router.register(r"experience", ExperienceViewSet)
router.register(r"project", ProjectViewSet)
router.register(r"resume", ResumeViewSet, basename="resume")
# router.register(r"links", LinksViewSet)

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        "auth/register": reverse("register", request=request, format=format),
        "auth/login": reverse("login", request=request, format=format),
        "auth/logout": reverse("logout", request=request, format=format),
        "projects": reverse("project-list", request=request, format=format),
        "resumes": reverse("resume-list", request=request, format=format),
    })

urlpatterns = [
    path("", lambda request: redirect("api/", permanent=False)),
    path("admin/", admin.site.urls),
    path("api/", api_root),
    path("api/", include(router.urls)),
    path("api/auth/", include("userauth.urls")),
]
