from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Lista
from django.utils import timezone
from django.http import JsonResponse
from django.utils.timezone import now


def criar_convidado(request):
    if request.method == 'GET':
        busca = request.GET.get('q')

        lista = Lista.objects.filter(expiradate__isnull=True).order_by('id')

        if busca:
            lista = lista.filter(nome__icontains=busca)
        
        total = Lista.objects.count()
        total_sim = Lista.objects.filter(confirmado="Sim").count()
        total_nao = Lista.objects.filter(confirmado="Não").count()
        total_menor = Lista.objects.filter(confirmado="Sim",idade_menor="Sim").count()
        total_maior = Lista.objects.filter(confirmado="Sim",idade_maio="Sim").count()

        context = {
            "lista": lista,
            "total": total,
            "total_sim": total_sim,
            "total_nao": total_nao,
            "total_menor":total_menor,
            "total_maior":total_maior,
        }
    
        return render(request, 'criar_convidado.html', context)
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        relacao = request.POST.get('relacao')
        confirmado = request.POST.get('confirmado')
        idade_menor = request.POST.get('idade_menor')
        idade_maio = request.POST.get('idade_maio')
        contato = request.POST.get('contato')
        
        lista = Lista(
            nome = nome,
            relacao = relacao,
            confirmado = confirmado,
            idade_menor = idade_menor,
            idade_maio = idade_maio,
            contato = contato
        )
        
        lista.save()
        

        
        return redirect('criar_convidado')
    
def deletar_convidado(request, id):
    convidado = get_object_or_404(Lista, id=id)
    
    convidado.expiradate = timezone.now()
    convidado.save()
    
    return redirect('criar_convidado')

    
def deletar_multiplos(request):
    if request.method == "POST":
        ids = request.POST.getlist('ids')

        if ids:  # 👈 ESSENCIAL
            Lista.objects.filter(id__in=ids).update(expiradate=now())

    return redirect('criar_convidado')


def atualizar_convidado(request, id):
    lista = get_object_or_404(Lista, id=id)
    
    nome = request.POST.get('nome')
    relacao = request.POST.get('relacao')
    confirmado = request.POST.get('confirmado')
    idade_menor = request.POST.get('idade_menor')
    idade_maio = request.POST.get('idade_maio')
    contato = request.POST.get('contato')
    
    lista.nome = nome
    lista.relacao = relacao
    lista.confirmado = confirmado
    lista.idade_menor = idade_menor
    lista.idade_maio = idade_maio
    lista.contato = contato
    
    lista.save()
    
    return redirect('criar_convidado')