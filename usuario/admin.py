from django.contrib import admin
from .models import UsrCad
# Register your models here.

@admin.register(UsrCad)
class UsrAdmin(admin.ModelAdmin):
    readonly_fields = ('nome','email','senha')
