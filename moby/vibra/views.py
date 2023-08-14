from django.shortcuts import render, redirect

from vibra.models import Cliente, Produto

def clientes(request):
    search_name = request.GET.get('search-name')
    search_inbound = request.GET.get('drop')
    clientes = Cliente.query_all()

    if search_name:
        clientes = clientes.filter(nome__contains=search_name)

    if search_inbound != 'Seleciona a operação':
        if search_inbound == 'inbound':
            clientes = clientes.filter(outbound=False)
        else:
            clientes = clientes.filter(outbound=True)

    return render(request, 'pages/vibra-clientes.html', context={
        'clientes':clientes
        }
    )

def edit_cliente(request, codigo):
    cliente = Cliente.get(codigo)

    if request.method == 'GET':
        return render(request, 'pages/edit-clientes.html', context={
            'cliente':cliente
            }
        )
    
    if request.method == 'POST':
        cliente.modelo_de_negocio = request.POST.get('modelo')
        cliente.tipo_de_cliente = request.POST.get('tipo_cliente')
        cliente.save()

        return redirect('clientes')
    
def produtos(request):
    search_name = request.GET.get('search-name')
    produtos = Produto.query_all()

    if search_name:
        produtos = produtos.filter(produto_nome__contains=search_name)

    return render(request, 'pages/vibra-produtos.html', context={
            'produtos':produtos
        }
    )

def edit_produto(request, codigo):
    produto = Produto.get(codigo)
    lista_grupos = Produto.lista_grupos()

    if request.method == 'GET':
        return render(request, 'pages/edit-produtos.html', context={
                'produto':produto,
                'lista_grupos':lista_grupos
            }
        )
    
    if request.method == 'POST':
        if request.POST.get('torre') == 'Torre':
            torre = True
        else:
            torre = False

        produto.produto_grupo = request.POST.get('grupo-produto')
        produto.produto_torre = torre
        produto.save()

        return redirect('produtos')

