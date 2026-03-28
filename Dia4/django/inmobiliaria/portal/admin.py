from django.contrib import admin
from django.utils.html import format_html
from.models import *
# Register your models here.

admin.site.register(TipoInmueble)
#admin.site.register(Inmueble)
admin.site.register(Ciudad)
#admin.site.register(Agente)
#admin.site.register(Comentario)
#admin.site.register(ImagenInmueble)

#modificar la visualizacion de los comentarios
@admin.register(Agente)
class AgenteAdmin(admin.ModelAdmin):
    list_display = ('usuario','telefono')
    search_fields = ('usuario_username',)

@admin.register(Comentario)
class CometarioAdmin(admin.ModelAdmin):
    list_display = ('usuario','inmueble','fecha')
    list_filter = ('fecha',)

@admin.register(ImagenInmueble)
class imagenAdmin(admin.ModelAdmin):

    list_display = ('inmueble','preview')

    def preview(selft, obj):
        return format_html(
            '<img src="{}" width="88" height="60" />',
            obj.imagen.url
        )
    preview.short_descripcion = "Preview"

class ImagenInline(admin.TabularInline):
    model= ImagenInmueble
    extra = 1


@admin.register(Inmueble)
class InmuebleAdmin(admin.ModelAdmin):
    # columnas visibles
    list_display = ('titulo','precio','ciudad','tipo','agente','mostrar_imagen')

    #filtros laterales
    list_filter = ('tipo','ciudad','precio')

    #buscador
    search_fields = ('titulo','ciudad','descripcion')

    #orden
    ordering = ('-precio',)

    #inline images
    inlines = [ImagenInline]

    #cantidad por pagina
    list_per_page = 10

    #metodo para mostrar imagen miniatura 
    def mostrar_imagen(self, obj):
        imagen = obj.imagenes.first()

        if imagen:
            return format_html(
                '<img src="{}" width="80" height="60" style="object-fit:cover;" />',
                imagen.imagen.url
             )
    
        return "Sin imagen"
    
    mostrar_imagen.short_description = 'Imagen'