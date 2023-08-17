from moby.abstract_models import BaseTransportadora

DATABASE = 'db_vibra'

class Transportadora(BaseTransportadora):

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
