from django.db import models
from abonne.models import Abonne
import datetime
import os

def filepath(request, filename):
    old_filname = filename,
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    filename = "%s%s", (timeNow, old_filname)
    return os.path.join('uploads/', filename)

class Boite(models.Model):
    nom_boite = models.CharField(max_length=50,null=True)
    descrition_boite = models.CharField(max_length=50,null=True)
    ninea_boite =  models.IntegerField(null=True)
    image = models.ImageField(upload_to=filepath,null=True,blank=True)
    date_creation = models.DateTimeField(auto_now_add=True, null=True)
    id_abonne = models.OneToOneField(Abonne,on_delete=models.CASCADE)
    def __str__(self):
        return self.nom_boite
