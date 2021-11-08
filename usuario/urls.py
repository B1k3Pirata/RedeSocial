from django.urls import path
from .views import *
from . import views

app_name = 'usuario'

urlpatterns = [
    #autenticação e cadastro de acesso
    path('login/', Login.as_view(), name='login'),
    path('cadastro/', Cadastro.as_view(), name='cadastro'),
    #path('valida_cadastro/', views.valida_cadastro, name = 'valida_cadastro'),
    #path('valida_login/', views.valida_login, name = 'valida_login'),
    path('sair/', views.sair, name='sair'),
    #cadastro de dados
    #path('inicio/', views.iniciousr, name='inicio'),
    path('inicio/', Aluno.as_view(), name = 'inicio'),
    path('novo/', AlunoNovo.as_view(), name = 'novo'),
    path('veterano/', AlunoVeterano.as_view(), name='veterano'),
    path('dados/', DadosAluno.as_view(), name='dados_pessoais'),
    path('docs/', DocP.as_view(), name='documentos_pessoais'),
    path('docs2/', DocP2.as_view(), name='documentos_pessoais2'),
    path('docs3/', DocP3.as_view(), name='documentos_pessoais3'),
    path('end/', Endereco.as_view(), name='endereço'),
    path('contato/', Contato.as_view(), name='contato'),
    path('sau/', Saude.as_view(), name='saúde'),
    path('soc/', Social.as_view(), name='social'),
    path('transp/', Transporte.as_view(), name='Transporte'),
    path('proc/', Procedencia.as_view(), name='Procedência'),
    path('imagem/', Imagem.as_view(), name='imagem'),
    path('sucesso/', Sucesso.as_view(), name='sucesso'),
]
