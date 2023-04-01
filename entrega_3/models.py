from django.db import models

class Animal(models.Model):
    nombre_animal = models.CharField(max_length=100)
    altura = models.TextField(max_length=100)
    peso = models.TextField(max_length=100)

    def __str__(self):
        return f"{self.id} → Animal: {self.nombre_animal} → Altura: {self.altura} cm → Peso: {self.peso} kg"


class Producto(models.Model):
    nombre_producto = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500)
    precio = models.TextField(max_length=8)

    def __str__(self):
        return f"{self.id} → Producto: {self.nombre_producto} → Precio: (${self.precio}) → Descripcion: {self.descripcion}"


class Libro(models.Model):
    nombre_libro = models.CharField(max_length=100)
    genero = models.TextField(max_length=100)
    cantidad_paginas = models.TextField(max_length=2000)

    def __str__(self):
        return f"{self.id} → Nombre: {self.nombre_libro} → Genero: {self.genero} → Paginas: {self.cantidad_paginas}"


