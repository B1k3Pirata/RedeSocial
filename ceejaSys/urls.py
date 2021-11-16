
from django.contrib import admin
from django.urls import path, include
#para fornecer arquivos estáticos
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('basePG.urls')),
    path('usuario/', include('usuario.urls', namespace='usuario')),
    path('agenda/', include('agenda.urls', namespace='agenda')),
    path('perfil/', include('perfil.urls', namespace='perfil')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#para fornecer arquivos estáticos
