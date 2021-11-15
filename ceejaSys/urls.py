
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('basePG.urls')),
    path('usuario/', include('usuario.urls', namespace='usuario')),
    path('agenda/', include('agenda.urls', namespace='agenda')),
    path('perfil/', include('perfil.urls', namespace='perfil')),
]
