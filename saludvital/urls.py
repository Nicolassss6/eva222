from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Documentación Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Salud Vital API",
        default_version='v1',
        description="Documentación de la API para la Evaluación 2 - Programación Backend",
        contact=openapi.Contact(email="tucorreo@ejemplo.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Incluye todas las rutas de la app principal
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
