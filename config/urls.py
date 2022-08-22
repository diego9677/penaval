'''config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
'''
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.generic import RedirectView
from ninja import NinjaAPI, ModelSchema
from productos.models import Producto
from typing import List

class ProductosOut(ModelSchema):
    class Config:
        model = Producto
        model_fields = ['codigo', 'lugar', 'marca', 'cantidad_disponible', 'precio_unitario', 'medidas']

api = NinjaAPI()


@api.get("/products", response=List[ProductosOut])
def add(request):
    productos = Producto.objects.all()
    return productos


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('productos/', include('productos.urls')),
    path('ventas/', include('ventas.urls')),
    path('compras/', include('compras.urls')),
    path("api/", api.urls),
    path('', RedirectView.as_view(pattern_name='producto-list'), name='index'),
]


if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
