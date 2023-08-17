from django.urls import path

from api.views import APITransportadora

urlpatterns = [
    path('transportadora_cnpj/', APITransportadora.as_view(), name='api=transportadora')
]