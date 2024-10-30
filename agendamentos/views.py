from django.shortcuts import render

# agendamentos/views.py

from django.shortcuts import render

from home.models import Agendamento

def status_agendamentos(request):
    agendamentos = Agendamento.objects.all().order_by('-data_agend')
    # return render(request, 'agendamento', {'data_agend': data_agend })
    
    context = {
        'agendamentos': agendamentos
    }
   
    return render(request, 'agendamentos/status_agendamentos.html', context)

