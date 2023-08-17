from django.db import models

class BaseTransportadora(models.Model):
    transportadora_codigo_sap = models.CharField(max_length=255, primary_key=True)
    transportadora_nome_sap = models.CharField(max_length=255)
    transportadora_cnpj = models.CharField(max_length=255)
    transportadora_grupo_atlas = models.CharField(max_length=255)

    class Meta:
        abstract = True
        db_table = '"sc_sap"."tb_transportadoras"'