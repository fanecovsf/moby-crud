from django.shortcuts import render
from django.http.response import JsonResponse
from minalba.models import Placa

def placas(request):
    if request.method == 'GET':
        return JsonResponse({'data':Placa.query_all()}, safe=False)
