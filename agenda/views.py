from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView
from django.urls import reverse_lazy, reverse, path
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render

import pandas as pd
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

def nivel(request):

    return render(request, 'agenda/agendador.html', {'nivel':nivel})

def disc(request):
    from agenda.models import nivel
    nivel = Nivel.objects.all()
    if nivel == 'fundamental':
        df = pd.read_excel("./bdados/disciplina_professores.xlsx", sheet_name='disc_nivel')
        dfd = df.fundamental
        disc =dfd
    else:
        df = pd.read_excel("./bdados/disciplina_professores.xlsx", sheet_name='disc_nivel')
        dMd = df.medio
        disc =dMd
    disc = disc
    return render(request, 'agenda/agendador.html', {'disciplina':disciplina})

def person_create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person_add')
    return render(request, 'persons/home.html', {'form': form})


def person_update_view(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)
    return render(request, 'persons/home.html', {'form': form})


# AJAX
def load_cities(request):
    country_id = request.GET.get('country_id')
    cities = City.objects.filter(country_id=country_id).all()
    return render(request, 'persons/city_dropdown_list_options.html', {'cities': cities})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)

"""def cria_agendamento(request):
    nivel = Nivel.objects.all()
    if nivel == 'fundamental':
        df = pd.read_excel("./bdados/disciplina_professores.xlsx", sheet_name='disc_nivel')
        dfd = df.fundamental
        disc =dfd
    else:
        df = pd.read_excel("./bdados/disciplina_professores.xlsx", sheet_name='disc_nivel')
        dfd = df.medio
        disc =dfd

    disc = disc
    prof = []
    return render(request, 'agenda/agendador.html', {'nivel':nivel, 'disc':disc, 'prof':prof})
    print(disc)"""
"""def load_funcoes(request):
    nivel_id = request.GET.get('nivel_id')
    prof = ProfDisciplina.objects.filter(nivel_id=nivel_id).all()
    return render(request, 'agenda/agendador.html', {'prof':prof})"""

#-------------------------------------------------------------
"""def escolhenivel(request):
    nivel = Nivel.objects.all()
    return render(request,'agenda/form2.html',{'nivel':nivel})

def escolhedisciplina(request):

    if escolhenivel == 'fundamental':
        df = pd.read_excel("./bdados/disciplina_professores.xlsx", sheet_name='disc_nivel')
        dfd = df.fundamental
        disc =dfd
    else:
        df = pd.read_excel("./bdados/disciplina_professores.xlsx", sheet_name='disc_nivel')
        dfd = df.medio
        disc =dfd
    print(disc)
    prof = []
    return render(request,'agenda/form2.html',{'disc':disc, 'prof':prof})
"""
"""def pega_nivel(request):
    df = pd.read_excel("./bdados/disciplina_professores.xlsx", sheet_name='Planilha1')
    dfn = df.nivel
    nivel = {'dfn':dfn}
    return render(request, 'agenda/form2.html', nivel)

def pega_disciplina(request):
    if nivel == 'Fundamental':
        df = pd.read_excel("./bdados/disciplina_professores.xlsx", sheet_name='Planilha1')
        dfd = df.query('nivel=="fundamental"')
        disc = {'dfd':dfd}
        return render(request, 'agenda/form2.html', disc)
    else:
        df = pd.read_excel("./bdados/disciplina_professores.xlsx", sheet_name='Planilha1')
        dfn = df.nivel
        nivel = {'dfn':dfn}
        return render(request, 'agenda/form2.html', nivel)
    return render(request, 'agenda/form2.html', disc)
"""
"""class AgendaNvl(CreateView):
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

"""
'''class AgendaDsc(CreateView):
    model = Disciplinas
    fields = '__all__'
    template_name = 'agenda/form2.html'

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
'''
class AgendaSucesso(TemplateView):
    template_name = 'agenda/sucesso.html'
