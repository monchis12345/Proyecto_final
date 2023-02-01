from django.urls import path, include
from . import views
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib import admin
from django.contrib.staticfiles.urls import static 

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('libros', views.libros, name='libros'),
    path('libros/crear', views.crear, name='crear'),
    path('libros/editar', views.editar, name='editar'),
    path('eliminar<int:id>', views.eliminar, name='eliminar'),
    path('libros/editar/<int:id>', views.editar, name='editar'),
    path('accounts', include('django.contrib.auth.urls')),
    path('links', views.links, name='links'),
    path('fotos', views.fotos, name='fotos'),
     

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
