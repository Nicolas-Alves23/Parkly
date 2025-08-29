from django.db import models

class Placa(models.Model):
    placa = models.CharField(max_length=10, unique=True)
    descricao = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.placa


STATUS_CHOICES = [
    ('OCUPADO', 'OCUPADO'),
    ('LIVRE', 'LIVRE'),
]

TIPO_VAGA_CHOICES = [
    ('PCD', 'PCD'),
    ('GESTOR', 'GESTOR'),
    ("IDOSO", "IDOSO"),
    ("COMUM", "COMUM")
]

class Vaga(models.Model):
    numero_vaga = models.CharField(max_length=150, unique=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    tipo_vaga = models.CharField(max_length=10, choices=TIPO_VAGA_CHOICES)

    def __str__(self):
        return self.numero_vaga