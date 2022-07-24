"""example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views

from django.urls import path, include


from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(title="example API", default_version="v1"),
    public=True,
    authentication_classes=[SessionAuthentication],
    permission_classes=[IsAdminUser],
)

urlpatterns = [
    path('admin', admin.site.urls),

    # API Server
    path("api/boards", include("boards.urls")),

    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),  # The base django login view
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),  # The base django logout view

    path("docs", schema_view.with_ui("swagger", cache_timeout=0), name="schema-docs"),
]
