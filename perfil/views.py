from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse

from usuario.models import *


#--CADASTRO DE DADOS DE ACESSO
from django.contrib.auth.models import User
#from .forms import *

app_name = 'perfil'

#aluno
def inicioperfil(request):
    if request.session.get('usuario'):
        usuario = UsrCad.objects.get(id = request.session['usuario']).nome
        avatar  = Imagens.objects.get(id=request.session['usuario']).avatar
        nivel   = EduCad.objects.get(id = request.session['usuario']).nivel
        matric  = EduCad.objects.get(id = request.session['usuario']).matric
        ano     = EduCad.objects.get(id=request.session['usuario']).ano
        #return HttpResponse(f'Olá {usuario}{avatar}')
        return render(request, 'perfil/inicio.html', {'usuario':usuario,'avatar':avatar,'nivel':nivel,'matric':matric,'ano':ano})
    else:
        return redirect('/usuario/login/?status=2')

def avatar(request):
    if request.session.get('usuario'):
        #avatar = Imagens.objects.get(avatar=request.session['usuario']).avatar
        avatar = get_object_or_404(UsrCad, pk=request.session['usuario'])
        context = {'avatar':avatar}
    return render(request, 'perfil/inicio.html', context)
