from django.urls import path
from .views import Base, Landing
urlpatterns = [
    #path('', Base.as_view(), name='inicio'),
    path('', Landing.as_view(), name='intro')
]
