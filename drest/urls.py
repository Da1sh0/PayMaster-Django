"""
URL configuration for drest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from django.conf.urls.static import static # type: ignore
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("independientes/", include ('djangorest.urls')),
    # path("dependientes/", include ('dependiente.urls')),
    path('docs/',include_docs_urls(title='Documentation REST Independiente')),
    # path('docs1/',include_docs_urls(title='Documentation REST Calculosin')),
    # path('docs2/',include_docs_urls(title='Documentation REST Novedadesin')),
    # path('docsempresa/',include_docs_urls(title='Documentation REST Empresa')),
    # path('docsempleado/',include_docs_urls(title='Documentation REST Empleado')),
    # path('docscalculos/',include_docs_urls(title='Documentation REST Calculos')),
    # path('docsnovedades/',include_docs_urls(title='Documentation REST Novedades')),
]
