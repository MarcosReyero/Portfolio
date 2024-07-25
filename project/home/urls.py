from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),  # La URL principal debería apuntar a la vista 'home'
]
