from django.db import models

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

