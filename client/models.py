from django.db import models
from utilisateur.models import Utilisateur

# Create your models here.
import abonne

class Client(models.Model):
    utilisateur = models.OneToOneField(Utilisateur, null=True, on_delete=models.CASCADE)
    # number = models.PositiveSmallIntegerField(default=1)
def __str__(self):
      return  str(self.utilisateur.nom)