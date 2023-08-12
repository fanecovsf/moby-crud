from django.urls import path

from minalba import views

urlpatterns = [
    path('placas/', views.placas, name='placas'),
    path('placas/<id>/', views.edit_placa, name='edit_placa')
]