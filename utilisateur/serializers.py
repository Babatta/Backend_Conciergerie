from rest_framework import serializers

from utilisateur.models import Utilisateur

class UtilisateurSerializer(serializers.ModelSerializer):

    class Meta:
        model = Utilisateur
        fields = '__all__'
        #fields = ['id', 'nomEntreprise']
