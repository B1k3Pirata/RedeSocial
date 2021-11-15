from django.urls import path
from .views import *
from . import views

app_name = 'usuario'

urlpatterns = [
    #autenticação e cadastro de acesso
    path('login/', views.login, name='login'),
    path('validar_login/', views.validar_login, name = 'validar_login'),
    
    path('cadastro/', views.cadastro, name='cadastro'),
    path('valida_cadastro/', views.valida_cadastro, name='valida_cadastro'),
    path('sair/', views.sair, name='sair'),
    #pre-cadastro
    path('inicio/', views.inicio, name='inicio'),
    path('cap/', views.AP.as_view(), name='cap'),
    path('cbp/', views.BP.as_view(), name='cbp'),
    #path('gcomp/', views.GeraComprovante.as_view(), name='comprovante'),
    #cadastro
    #path('usrcad/', views.Cadastro_de_Usuario.as_view(), name='cadastro_de_usuario'),
    path('aluno/', views.DadosAluno.as_view(), name='aluno'),
    path('docs/', Parentesco.as_view(), name='documentos_pessoais'),
    path('docs2/', DocP.as_view(), name='documentos_pessoais2'),
    path('docs3/', DocP2.as_view(), name='documentos_pessoais3'),
    path('end/', Endereco.as_view(), name='endereço'),
    path('contato/', Contato.as_view(), name='contato'),
    path('sau/', Saude.as_view(), name='saúde'),
    path('soc/', Social.as_view(), name='social'),
    path('transp/', Transporte.as_view(), name='Transporte'),
    path('proc/', Procedencia.as_view(), name='Procedência'),
    path('imagem/', Imagem.as_view(), name='imagem'),
    path('sucesso/', Sucesso.as_view(), name='sucesso'),
]
