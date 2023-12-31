from django.urls import path

from vibra import views

urlpatterns = [
    path('clientes/', views.clientes, name='clientes'),
    path('clientes/<codigo>', views.edit_cliente, name='edit_cliente'),
    path('produtos/', views.produtos, name='produtos'),
    path('produtos/<codigo>', views.edit_produto, name='edit_produto'),
    path('transportadoras/', views.transportadoras, name='transportadoras'),
    path('transportadoras/<codigo>', views.transportadora, name='edit_transportadora'),
    path('api/transportadora-cnpj', views.TransportadoraCNPJAPI.as_view(), name='api-transportadora-cnpj')
]