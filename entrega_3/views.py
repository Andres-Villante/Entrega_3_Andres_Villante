from django.shortcuts import render, redirect
from entrega_3.models import Animal, Producto, Libro
from entrega_3.forms import AnimalForm, ProductoForm, LibroForm, BuscarAnimalForm
from django.views.generic import ListView


def mostrar_mis_animales(request):
    animales = Animal.objects.all()
    return render(request, "entrega_3/animales.html", {"animales": animales})

def agregar_animal(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            nuevo_animal = form.save()
            return redirect('mis-animales')
    else:
        form = AnimalForm()
    return render(request, 'entrega_3/agregar_animal.html', {'form': form})


def mostrar_mis_productos(request):
    productos = Producto.objects.all()
    return render(request, "entrega_3/productos.html", {"productos": productos})

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            nuevo_producto = form.save()
            return redirect('mis-productos')
    else:
        form = ProductoForm()
    return render(request, 'entrega_3/agregar_producto.html', {'form': form})


def mostrar_mis_libros(request):
    libros = Libro.objects.all()
    return render(request, "entrega_3/libros.html", {"libros": libros})

def agregar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            nuevo_libro = form.save()
            return redirect('mis-libros')
    else:
        form = LibroForm()
    return render(request, 'entrega_3/agregar_libro.html', {'form': form})


class AnimalBusqueda(ListView):
    model = Animal
    context_object_name = "animales"

    def get_queryset(self):
        f = BuscarAnimalForm(self.request.GET)
        if f.is_valid():
            return Animal.objects.filter(nombre_animal__icontains=f.cleaned_data["criterio_nombre"])
        return Animal.objects.none()





