
from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from django.conf.urls.static import static # type: ignore
from rest_framework.documentation import include_docs_urls # type: ignore

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
