from django.shortcuts import render, redirect, get_list_or_404
from .models import Libro
from django.core.paginator import Paginator
# Create your views here.

def listar_libros(request):
    libros = Libro.objects.select_related('usuario').filter(usuario=request.user)

    paginator = Paginator(libros, 5) #5 libros por paginas

    page_number = request.GET.get('page')

    page_onj = paginator.get_page(page_number)

    return render(request, 'listar_libros.html', {'page_obj':page_onj})
