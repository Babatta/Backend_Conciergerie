from django.db import models
from utilisateur.models import Utilisateur
# Create your models here.
import abonne

class Administrateur(models.Model):
    utilisateur = models.OneToOneField(Utilisateur, null=True, on_delete=models.SET_NULL)
    # number = models.PositiveSmallIntegerField(default=1)
def __str__(self):
       return  str(self.utilisateur.nom)