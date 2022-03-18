from django.db import models
from localisation.models import Localisation
from boite.models import Boite
from rubrique.models import Rubrique
# Create your models here.
class Service(models.Model):
    nom_service = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=200, null=True)
    id_localisation = models.OneToOneField(Localisation, on_delete=models.CASCADE)
    id_boite = models.ForeignKey(Boite, on_delete=models.CASCADE)
    id_rubrique = models.OneToOneField(Rubrique, on_delete=models.CASCADE)

def __str__(self):
        return self.nom_service