from django.contrib import admin
from .models import UsrCad, Categoria, AtendimentoPersonalizado, BancaPermanente
# Register your models here.

admin.site.register(Categoria)


@admin.register(BancaPermanente)
class BancaPermanenteAdmin(admin.ModelAdmin):
    list_display = ('nome','snome','dataCad','slug','controle')
    prepopulated_fields = {"slug":("snome","nome",)}

@admin.register(AtendimentoPersonalizado)
class AtendimentoPersonalizadoAdmin(admin.ModelAdmin):
    list_display = ('nome','snome','dataCad','slug','controle')
    prepopulated_fields = {"slug":("snome","nome",)}

@admin.register(UsrCad)
class UsrAdmin(admin.ModelAdmin):
    readonly_fields = ('nome','email','senha')
