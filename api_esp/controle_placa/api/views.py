from rest_framework import viewsets
from .models import Placa,Vaga
from .serializers import PlacaSerializer, VagaSerializer

class VerificarPlaca(viewsets.ModelViewSet):
    queryset = Placa.objects.all()
    serializer_class = PlacaSerializer
    
    def post(self, request):
        placa_recebida = request.data.get("placa", "").upper()
        if Placa.objects.filter(placa=placa_recebida).exists():
            return Response({"autorizado": True})
        return Response({"autorizado": False})

class ManterVaga(viewsets.ModelViewSet):
    queryset = Vaga.objects.all()
    serializer_class = VagaSerializer

    #Filtros
    def get_queryset(self):
        queryset = Vaga.objects.all()
        status = self.request.query_params.get("status")
        tipo_vaga = self.request.query_params.get("tipo_vaga")

        if status is not None:
            queryset = queryset.filter(status=status)
        elif tipo_vaga is not None:
            queryset = queryset.filter(tipo_vaga=tipo_vaga)
        return queryset