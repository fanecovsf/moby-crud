from django.db import models

DATABASE = 'db_vibra'

class Cliente(models.Model):
    codigo_sap = models.CharField(max_length=255, primary_key=True)
    nome_sap = models.CharField(max_length=255)
    modelo_de_negocio = models.CharField(max_length=255)
    tipo_de_cliente = models.CharField(max_length=255)
    outbound = models.BooleanField()

    class Meta:
        db_table = '"sc_sap"."tb_clientes"'

    def __str__(self) -> str:
        return f'Código: {self.codigo}, Nome: {self.nome}'
    

    @staticmethod
    def query_all():
        clientes = Cliente.objects.using(DATABASE).all()
        return clientes
    
    @staticmethod
    def get(codigo):
        cliente = Cliente.objects.using(DATABASE).get(codigo_sap=codigo)
        return cliente
    

class Produto(models.Model):
    produto_codigo = models.CharField(max_length=255, primary_key=True)
    produto_nome = models.CharField(max_length=255)
    produto_tipo = models.CharField(max_length=255)
    produto_grupo = models.CharField(max_length=255)
    produto_torre = models.BooleanField() #True=Torre / False=Vibra

    class Meta:
        db_table = '"sc_sap"."tb_produtos"'

    def __str__(self) -> str:
        return f'Código: {self.produto_codigo}, Nome: {self.produto_nome}'
    

    @staticmethod
    def query_all():
        produtos = Produto.objects.using(DATABASE).all()
        return produtos
    
    @staticmethod
    def get(codigo):
        produto = Produto.objects.using(DATABASE).get(produto_codigo=codigo)
        return produto
    
    @staticmethod
    def lista_grupos():
        grupos = Produto.objects.using(DATABASE).values_list('produto_grupo', flat=True).distinct()
        return list(grupos)

    

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
    def get(codigo):
        transportadora = Transportadora.objects.using(DATABASE).get(transportadora_codigo_sap=codigo)
        return transportadora
    
    @staticmethod
    def get_cnpj(cnpj: str):
        transportadora = Transportadora.objects.using(DATABASE).get(transportadora_cnpj=cnpj)
        return transportadora
