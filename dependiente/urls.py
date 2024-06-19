from django.urls import path, include # type: ignore
from . import views
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'empresarest', views.EmpresaViewSet)

router=routers.DefaultRouter()
router.register(r'empleadorest', views.EmpleadoViewSet)

router=routers.DefaultRouter()
router.register(r'calculosrest', views.CalculoViewSet)

router=routers.DefaultRouter()
router.register(r'novedadesrest', views.NovedadesViewSet)

urlpatterns = [
    path('',include(router.urls)),
 
]
