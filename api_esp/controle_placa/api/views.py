from rest_framework import viewsets
from .models import Placa
from .serializers import PlacaSerializer

class VerificarPlaca(viewsets.ModelViewSet):
    queryset = Placa.objects.all()
    serializer_class = PlacaSerializer
    
    def post(self, request):
        placa_recebida = request.data.get("placa", "").upper()
        if Placa.objects.filter(placa=placa_recebida).exists():
            return Response({"autorizado": True})
        return Response({"autorizado": False})
