
from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from django.conf.urls.static import static # type: ignore
from rest_framework.documentation import include_docs_urls # type: ignore

urlpatterns = [
    path('admin/', admin.site.urls),
    path("independientes/", include ('djangorest.urls')),
    # path("dependientes/", include ('dependiente.urls')),

    path('docs/',include_docs_urls(title='Documentation REST Independiente')),

    # path('docs_calcu_inde/',include_docs_urls(title='Documentation REST Calculos de Independiente')),
    # path('docs_noved_inde/',include_docs_urls(title='Documentation REST Novedades de Independiente')),

    # path('docs_empresa/',include_docs_urls(title='Documentation REST Empresa')),
    # path('docs_empleado/',include_docs_urls(title='Documentation REST Empleado')),
    # path('docs_calcu_depen/',include_docs_urls(title='Documentation REST Calculos de Dependiente')),
    # path('docs_noved_depen/',include_docs_urls(title='Documentation REST Novedades de Dependiente')),
]
