from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from django.shortcuts import render
from .models import Morador
from django.contrib.auth.decorators import login_required

@login_required
def moradores(request):
    todos_moradores = Morador.objects.order_by()
    
    context = {
        'nome_pagina' : 'Inicio da Dashboard',
        'todos_moradores': todos_moradores,

    }
    
    return render(request,'moradores.html', context)