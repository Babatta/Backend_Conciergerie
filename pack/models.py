from django.db import models
from boite.models import Boite
# Create your models here.
class Pack(models.Model):
    id_boite = models.ForeignKey(Boite, on_delete=models.CASCADE)
    nom_pack = models.CharField(max_length=50, null=True)
    prix_pack = models.IntegerField(null=True)
    nombre_credit = models.IntegerField(null=True)
    duree = models.IntegerField(null=True)

def __str__(self):
        return self.nom_pack