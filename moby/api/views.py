from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from api.models import Transportadora
from api.serializers import TransportadoraSerializer
from api.authentication import APIAuthentication

class APITransportadora(APIView):
    authentication_classes = [APIAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self, request):
        transp_cnpj = request.headers.get('cnpj')

        if not transp_cnpj:
            return Response(status=status.HTTP_428_PRECONDITION_REQUIRED)
        
        else:
            try:
                transp = Transportadora.get_cnpj(transp_cnpj)
                serializer = TransportadoraSerializer(transp, many=True)
                return Response(serializer.data, many=True, status=status.HTTP_200_OK)
            
            except Transportadora.DoesNotExist:
                return Response({'error':'Transportadora não enconstrada'}, status=status.HTTP_404_NOT_FOUND)

