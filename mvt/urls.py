"""mvt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from entrega_3.views import( mostrar_mis_animales, 
                    agregar_animal, 
                    mostrar_mis_productos, 
                    agregar_producto,
                    mostrar_mis_libros, 
                    agregar_libro, 
                    AnimalBusqueda,
                    )




urlpatterns = [
    path('admin/', admin.site.urls),

    path('mis-animales/', mostrar_mis_animales, name="mis-animales"),
    path('agregar-animales/', agregar_animal, name='agregar-animales'),
    
    path('mis-productos/', mostrar_mis_productos, name="mis-productos"),
    path('agregar-productos/', agregar_producto, name='agregar-productos'),

    path('mis-libros/', mostrar_mis_libros, name="mis-libros"),
    path('agregar-libros/', agregar_libro, name='agregar-libros'),

    path('lista-animales/', AnimalBusqueda.as_view(), name='lista-animales')
]
