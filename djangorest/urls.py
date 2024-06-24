from django.urls import path, include # type: ignore
from rest_framework.routers import DefaultRouter # type: ignore
from .views import IndependienteViewSet, CalculosViewSet, CalculosGenerales

independiente_router = DefaultRouter()
independiente_router.register(r'independienterest', IndependienteViewSet)

calculos_router = DefaultRouter()
calculos_router.register(r'calculosrest', CalculosViewSet)

urlpatterns = [
    path('inde/', include(independiente_router.urls)),
    path('calcu/', include(calculos_router.urls)),
    path('calcularinde/<str:numero_identificacion>/', CalculosGenerales.as_view(), name='calcularinde'),
]
