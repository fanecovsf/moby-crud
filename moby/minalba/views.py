from django.shortcuts import render, redirect
from minalba.models import Placa

def placas(request):
    search_placa = request.GET.get('search', '')

    if search_placa:
        placas = Placa.filter_placa(search_placa)

    else:
        placas = Placa.query_all()

    return render(request, 'pages/placas-minalba.html', context={
        'placas':placas
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

