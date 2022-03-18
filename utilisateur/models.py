from django.db import models
class Utilisateur(models.Model):
    nom = models.CharField(max_length=100,null=True)
    prenom = models.CharField(max_length=100,null=True)
    adresse =  models.CharField(max_length=100,null=True)
    telephone = models.IntegerField(null=True)
    email =  models.EmailField(max_length=50,null=True)
    login = models.CharField(max_length=100,null=True)
    password = models.CharField(max_length=100,null=True)
    cni = models.IntegerField(null=True)
    date_creation = models.DateTimeField(auto_now_add=True,null=True)
    Mode = (('masculin', 'masculin'),
        ('feminin', 'feminin'))
    sexe = models.CharField(max_length=100, null=True, choices=Mode)

    def __str__(self):
        return self.prenom
