from django.shortcuts import render, redirect

from vibra.models import Cliente

def clientes(request):
    return render(request, 'pages/vibra-clientes.html', context={
        'clientes':Cliente.query_all()
    })

def edit_cliente(request, codigo):
    cliente = Cliente.get(codigo)

    if request.method == 'GET':
        return render(request, 'pages/edit-clientes.html', context={
            'cliente':cliente
        })
    
    if request.method == 'POST':
        cliente.modelo_de_negocio = request.POST.get('modelo')
        cliente.tipo_de_cliente = request.POST.get('tipo_cliente')
        cliente.save()

        return redirect('clientes')

