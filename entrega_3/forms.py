from django import forms
from entrega_3.models import Animal, Producto, Libro


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['nombre_animal', 'altura', 'peso']


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre_producto', 'descripcion', 'precio']


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['nombre_libro', 'genero', 'cantidad_paginas']

class AnimalBusquedaForm(forms.Form):
    nombre_animal = forms.CharField(max_length=100)