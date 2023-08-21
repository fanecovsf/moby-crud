from rest_framework import serializers

from vibra.models import Transportadora

class TransportadoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transportadora
        
        fields = [
            'transportadora_codigo_sap',
            'transportadora_nome_sap',
            'transportadora_cnpj',
            'transportadora_grupo_atlas'
        ]