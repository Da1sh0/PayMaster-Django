from rest_framework.routers import DefaultRouter # type: ignore
from .views import IndependienteViewSet, CalculosViewSet, NovedadesViewSet
from django.urls import path, include # type: ignore

independiente_router = DefaultRouter()
independiente_router.register(r'independienterest', IndependienteViewSet)

calculos_router = DefaultRouter()
calculos_router.register(r'calculosrest', CalculosViewSet)

novedades_router= DefaultRouter()
novedades_router.register(r'novedadesrest', NovedadesViewSet)

urlpatterns = [
    path('inde',include(independiente_router.urls)),
    path('calcu',include(calculos_router.urls)),
    path('nove',include(novedades_router.urls)),
 
]