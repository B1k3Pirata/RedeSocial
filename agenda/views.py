from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView
from django.urls import reverse_lazy, reverse, path
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render

import pandas as pd
import sqlite3 as sql
import json
from agenda.models import Nivel, Disciplinas, Professor
#from usuario.models import Matricula, AlunoDados, Imagens
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

#@login_required

class InicioAgenda(TemplateView):
    template_name = 'agenda/inicioagenda.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Agendamento de Atividade'
        context['subt'] = 'Bem-Vindo(a)!'
        context['texto'] = 'Preencha os campos pedidos, para que posssamos melhor atende-lo(a)'

        return context

def escolhe(request):
    nivel = Nivel.objects.all()
    disc = []
    grupo = []
    return render(request,'agenda/agendador.html',{'nivel':nivel,'disc':disc,'grupo':grupo})

def load_funcoes(request):
    nivelID = request.GET.get('nivelID')
    grupo = GrupoFucao.objects.filter(nivelID=nivelID).all()
    return render(request, 'agenda/ajax/funcao_ajax.html',{'grupo':grupo})

class AgendaSucesso(TemplateView):
    template_name = 'agenda/sucesso.html'
