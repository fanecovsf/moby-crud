from django.db import models

DATABASE = 'default'

class Cliente(models.Model):
    codigo = models.CharField(max_length=255, primary_key=True)
    nome = models.CharField()
    modelo_de_negocio = models.CharField()
    tipo_de_cliente = models.CharField()
    outbound = models.BooleanField()

    def __str__(self) -> str:
        return f'Código: {self.codigo}, Nome: {self.nome}'
    

    @staticmethod
    def query_all():
        clientes = Cliente.objects.using(DATABASE).all()
        return clientes
    
    @staticmethod
    def get(codigo):
        cliente = Cliente.objects.using(DATABASE).get(codigo=codigo)
        return cliente
    

class Produto(models.Model):
    produto_codigo = models.CharField(primary_key=True)
    produto_nome = models.CharField()
    produto_tipo = models.CharField()
    produto_grupo = models.CharField()
    produto_torre = models.BooleanField() #True=Torre / False=Vibra

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

    

class Transportadora(models.Model):
    transportadora_codigo_sap = models.CharField(primary_key=True)
    transportadora_nome_sap = models.CharField()
    transportadora_cnpj = models.CharField()
    transportadora_grupo_atlas = models.CharField()

    def __str__(self) -> str:
        return f'Código SAP: {self.transportadora_codigo_sap}, Nome SAP: {self.transportadora_nome_sap}'


    @staticmethod
    def query_all():
        Transportadora.objects.using(DATABASE).all()

    @staticmethod
    def get(codigo):
        Transportadora.objects.using(DATABASE).get(transportadora_codigo_sap=codigo)
