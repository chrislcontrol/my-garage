"""my_garage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from my_garage.authentication.urls import AUTH_PATH
from my_garage.clients.urls import CLIENTS_PATH
from my_garage.settings import PROJECT_VERBOSE_NAME, PROJECT_DESCRIPTION, PROJECT_VERSION
from my_garage.vehicles.urls import VEHICLES_PATH

schema_view = get_schema_view(
    openapi.Info(title=f"{PROJECT_VERBOSE_NAME} - {PROJECT_DESCRIPTION}",
                 default_version=f"v{PROJECT_VERSION}"
                 ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

V1 = "api/v1/"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-docs/', schema_view.with_ui('swagger', cache_timeout=None), name='schema-swagger-ui'),
    path(V1, include('my_garage.authentication.urls', namespace=AUTH_PATH)),
    path(V1, include('my_garage.clients.urls', namespace=CLIENTS_PATH)),
    path(V1, include('my_garage.vehicles.urls', namespace=VEHICLES_PATH)),
]
