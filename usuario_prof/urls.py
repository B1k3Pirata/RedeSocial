from django.urls import path
from .views import *
from . import views

app_name = 'usuario'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('validar_login/', views.validar_login, name = 'validar_login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('valida_cadastro/', views.valida_cadastro, name='valida_cadastro'),
    path('sair/', views.sair, name='sair'),

    path('prof/', DocenteCreate.as_view(), name="prof"),
    path('perfilp/', views.inicioperfildocente, name='perfil_professor'),
    path('sucesso/', Sucesso.as_view(), name='sucesso'),
]
