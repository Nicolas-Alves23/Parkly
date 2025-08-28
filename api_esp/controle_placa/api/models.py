from django.db import models

class Placa(models.Model):
    placa = models.CharField(max_length=10, unique=True)
    descricao = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.placa
