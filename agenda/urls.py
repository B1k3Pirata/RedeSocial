from django.urls import path
from .views import *
from . import views

app_name = 'agenda'

urlpatterns = [
    path('inicioagenda', views.InicioAgenda.as_view(),name='inicioagenda'),
    path('agenda1', views.Agendar1.as_view(),name='agendar1'),
    #path('agenda2', views.Agendar2.as_view(),name='agendar2'),
    #path('agenda3', views.Agendar3.as_view(),name='agendar3'),
    #path('agenda4', views.Agendar4.as_view(),name='agendar4'),
    path('sucesso', views.Concluiu.as_view(), name='sucesso'),
    #path('agenda/list', views.AgendaList.as_view(), name='lista'),
    #path('agenda/<slug:slug>', views.AgendaDet.as_view(), name='detalhe'),
]
