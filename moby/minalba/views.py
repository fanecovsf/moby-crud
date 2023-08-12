from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from minalba.models import Placa

def placas(request):
    return render(request, 'pages/placas-minalba.html', context={
        'placas':Placa.query_all()
    })
    
def placa(request, id):
    placa = Placa.objects.get(placa=id)

    if request.method == 'GET':
        return render(request, 'pages/edit-placas-minalba.html', context={
            'placa':placa
        })
    
    elif request.method == 'POST':
        placa.classificacao = request.POST.get('classificacao')
        placa.save()
        return redirect('placas')

