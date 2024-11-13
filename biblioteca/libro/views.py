from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro
from django.core.paginator import Paginator
from django.http import HttpResponse
from .forms import LibroForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def listar_libros(request):
    libros = Libro.objects.select_related('usuario').filter(usuario=request.user)

    paginator = Paginator(libros, 5) #5 libros por paginas

    page_number = request.GET.get('page')

    page_onj = paginator.get_page(page_number)

    return render(request, 'listar_libros.html', {'page_obj':page_onj})

# Crear un nuevo libro
@login_required
def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            nuevo_libro = form.save(commit=False)
            nuevo_libro.usuario = request.user #Asignamos el usuario autenticado
            nuevo_libro.save()
            return redirect('listar_libros')
    else:
        form = LibroForm()
    return render(request, 'crear_libros.html', {'form': form})

# Editar libro existente
def editar_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id, usuario=request.user)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'editar_libro.html', {'form': form, 'libro': libro})

# Eliminar un libro
def eliminar_libro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id, usuario=request.user)
    if request.method == 'POST':
        libro.delete()
        return redirect('listar_libros')
    return render(request, 'eliminar_libro.html', {'libro': libro})