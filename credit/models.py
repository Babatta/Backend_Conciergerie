from django.db import models
from paiement.models import Paiement
# Create your models here.
class Credit(models.Model):
    id_paiement = models.OneToOneField(Paiement, on_delete=models.CASCADE)
    prix_credit = models.IntegerField(null=True)
    etat = models.BooleanField(null=True)

def __str__(self):
        return self.prix_credit