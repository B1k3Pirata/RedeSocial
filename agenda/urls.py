from django.urls import path
from .views import *
from . import views

app_name = 'agenda'

urlpatterns = [
    path('inicioagenda/', views.InicioAgenda.as_view(),name='inicioagenda'),

]
