from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView
from django.urls import reverse_lazy, reverse, path
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from agenda.models import *
#from usuario.models import Matricula, AlunoDados, Imagens
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
#@login_required
def filtros(request):
    pass

class InicioAgenda(TemplateView):
    template_name = 'agenda/inicioagenda.html'
