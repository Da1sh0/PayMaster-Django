
from django.urls import path, include # type: ignore
from . import views
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'independienterest', views.IndependienteViewSet)

router=routers.DefaultRouter()
router.register(r'calculosrest', views.CalculosViewSet)

router=routers.DefaultRouter()
router.register(r'novedadesrest', views.NovedadesViewSet)

urlpatterns = [
    path('',include(router.urls)),
 
]