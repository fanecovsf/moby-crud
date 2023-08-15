from django.shortcuts import render, redirect
from minalba.models import Placa
from django.core.paginator import Paginator

def placas(request):
    search_placa = request.GET.get('search', '')
    placas = Placa.query_all()

    placas_paginator = Paginator(placas, 2)
    page_num = request.GET.get('page')
    page = placas_paginator.get_page(page_num)

    if search_placa:
        placas = placas.filter(placa__contains=search_placa)

    else:
        pass

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

