from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Placa

class VerificarPlaca(APIView):
    def post(self, request):
        placa_recebida = request.data.get("placa", "").upper()
        if Placa.objects.filter(placa=placa_recebida).exists():
            return Response({"autorizado": True})
        return Response({"autorizado": False})
