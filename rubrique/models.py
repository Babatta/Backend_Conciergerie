from django.db import models

# Create your models here.
class Rubrique(models.Model):
    nom_rubrique = models.CharField(max_length=50, null=True)
def __str__(self):
        return self.nom_rubrique