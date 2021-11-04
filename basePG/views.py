from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

app_name='basePG'

class Base(TemplateView):
    template_name = 'basePG/base.html'
