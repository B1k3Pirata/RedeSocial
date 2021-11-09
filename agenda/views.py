from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView
from django.urls import reverse_lazy, reverse, path
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from agenda.models import *
#from usuario.models import Matricula, AlunoDados, Imagens
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
#@login_required
"""def filtros(request):
    pass

class InicioAgenda(TemplateView):

    template_name = 'agenda/inicioagenda.html'

class Agendar1(CreateView):
    model = Disciplinas
    fields = [
        'nome','sobrenome', 'matricula', 'turno','email','cell','slug',
    ]
    template_name = 'agenda/form.html'
    success_url = '/agenda/sucesso/'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['titulo'] = 'Agendamento de Aula'
        context['botaoA'] = 'Agenda!'
        context['botaoB'] = 'Reseta'
        return context"""
"""
class Agendar2(CreateView):
    model = AgendamentoNVL
    fields = [
        'nivel'
    ]
    template_name = 'agenda/form.html'
    success_url = '/agenda/agenda3/'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['titulo'] = 'Agendamento de Aula'
        context['botaoA'] = 'Avançar'
        context['botaoB'] = 'Reseta'
        return context

class Agendar3(CreateView):
    model = AgendamentoDSC
    fields = [
        'dF','dM'
        ]
    template_name = 'agenda/form.html'
    success_url = '/agenda/agenda4/'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['titulo'] = 'Agendamento de Aula'
        context['botaoA'] = 'Avançar'
        context['botaoB'] = 'Reseta'
        return context

class Agendar4(CreateView):
    model = AgendamentoPRF
    fields = [
        'professor',
        ]
    template_name = 'agenda/form.html'
    success_url = '/agenda/sucesso/'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['titulo'] = 'Agendamento de Aula'
        context['botaoA'] = 'Avançar'
        context['botaoB'] = 'Reseta'
        return context"""

class Concluiu(TemplateView):
    template_name = 'agenda/sucesso.html'
#class Sucesso(CreateView):
#    template_name = 'agenda/sucess.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['titulo'] = 'Agendamento Concluido'
        context['texto'] = 'Seu agendamento foi concluido com sucesso, escolha uma das opções abaixo ou selecione no menu.'
        context['botaoA'] = 'Novo Agendamento'
        context['botaoB'] = 'Perfil'
        context['botaoC'] = 'Lista de Agendamentos'
        return context

#Listagem e Detalhamento
#@login_required
"""class AgendaList(ListView):
    model = Agendamento
    def get_querysert(self):
        self.agendamento_list = Agendamento.objects.filter(usuario=self.request.user)
        return self.agendamento_list
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['titulo'] = 'Agendamento Concluido'
        context['texto'] = 'Seu agendamento foi concluido com sucesso, escolha uma das opções abaixo ou selecione no menu.'
        context['botaoA'] = 'Novo Agendamento'
        context['botaoB'] = 'Perfil'
        context['botaoC'] = 'Inicio'
        context['botaoAv'] = 'avaliar'
        context['botaoex'] = 'aula'
        return context
#@login_required
class AgendaDet(DetailView):
    model = Agendamento
"""
