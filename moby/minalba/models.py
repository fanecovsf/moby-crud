from typing import Any
from django.db import models
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
import json

DATABASE = 'default'

class Placa(models.Model):
    placa = models.CharField(max_length=255, primary_key=True)
    classificacao = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.placa

    
    @staticmethod
    def query_all():
        placas = Placa.objects.using(DATABASE).all()
        return placas
    
    @staticmethod
    def filter_placa(placa):
        placas = Placa.objects.using(DATABASE).filter(placa__contains=placa)
        return placas
