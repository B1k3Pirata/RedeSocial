from django.urls import path
from .views import *
from . import views

app_name = 'agenda'

urlpatterns = [
    path('inicioagenda/', views.InicioAgenda.as_view(),name='inicioagenda'),
    path('ag1/', AgendaNvl.as_view(), name='agenda_nivel'),
    path('ag2/', AgendaDsc.as_view(), name='agenda_disciplina'),
    path('ag3/', AgendaPrf.as_view(), name='agenda_professor'),
    path('ok/', AgendaSucesso.as_view(), name='agenda_sucesso'),
]
