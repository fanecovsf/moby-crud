from django.urls import path

from vibra import views

urlpatterns = [
    path('clientes/', views.clientes, name='clientes'),
    path('clientes/<codigo>', views.edit_cliente, name='edit_cliente')
]