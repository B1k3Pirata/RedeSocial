from django.contrib import admin
from .models import Categoria, AtendimentoPersonalizado, BancaPermanente
# Register your models here.

admin.site.register(Categoria)
@admin.register(AtendimentoPersonalizado)
@admin.register(BancaPermanente)


class BancaPermanenteAdmin(admin.ModelAdmin):
    list_display = ('nome','snome','dataCad','slug','controle')
    prepopulated_fields = {"slug":("snome","nome",)}

class AtendimentoPersonalizadoAdmin(admin.ModelAdmin):
    list_display = ('nome','snome','dataCad','slug','controle')
    prepopulated_fields = {"slug":("snome","nome",)}
