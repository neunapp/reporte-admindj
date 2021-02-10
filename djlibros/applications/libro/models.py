
from django.db import models
#

class Autor(models.Model):
    #
    nombres = models.CharField('nombres', max_length=50)
    nacionalidad = models.CharField('nacionalidad', max_length=100)
    
    class Meta:

      verbose_name = 'Autor'
      verbose_name_plural = 'Autores'

    def __str__(self):
      return self.nombres


class Libro(models.Model):
    #
    autores = models.ManyToManyField(Autor)
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)

    class Meta:

      verbose_name = 'Libro'
      verbose_name_plural = 'Libros'

    def __str__(self):
      return self.titulo
