from django.db import models

DATABASE = 'db_minalba'

class Placa(models.Model):
    placa = models.CharField(max_length=255, primary_key=True)
    classificacao = models.CharField(max_length=255)

    class Meta:
        db_table = '"sc_placa"."tb_placas"'

    def __str__(self) -> str:
        return self.placa

    
    @staticmethod
    def query_all():
        placas = Placa.objects.using(DATABASE).all()
        return placas
    
    @staticmethod
    def get(placa_codigo):
        placa = Placa.objects.using(DATABASE).get(placa=placa_codigo)
        return placa

