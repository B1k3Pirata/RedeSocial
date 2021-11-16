from django.urls import path, include
from django.views.generic import TemplateView
#para fornecer arquivos estáticos
from django.conf import settings
from django.conf.urls.static import static

from .views import *
from . import views

app_name = 'perfil'

urlpatterns = [
        path('inicio/', views.inicioperfil, name='inicio'),
]
