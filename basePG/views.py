from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

app_name='basePG'

class Base(TemplateView):
    template_name = 'basePG/base.html'

class Landing(TemplateView):
    template_name = 'landing/landing.html'

#@login_required
def usuario(request):
    cusr = request.user
    usrid = cusr.id
    context = {'usrid':usrid}
    return render(request, 'basePG/base.html', context)
