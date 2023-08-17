from django.db import models

DATABASE = 'db_vibra'

class Transportadora(models.Model):
    transportadora_codigo_sap = models.CharField(max_length=255, primary_key=True)
    transportadora_nome_sap = models.CharField(max_length=255)
    transportadora_cnpj = models.CharField(max_length=255)
    transportadora_grupo_atlas = models.CharField(max_length=255)

    class Meta:
        db_table = '"sc_sap"."tb_transportadoras"'

    def __str__(self) -> str:
        return f'Código SAP: {self.transportadora_codigo_sap}, Nome SAP: {self.transportadora_nome_sap}'


    @staticmethod
    def query_all():
        transportadoras = Transportadora.objects.using(DATABASE).all()
        return transportadoras
    
    @staticmethod
    def get_cnpj(cnpj: str):
        transportadora = Transportadora.objects.using(DATABASE).get(transportadora_cnpj=cnpj)
        return transportadora
