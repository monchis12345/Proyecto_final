from django.db import models
from django.contrib.auth.models import User
from datetime import date
class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    imagen = models.ImageField(upload_to='imagenes/', verbose_name='Imagen', null= True )
    descripcion = models.TextField(verbose_name='Descripciòn' ,null=True)

    def __str__(self):
        fila = "Titulo: " + self.titulo + " - " + "Descripciòn: " + self.descripcion
        return fila 
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    


# Create your models here.
