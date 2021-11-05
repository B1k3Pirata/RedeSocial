from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse

from .models import *

#--CADASTRO DE DADOS DE ACESSO
from django.contrib.auth.models import User
#from .forms import *

class PerfilInicio(TemplateView):
    template_name = 'perfil/perfil.html'

def PessoalList(request):
    pessoal = Perfil.objects.all()
    contexto = {
        'pessoal': pessoal,
    }
    return render(request,'perfil/perfil.html', contexto)

def AvatarList(request):
    avatar = Imagens.objects.all()
    contexto = {
        'avatar':avatar,
    }
    return render(request, 'perfil/perfil.html',contexto)

def lista_avatar(request):
    contexto = {'avatar':Imagens.objects.all()}
    return render(request,'perfil/avatar_list.html', contexto)
