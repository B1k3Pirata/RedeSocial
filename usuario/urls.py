from django.urls import path
from .views import *

app_name = 'usuario'

urlpatterns = [
    path('inicio/', Usuario.as_view(), name='inicio'),
    path('matricula/', Matricula.as_view(), name='matricula'),
    path('dados/', DadosAluno.as_view(), name='dados_pessoais'),
    path('docs/', DocP.as_view(), name='documentos_pessoais'),
    path('docs2/', DocP2.as_view(), name='documentos_pessoais2'),
    path('docs3/', DocP3.as_view(), name='documentos_pessoais3'),
    path('end/', Endereco.as_view(), name='endereço'),
    path('sau/', Saude.as_view(), name='saúde'),
    path('soc/', Social.as_view(), name='social'),
    path('transp/', Transporte.as_view(), name='Transporte'),
    path('proc/', Procedencia.as_view(), name='Procedência'),
    path('imagem/', Imagem.as_view(), name='imagem'),
    path('signup/', LOG.as_view(), name='signup'),
    path('sucesso/', Sucesso.as_view(), name='sucesso'),
]
