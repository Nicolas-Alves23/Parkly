from django.urls import path
from .views import VerificarPlaca

urlpatterns = [
    path('verificar-placa/', VerificarPlaca.as_view(), name='verificar_placa'),
]
