from django.db import models
from service.models import Service
# Create your models here.
class Publication(models.Model):
    id_service = models.ForeignKey(Service, on_delete=models.CASCADE)
    commentaire = models.CharField(max_length=200, null=True)
    nom_pub = models.CharField(max_length=100, null=True)
    date_debut = models.DateTimeField(auto_now_add=True, null=True)
    date_fin = models.DateTimeField(auto_now_add=True, null=True)

def __str__(self):
        return self.nom_pub