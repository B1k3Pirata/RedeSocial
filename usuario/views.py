from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.urls import reverse

from .models import *

app_name = 'usuario'

class Usuario(TemplateView):
    template_name = 'usuario/index.html'

class Matricula(CreateView):
    model = Matricula
    fields = ['matricula','ano_matricula','nivel']
    template_name = 'usuario/form.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Cadastro de Usuário'
        context['texto1'] = 'Preencha seus dados completos, para melhor configuração do seu perfil'
        context['botaoC'] = 'Avançar'
        context['botaoB'] = 'Limpar'
        context['botaoA'] = 'Cancelar'
        return context
    success_url = '/usuario/dados/'

class DadosAluno(CreateView):
    model = AlunoDados
    fields = '__all__'#['nome','snome']
    template_name = 'usuario/form.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Cadastro de Usuário'
        context['texto1'] = 'Preencha seus dados completos, para melhor configuração do seu perfil'
        context['botaoC'] = 'Avançar'
        context['botaoB'] = 'Limpar'
        context['botaoA'] = 'Cancelar'
        return context
    success_url = '/usuario/docs/'

class DocP(CreateView):
    model = DocPessoal
    fields = '__all__'#['rg','cpf','filia1','filia2']
    template_name = 'usuario/form.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Cadastro de Usuário'
        context['texto1'] = 'Preencha seus dados completos, para melhor configuração do seu perfil'
        context['botaoC'] = 'Avançar'
        context['botaoB'] = 'Limpar'
        context['botaoA'] = 'Cancelar'
        return context
    success_url = '/usuario/docs2/'

class DocP2(CreateView):
    model = Pessoal
    fields = '__all__'#['Dnasc','sexo','raca','qprenm','prenm','nacio','qnacio','ufnasc','locnasc']
    template_name = 'usuario/form.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Cadastro de Usuário'
        context['texto1'] = 'Preencha seus dados completos, para melhor configuração do seu perfil'
        context['botaoC'] = 'Avançar'
        context['botaoB'] = 'Limpar'
        context['botaoA'] = 'Cancelar'
        return context
    success_url = '/usuario/docs3/'

class DocP3(CreateView):
    model = Documento
    fields = '__all__'#['qpcer','tpcerl','nocer','licer','flcer','emtcr','cartc','ufcrt','cidcrt','qrg','norg','orgrg','ufrg','dtrg','cpf','pasp']
    template_name = 'usuario/form.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Cadastro de Usuário'
        context['texto1'] = 'Preencha seus dados completos, para melhor configuração do seu perfil'
        context['botaoC'] = 'Avançar'
        context['botaoB'] = 'Limpar'
        context['botaoA'] = 'Cancelar'
        return context
    success_url = '/usuario/end/'

class Endereco(CreateView):
    model = End
    fields = '__all__'#['end','num','muni','cep','comp','brr','uncon','qzon','ct1','ct2']
    template_name = 'usuario/form.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Cadastro de Usuário'
        context['texto1'] = 'Preencha seus dados completos, para melhor configuração do seu perfil'
        context['botaoC'] = 'Avançar'
        context['botaoB'] = 'Limpar'
        context['botaoA'] = 'Cancelar'
        return context
    success_url = '/usuario/sau/'

class Saude(CreateView):
    model = Sau
    fields = '__all__'#['aep','cego','bv','sc','sd','da','di','dm','df','ai','srt','sasp','tdi','ahs']
    template_name = 'usuario/form.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Cadastro de Usuário'
        context['texto1'] = 'Preencha seus dados completos, para melhor configuração do seu perfil'
        context['botaoC'] = 'Avançar'
        context['botaoB'] = 'Limpar'
        context['botaoA'] = 'Cancelar'
        return context
    success_url = '/usuario/soc/'

class Social(CreateView):
    model = Social
    fields = ['bcp','pbf','pbt','peti']
    template_name = 'usuario/form.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Cadastro de Usuário'
        context['texto1'] = 'Preencha seus dados completos, para melhor configuração do seu perfil'
        context['botaoC'] = 'Avançar'
        context['botaoB'] = 'Limpar'
        context['botaoA'] = 'Cancelar'
        return context
    success_url = '/usuario/transp/'

class Transporte(CreateView):
    model = Transp
    fields = '__all__'#['pprte','pbfa','qserv','urb','rod','aqua','trm']
    template_name = 'usuario/form.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Cadastro de Usuário'
        context['texto1'] = 'Preencha seus dados completos, para melhor configuração do seu perfil'
        context['botaoC'] = 'Avançar'
        context['botaoB'] = 'Limpar'
        context['botaoA'] = 'Cancelar'
        return context
    success_url = '/usuario/proc/'

class Procedencia(CreateView):
    model = Proc
    fields = '__all__'#['nesc','pore1a','pore2a','pore3a','pore4a','comec','anx','idtnv','fase','turno','modal','seq','rat']
    template_name = 'usuario/form.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Cadastro de Usuário'
        context['texto1'] = 'Preencha seus dados completos, para melhor configuração do seu perfil'
        context['botaoC'] = 'Avançar'
        context['botaoB'] = 'Limpar'
        context['botaoA'] = 'Cancelar'
        return context
    success_url = '/usuario/sucesso/'

class Sucesso(TemplateView):
    template_name = 'usuario/sucesso.html'
