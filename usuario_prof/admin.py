from django.contrib import admin
from .models import Acesso

# Register your models here.
@admin.register(Acesso)
class UsrAdmin(admin.ModelAdmin):
    readonly_fields = ('nome','email','senha')
