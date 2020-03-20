from django.db import models
from zonas.models import Zona

class Mensaje(models.Model):
    texto = models.TextField()
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE)
