from import_export import resources
from import_export.admin import ImportExportModelAdmin
#
from django.contrib import admin
#
from .models import Autor, Libro



@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = (
        'nombres',
        'nacionalidad',
        'id',
    )
    search_fields = ('nombres',)


class LibroResources(resources.ModelResource):
    fields = (
      'titulo',
      'descripcion',
      'autor__nombres',
      'id',
    )
    class Meta:
        model = Libro


@admin.register(Libro)
class LibroAdmin(ImportExportModelAdmin):
    resource_class = LibroResources
    list_display = (
        'titulo',
        'descripcion',
        'autor',
        'id',
    )
    #
    def autor(self, obj):
        #toda la operacion
        return 'Autor de Prueba'
    
    search_fields = ('titulo',)
    list_filter = ('autores',)
    #
    filter_horizontal = ('autores',)