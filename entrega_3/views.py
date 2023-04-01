from django.shortcuts import render, redirect
from entrega_3.models import Animal, Producto, Libro
from entrega_3.forms import AnimalForm, ProductoForm, LibroForm, AnimalBusquedaForm
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







def buscar_animal(request):
    form = AnimalBusquedaForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['nombre_animal']
        results = Animal.objects.filter(nombre_animal__icontains=query)
        return render(request, 'buscar_resultados.html', {'results': results, 'query': query})
    else:
        return render(request, 'buscar_resultados.html', {'results': results, 'query': query})


class BuscarAnimalView(ListView):
    model = Animal
    template_name = "buscar_resultados.html"
    context_object_name = "results"
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Animal.objects.filter(nombre_animal__icontains=query)
        return Animal.objects.none()
