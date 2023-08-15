from django.shortcuts import render, redirect
from minalba.models import Placa
from util.util import Util

def placas(request):
    search_placa = request.GET.get('search', '')
    placas = Placa.query_all()

    

    if search_placa:
        placas = placas.filter(placa__contains=search_placa)

    else:
        pass

    page = Util.pagination(placas, 100, request)

    return render(request, 'pages/placas-minalba.html', context={
        'page':page
    })
    
def edit_placa(request, id):
    placa = Placa.objects.get(placa=id)

    if request.method == 'GET':
        return render(request, 'pages/edit-placas-minalba.html', context={
            'placa':placa
        })
    
    elif request.method == 'POST':
        placa.classificacao = request.POST.get('classificacao')
        placa.save()
        return redirect('placas')

