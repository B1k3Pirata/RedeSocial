from django.urls import path
from .views import *
from . import views

app_name = 'agenda'

urlpatterns = [
    path('agenda/agenda1', views.Agendar1.as_view(),name='agendar1'),
    path('agenda/agenda2', views.Agendar2.as_view(),name='agendar2'),
    path('agenda/agenda3', views.Agendar3.as_view(),name='agendar3'),
    path('agenda/agenda4', views.Agendar4.as_view(),name='agendar4'),
    path('agenda/sucesso', views.Concluiu.as_view(), name='sucesso'),
    #path('agenda/list', views.AgendaList.as_view(), name='lista'),
    #path('agenda/<slug:slug>', views.AgendaDet.as_view(), name='detalhe'),
]
