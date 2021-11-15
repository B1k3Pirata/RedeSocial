from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.urls import reverse
from django.http import HttpResponse
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from hashlib import sha256

from .models import *

import sqlite3 as sl
from datetime import date, time, datetime
#import pandas as pd

app_name = 'usuario'

def inicio(request):
    return render(request,'usuario/index.html')
#cadastro e login
def cadastro(request):
    if request.session.get('usuario'):
        return redirect('/usuario/inicio/')
    status = request.GET.get('status')
    return render(request, 'usuario/cadastro.html', {'status': status})

def valida_cadastro(request):
    nome    = request.POST.get('nome')
    senha   = request.POST.get('senha')
    email   = request.POST.get('email')

    #usuario = UsrCad(usuario=usuario,email=email,senha=senha)
    #return HttpResponse(f"{usuario}, {senha}, {email}")
    usuario = UsrCad.objects.filter(email = email)
    if len(nome.strip())==0 or len(email.strip())==0: #verifica espaços vazios e anula
        return redirect('/usuario/cadastro/?status=1')

    if len(senha)<8: #verifica senha menor que oito caracteres
        return redirect('/usuario/inicio/?status=2')

    if len(usuario)>0: #verifica se usuario existe
        return redirect('/usuario/cadastro/?status=3')

    try: #se tudo OK, salva no Banco de Dados
        senha = sha256(senha.encode()).hexdigest()
        usuario = UsrCad(nome=nome,senha=senha,email=email)
        usuario.save()
        return redirect('/usuario/cadastro/?status=0')
    except: #caso Contrario sinaliza como erro do sistema
        return redirect('/usuario/cadastro/?status=4')

def login(request):
    def login(request):
        if request.session.get('usuario'):
            return redirect('/usuario/inicio/')
    status = request.GET.get('status')
    return render(request, 'usuario/login.html', {'status': status})

def validar_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    senha = sha256(senha.encode()).hexdigest()

    usuario = UsrCad.objects.filter(email = email).filter(senha = senha) #buscando do BD
    if len(usuario) == 0: #se não existe usuario
        return redirect('/usuario/inicio/?status=1')
    elif len(usuario) > 0: #se existe usuario, pois nao existe repetido
        request.session['usuario'] = usuario[0].id #armazena globalmente o ID do usuario
        return redirect(f'/perfil/inicio/')

    return HttpResponse(f"{email} {senha}")

def sair(request):
    request.session.flush()
    return redirect('/usuario/inicio/')
#categorias
class SelecionaCategoria(CreateView):
    model = Categoria
    fields = '__all__'
    template_name = 'usuario/form.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Pré-Cadastro de Usuário'
        context['texto1'] = 'Selecione uma opção de pré-cadastro'
        #context['botaoD'] = 'Aluno Novo'
        context['botaoC'] = 'Avançar'
        #context['botaoB'] = 'Limpar'
        context['botaoA'] = 'Cancelar'
        return context
    success_url = '/usuario/dados/'

class BP(CreateView):
    model = BancaPermanente
    fields = '__all__'
    template_name = 'usuario/form.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Pré-Cadastro de Usuário'
        context['texto1'] = 'Insira seus dados para o pré-cadastro'
        #context['botaoD'] = 'Aluno Novo'
        context['botaoC'] = 'Avançar'
        #context['botaoB'] = 'Limpar'
        context['botaoA'] = 'Cancelar'
        return context
    success_url = '/usuario/dados/'

class AP(CreateView):
    model = AtendimentoPersonalizado
    fields = '__all__'
    template_name = 'usuario/form.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Pré-Cadastro de Usuário'
        context['texto1'] = 'Insira seus dados para o pré-cadastro'
        #context['botaoD'] = 'Aluno Novo'
        context['botaoC'] = 'Avançar'
        #context['botaoB'] = 'Limpar'
        context['botaoA'] = 'Cancelar'
        return context
    success_url = '/usuario/dados/'

class GeraComprovante_AP(ListView):
    model = AtendimentoPersonalizado

class GeraComprovante_BP(ListView):
    model = BancaPermanente

class CompDetalheAP(DetailView):
    model = AtendimentoPersonalizado

class CompDetalheBP(DetailView):
    model = BancaPermanente
#Cadastro de Aluno
"""class CadastroAlunoUsuario(CreateView):
    model = UsrCad
    fields = '__all__'
    template_name = 'usuario/form.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Cadastro de Acesso de Usuário'
        context['texto1'] = 'Preencha seus dados completos, para melhor configuração do seu perfil'
        context['botaoC'] = 'Avançar'
        context['botaoB'] = 'Limpar'
        context['botaoA'] = 'Cancelar'
        return context
    success_url = '/usuario/aluno/'
"""
"""class UsrLog(CreateView):
    model = UsrLog
    fields = '__all__'
    template_name = 'usuario/form.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Acesso de Usuário'
        context['texto1'] = 'Preencha seus dadospara acessar seu perfil'
        context['botaoC'] = 'Acessar'
        #context['botaoB'] = 'Limpar'
        context['botaoA'] = 'Cancelar'
        return context
    success_url = '/'"""

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

class Parentesco(CreateView):
    model = Parentesco
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

class DocP(CreateView):
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

class DocP2(CreateView):
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
    success_url = '/usuario/contato/'

class Contato(CreateView):
    model = Contato
    fields = '__all__'
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
    fields = '__all__'
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
    success_url = '/usuario/imagem/'

class Imagem(CreateView):
    model = Imagens
    fields = '__all__'
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
