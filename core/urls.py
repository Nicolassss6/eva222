from django.urls import path, include
from . import views
from rest_framework import routers
from .api_views import (
    MedicoViewSet, EspecialidadViewSet, PacienteViewSet,
    MedicamentoViewSet, ConsultaViewSet, RecetaViewSet
)

# API router (para endpoints REST)
router = routers.DefaultRouter()
router.register('medicos', MedicoViewSet)
router.register('especialidades', EspecialidadViewSet)
router.register('pacientes', PacienteViewSet)
router.register('medicamentos', MedicamentoViewSet)
router.register('consultas', ConsultaViewSet)
router.register('recetas', RecetaViewSet)

# URLs de vistas normales (HTML)
urlpatterns = [
    path('', views.home, name='home'),

    path('medicos/', views.MedicoListView.as_view(), name='medico_list'),
    path('medicos/nuevo/', views.MedicoCreateView.as_view(), name='medico_create'),
    path('medicos/<int:pk>/editar/', views.MedicoUpdateView.as_view(), name='medico_update'),
    path('medicos/<int:pk>/eliminar/', views.MedicoDeleteView.as_view(), name='medico_delete'),

    path('pacientes/', views.PacienteListView.as_view(), name='paciente_list'),
    path('pacientes/nuevo/', views.PacienteCreateView.as_view(), name='paciente_create'),

    path('consultas/', views.ConsultaListView.as_view(), name='consulta_list'),
    path('consultas/nuevo/', views.ConsultaCreateView.as_view(), name='consulta_create'),

    path('especialidades/', views.EspecialidadListView.as_view(), name='especialidad_list'),

    path('recetas/', views.RecetaListView.as_view(), name='receta_list'),
    path('recetas/nueva/', views.RecetaCreateView.as_view(), name='receta_create'),

    # Rutas API REST
    path('api/', include(router.urls)),
]
