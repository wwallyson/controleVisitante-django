from django.utils import timezone
from django.shortcuts import render
from visitantes.models import Visitante

# Create your views here.
def index(request):
    
    todos_visitantes = Visitante.objects.order_by('horario_chegada')
    
    visitante_aguardando = todos_visitantes.filter(status='AGUARDANDO')
    visitante_em_visita = todos_visitantes.filter(status='EM_VISITA')
    visitante_finalizado = todos_visitantes.filter(status='FINALIZADO')
    
    hora_atual = timezone.now()
    mes_atual = hora_atual.month
    visitantes_mes = todos_visitantes.filter(horario_chegada__month = mes_atual)
    
    context = {
        'nome_pagina' : 'Inicio da Dashboard',
        'todos_visitantes' : todos_visitantes,
        'visitante_aguardando' : visitante_aguardando.count(),
        'visitante_em_visita' : visitante_em_visita.count(),
        'visitante_finalizado' : visitante_finalizado.count(),              
        'visitantes_mes' : todos_visitantes.count(),
    }
    return render(request, 'index.html', context)