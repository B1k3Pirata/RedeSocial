from django.urls import path
from .views import Base
urlpatterns = [
    path('', Base.as_view(), name='inicio'),    
]
