"""
URL configuration for biblioteca project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from libro import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('libros/', views.listar_libros, name='listar_libros'),
    path('', views.crear_libro, name='crear_libro'),
    path('libros/<int:libro_id>/editar/', views.editar_libro, name='editar_libro'),
    path('libros/<int:libro_id>/eliminar/', views.eliminar_libro, name='eliminar_libro'),
    path('libros/<int:libro_id>/', views.detalle_libro, name='detalle_libro'),
    # Aquí añadimos las rutas para login y logout
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    #path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),

    # Incluye las rutas de tu aplicación si están en un archivo urls.py separado
    #path('', include('tu_aplicacion.urls')),  # Asegúrate de incluir tu app aquí
]
