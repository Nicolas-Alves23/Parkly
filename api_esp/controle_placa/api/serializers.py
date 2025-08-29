from rest_framework import serializers
from .models import Placa, Vaga

class PlacaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Placa
        fields = ['placa', 'descricao']

class VagaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaga
        fields = '__all__'