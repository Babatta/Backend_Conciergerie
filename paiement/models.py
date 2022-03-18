from django.db import models
from boite.models import Boite
# Create your models here.
class Paiement(models.Model):
    id_boite = models.ForeignKey(Boite, on_delete=models.CASCADE)
    nom_transaction = models.IntegerField(null=True)
    num_commande = models.IntegerField(null=True)
    montant = models.IntegerField(null=True)

def __str__(self):
        return self.nom_transaction