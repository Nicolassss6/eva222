from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# --- Configuración de Swagger / Redoc ---

schema_view = get_schema_view(
    openapi.Info(
        title="💊 Salud Vital API",
        default_version='v1',
        description="""
        API del sistema **Salud Vital** 🏥  
        Gestiona médicos, pacientes, consultas, especialidades, medicamentos y recetas médicas.  
        Incluye endpoints completos (CRUD) y documentación automática con Swagger y ReDoc.
        """,
        contact=openapi.Contact(email="admin@saludvital.cl"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Rutas de la app principal
    path('', include('core.urls')),

    # Documentación Swagger y Redoc
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
