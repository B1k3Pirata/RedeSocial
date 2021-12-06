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

class InicioAgenda(TemplateView):
    template_name = 'agenda/inicioagenda.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Agendamento de Atividade'
        context['subt'] = 'Bem-Vindo(a)!'
        context['texto'] = 'Preencha os campos pedidos, para que posssamos melhor atende-lo(a)'

        return context

class AgendaNvl(CreateView):
    model = Nivel
    fields = '__all__'
    template_name = 'agenda/form.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Agendamento'
        #context['texto1'] = 'Preencha seus dados completos, para melhor configuração do seu perfil'
        context['botaoC'] = 'Avançar'
        context['botaoB'] = 'Limpar'
        context['botaoA'] = 'Cancelar'
        return context
    success_url = '/agenda/ag2/'

class AgendaDsc(CreateView):
    model = Disciplinas
    fields = '__all__'
    template_name = 'agenda/form.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Agendamento de Disciplina'
        #context['texto1'] = 'Preencha seus dados completos, para melhor configuração do seu perfil'
        context['botaoC'] = 'Avançar'
        context['botaoB'] = 'Limpar'
        context['botaoA'] = 'Cancelar'
        return context
    success_url = '/agenda/ag3/'

class AgendaPrf(CreateView):
    model = Professor
    fields = '__all__'
    template_name = 'agenda/form.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = 'Agendamento com Professor'
        #context['texto1'] = 'Preencha seus dados completos, para melhor configuração do seu perfil'
        context['botaoC'] = 'Avançar'
        context['botaoB'] = 'Limpar'
        context['botaoA'] = 'Cancelar'
        return context
    success_url = '/agenda/ok/'

class AgendaSucesso(TemplateView):
    template_name = 'agenda/sucesso.html'
