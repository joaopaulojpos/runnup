from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Corridas(models.Model):
    distancia = models.DecimalField(max_digits=5, decimal_places=2)
    tempo = models.TimeField(blank=True, null=True)
    data_da_corrida = models.DateField(null=False, blank=False)
    sentimento = models.CharField(max_length=10, null=True, blank=True)
    observacoes = models.CharField(max_length=400, blank=True, null=True)
    lancado_em = models.DateTimeField(default=timezone.now)
    corredor = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.distancia)
