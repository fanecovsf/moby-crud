from django.shortcuts import render, redirect
from util.util import Util

from vibra.models import Cliente, Produto, Transportadora
from vibra.serializers import TransportadoraSerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

def clientes(request):
    search_name = request.GET.get('search-name')
    search_inbound = request.GET.get('drop')
    search_modelo = request.GET.get('search-modelo')
    clientes = Cliente.query_all().order_by('codigo_sap')

    if search_name:
        clientes = clientes.filter(nome_sap__contains=search_name)

    if search_inbound != 'Seleciona a operação':
        if search_inbound == 'inbound':
            clientes = clientes.filter(outbound=False)
        else:
            clientes = clientes.filter(outbound=True)

    if search_modelo:
        clientes = clientes.filter(modelo_de_negocio__contains=search_modelo)

    page = Util.pagination(clientes, 100, request)

    return render(request, 'pages/vibra-clientes.html', context={
        'page':page,
        'search_name':search_name,
        'search_inbound':search_inbound,
        'search_modelo':search_modelo
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
    produtos = Produto.query_all().order_by('produto_codigo')
    search_name = None
    search_codigo = None

    if request.method == 'POST':
        search_name = request.POST.get('search-name')
        search_codigo = request.POST.get('search-codigo')

        if search_name:
            produtos = produtos.filter(produto_nome__contains=search_name)

        if search_codigo:
            produtos = produtos.filter(produto_codigo__contains=search_codigo)

        page = Util.pagination(produtos, 100, request)

        return render(request, 'pages/vibra-produtos.html', context={
                'page':page,
                'search_name':search_name,
                'search_codigo':search_codigo
            }
        )

    page = Util.pagination(produtos, 100, request)

    return render(request, 'pages/vibra-produtos.html', context={
            'page':page,
            'search_name':search_name,
            'search_codigo':search_codigo
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
    
    
def transportadoras(request):
    search_cod = request.GET.get('search-cod')
    search_grupo = request.GET.get('search-grupo')
    search_name = request.GET.get('search-nome')
    transportadoras = Transportadora.query_all().order_by('transportadora_codigo_sap')

    if search_cod:
        transportadoras = transportadoras.filter(transportadora_codigo_sap__contains=search_cod)

    if search_grupo:
        transportadoras = transportadoras.filter(transportadora_grupo_atlas__contains=search_grupo)

    if search_name:
        transportadoras = transportadoras.filter(transportadora_nome_sap__contains=search_name)

    page = Util.pagination(transportadoras, 100, request)

    return render(request, 'pages/vibra-transportadoras.html', context={
            'page':page,
            'search_cod':search_cod,
            'search_grupo':search_grupo,
            'search_name':search_name
        }
    )


def transportadora(request, codigo):
    transportadora = Transportadora.get(codigo)

    if request.method == 'POST':
        transportadora.transportadora_grupo_atlas = request.POST.get('grupo')
        transportadora.save()

        return redirect('transportadoras')

    if request.method == 'GET':
        return render(request, 'pages/edit-transportadoras.html', context={
                'transportadora':transportadora
            }
        )
    

class TransportadoraCNPJAPI(APIView):
    def get(self, request):
        transp_cnpj = request.headers.get('cnpj')

        if not transp_cnpj:
            return Response({'erro':'Insira um CNPJ.'},status=status.HTTP_428_PRECONDITION_REQUIRED)

        else:
            try:
                transp = Transportadora.get_cnpj(str(transp_cnpj))
                serializer = TransportadoraSerializer(transp)
                response = Response(serializer.data, status=status.HTTP_200_OK)
                response["Access-Control-Allow-Origin"] = "*"
                return response
            
            except Transportadora.DoesNotExist:
                return Response({'error':'Transportadora não encontrada'} ,status=status.HTTP_404_NOT_FOUND)

