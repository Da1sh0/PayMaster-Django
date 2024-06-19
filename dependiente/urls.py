from django.urls import path, include # type: ignore
from .views import EmpresaViewSet, EmpleadoViewSet, CalculosViewSet, NovedadesViewSet
from rest_framework.routers import DefaultRouter # type: ignore



empresa_router = DefaultRouter()
empresa_router.register(r'empresarest', EmpresaViewSet)

empleado_router = DefaultRouter()
empleado_router.register(r'empleadorest', EmpleadoViewSet)

calculos_router = DefaultRouter()
calculos_router.register(r'calculorest', CalculosViewSet)

novedades_router = DefaultRouter()
novedades_router.register(r'calculorest', NovedadesViewSet)

# router=routers.DefaultRouter()
# router.register(r'calculosrest', views.CalculoViewSet)

# router=routers.DefaultRouter()
# router.register(r'novedadesrest', views.NovedadesViewSet)

urlpatterns = [
    path('empresa',include(empresa_router.urls)),
    path('empleado',include(empleado_router.urls)),
    path('calculosdepe',include(calculos_router.urls)),
    path('novedadesdepe',include(novedades_router.urls)),
 
]
