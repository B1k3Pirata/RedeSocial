from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.urls import reverse
from django.http import HttpResponse
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from hashlib import sha256

from usuario_prof.models import Acesso, Docente

# Create your views here.
def cadastro(request):
    if request.session.get('usuario'):
        return redirect('/usuario_prof/login/')
    status = request.GET.get('status')
    return render(request, 'usuario_prof/cadastro.html', {'status': status})

def valida_cadastro(request):
    nome  = request.POST.get('nome')
    senha   = request.POST.get('senha')
    email   = request.POST.get('email')

    usuario = Acesso.objects.filter(email = email)
    if len(nome.strip())==0 or len(email.strip())==0: #verifica espaços vazios e anula
        return redirect('/usuario_prof/cadastro/?status=1')

    if len(senha)<8: #verifica senha menor que oito caracteres
        return redirect('/usuario_prof/cadastro/?status=2')

    if len(usuario)>0: #verifica se usuario existe
        return redirect('/usuario_prof/cadastro/?status=3')

    try: #se tudo OK, salva no Banco de Dados
        senha = sha256(senha.encode()).hexdigest()
        usuario = Acesso(nome=nome,senha=senha,email=email)
        usuario.save()
        return redirect('/usuario_prof/prof/?status=0')
    except: #caso Contrario sinaliza como erro do sistema
        return redirect('/usuario_prof/cadastro/?status=4')

def login(request):
    if request.session.get('usuario'):
        return redirect('/usuario_prof/prof/')
    status = request.GET.get('status')
    return render(request, 'usuario_prof/login.html', {'status': status})

def validar_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    senha = sha256(senha.encode()).hexdigest()

    usuario = Acesso.objects.filter(email = email).filter(senha = senha) #buscando do BD
    if len(usuario) == 0: #se não existe usuario
        return redirect('/usuario_prof/cadastro/?status=1')
    elif len(usuario) > 0: #se existe usuario, pois nao existe repetido
        request.session['usuario'] = usuario[0].id #armazena globalmente o ID do usuario
        return redirect(f'/usuario_prof/perfilp/')
        request.session["usuario"]=usuario[0].id
        return redirect(f"/usuario_prof/perfilp/")
    return HttpResponse(f"{email} {senha}")

def sair(request):
    request.session.flush()
    return redirect('/usuario_prof/login/')

class DocenteCreate(CreateView):
    model = Docente
    fields = '__all__'
    template_name = 'usuario_prof/form.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Cadastro de Acesso de Usuário'
        context['texto1'] = 'Preencha seus dados completos, para melhor configuração do seu perfil'
        context['botaoC'] = 'Avançar'
        context['botaoB'] = 'Limpar'
        context['botaoA'] = 'Cancelar'
        return context
    success_url = '/usuario_prof/sucesso/'

class Sucesso(TemplateView):
    template_name = 'usuario/sucesso.html'

#perfil
#professor
def inicioperfildocente(request):
    if request.session.get('usuario'):
        usuario = Docente.objects.get(id=request.session['usuario']).nome
        usuarios = Docente.objects.get(id=request.session['usuario']).snome
        avatar  = Docente.objects.get(id=request.session['usuario']).avatar
        nivel  = Docente.objects.get(id=request.session['usuario']).nivel
        disc  = Docente.objects.get(id=request.session['usuario']).disciplina
        trn  = Docente.objects.get(id=request.session['usuario']).turno
        return render(request, 'usuario_prof/perfilp.html',{'usuario':usuario, 'usuarios':usuarios, 'avatar':avatar, 'nivel':nivel, 'disc':disc,'trn':trn})
    else:
        return redirect('/usuario_prof/login/?status=2')
