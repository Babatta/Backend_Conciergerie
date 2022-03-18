from django.db import models

# Create your models here.
class Localisation(models.Model):
    ville = models.CharField(max_length=50, null=True)
    commune = models.CharField(max_length=50, null=True)
    latitude = models.IntegerField(null=True)
    longitude = models.IntegerField(null=True)

def __str__(self):
        return self.commune