from django.shortcuts import redirect, render
from django.contrib import messages

from visitantes.forms import VisitanteForm

# @login_required
def registrar_visitante(request):
    form = VisitanteForm()
    
    if request.method == 'POST':
        form = VisitanteForm(request.POST)
        
        if form.is_valid():
            visitante = form.save(commit=False)
            
            visitante.registrado_por = request.user.porteiro
            visitante = form.save()
            
            messages.success(request,'Visitante registrado com sucesso')
            return redirect('index')
        
    context ={
        'nome_pagina': 'Registrar visitante',
        'form': form
    }
    
    return render(request,'registrar_visitante.html',context)