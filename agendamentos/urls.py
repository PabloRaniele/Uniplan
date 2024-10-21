# meu_projeto/urls.py

from django.contrib import admin
from django.urls import path
from agendamentos.views import status_agendamentos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agendamentos/', status_agendamentos, name='status_agendamentos'),
]
