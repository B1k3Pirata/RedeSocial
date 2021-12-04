from django.urls import path
from .views import Base, Landing

from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

app_name = "basePG"

urlpatterns = [
    #path('', Base.as_view(), name='inicio'),
    path('', Landing.as_view(), name='intro'),

    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico'))),
]
