from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Lista


def criar_convidado(request):
    if request.method == 'GET':
        lista = Lista.objects.all()
        return render(request, 'criar_convidado.html', {'lista':lista})
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        relacao = request.POST.get('relacao')
        confirmado = request.POST.get('confirmado')
        
        lista = Lista(
            nome = nome,
            relacao = relacao,
            confirmado = confirmado
        )
        
        lista.save()
        
        return redirect('criar_convidado')
    
def deletar_convidado(request, id):
    convidado = get_object_or_404(Lista, id=id)
    convidado.delete()
    
    return redirect('criar_convidado')


def atualizar_convidado(request, id):
    lista = get_object_or_404(Lista, id=id)
    
    nome = request.POST.get('nome')
    relacao = request.POST.get('relacao')
    confirmado = request.POST.get('confirmado')
    
    lista.nome = nome
    lista.relacao = relacao
    lista.confirmado = confirmado
    
    lista.save()
    
    return redirect('criar_convidado')