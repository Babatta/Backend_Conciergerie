from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
class Utilisateur(models.Model):
    nom = models.CharField(max_length=100,null=True)
    prenom = models.CharField(max_length=100,null=True)
    adresse =  models.CharField(max_length=100,null=True)
    telephone = models.IntegerField(null=True)
    email =  models.EmailField(max_length=50,null=True)
    mdp = models.CharField(max_length=100,null=True)
    cni = models.IntegerField(null=True)
    date_creation = models.DateTimeField(auto_now_add=True,null=True)
    Mode = (('masculin', 'masculin'),
        ('feminin', 'feminin'))
    sexe = models.CharField(max_length=100, null=True, choices=Mode)

    # USERNAME_FIELD="email"
    # REQUIRED_FIELS=[]

    def __str__(self):
        return str(self.prenom)



