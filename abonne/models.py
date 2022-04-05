from django.db import models
from utilisateur.models import Utilisateur
# Create your models here.
import abonne


class Abonne(models.Model):
    utilisateur = models.OneToOneField(Utilisateur, on_delete=models.CASCADE)

def __str__(self):
    # if not self.utiliisateur:
    #     return ""
    return str(self.utilisateur.nom)