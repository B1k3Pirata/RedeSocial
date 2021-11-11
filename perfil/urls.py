from django.urls import path, include
from django.views.generic import TemplateView
from .views import *

app_name = 'perfil'

urlpatterns = [
    #path('perfil/avatar', lista_avatar, name='avatar'),
    path('inicio/', PerfilInicio.as_view(), name='perfil'),
]
