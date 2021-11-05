from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from usuario.models import Matricula, AlunoDados, Imagens


def usr(request):
	cusr = request.user
	print(cusr.id)
